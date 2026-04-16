import unittest
from cart import ShoppingCart

class TestShoppingCart(unittest.TestCase):
    def setUp(self):
        # her testten önce sıfırdan boş sepet oluştur
        self.cart = ShoppingCart()

    def test_add_item(self):
        # sepete 2 adet elma ekleyelim
        self.cart.add_item("Apple", 1.50, 2)
        self.assertEqual(self.cart.get_total(), 3.00)
    
    def test_add_same_item_twice(self):
        # aynı ürünü 2 kere ekleyince sayının toplanması lazım (burada quantity eziliyordu düzeltildi)
        self.cart.add_item("Apple", 1.50, 2)
        self.cart.add_item("Apple", 1.50, 3)
        
        self.assertEqual(self.cart.get_item_count(), 5)
        # 5 * 1.50 = 7.5
        self.assertEqual(self.cart.get_total(), 7.50)

    def test_negatif_ve_sifir_ekleme(self):
        # miktar 0 olamaz
        with self.assertRaises(ValueError):
            self.cart.add_item("Banana", 1.00, 0)
        
        # eksi miktar ve eksi fiyat eklenemez
        with self.assertRaises(ValueError):
            self.cart.add_item("Banana", 1.00, -1)
        with self.assertRaises(ValueError):
            self.cart.add_item("Banana", -1.00, 1)

    def test_remove_item(self):
        self.cart.add_item("Apple", 1.50)
        self.cart.remove_item("Apple")
        
        # zaten silinmiş şeyi tekrar silmeye çalışınca KeyError fırlatmalı
        with self.assertRaises(KeyError):
            self.cart.remove_item("Apple")

    def test_flat_discount(self):
        self.cart.add_item("Orange", 10.00, 4) # subtotal 40 oldu, 30 limitini geçiyor
        self.cart.apply_discount("FLAT5") # 5 lira net indirim -> geriye 35 kalmalı
        self.assertEqual(self.cart.get_total(), 35.00)

    def test_percent_discount(self):
        self.cart.add_item("Orange", 10.00, 4) # subtotal 40
        self.cart.apply_discount("SAVE10") # yüzde 10 indirim yani 4 lira düşecek
        # print("Total:", self.cart.get_total())
        self.assertEqual(self.cart.get_total(), 36.00)

    def test_hatali_indirim_kodu(self):
        self.cart.add_item("Orange", 10.00, 4)
        with self.assertRaises(ValueError):
            self.cart.apply_discount("KAFADAN_KOD")

    def test_discount_tam_sinirda(self):
        # sepet limiti tam 30 lirayı bulduğunda
        self.cart.add_item("Mango", 30.00, 1) 
        self.cart.apply_discount("FLAT5") # min threshold 30 verilmiş, indirim uygulanmalı
        self.assertEqual(self.cart.get_total(), 25.00)

    def test_discount_limitinin_altinda(self):
        self.cart.add_item("Mango", 29.00, 1) # 29 < 30
        with self.assertRaises(ValueError):
            self.cart.apply_discount("FLAT5")

    def test_clear_cart(self):
        self.cart.add_item("Mango", 30.00, 1)
        self.cart.clear() # her şeyi sıfırladık
        
        self.assertEqual(self.cart.get_total(), 0.00)
        self.assertEqual(self.cart.get_item_count(), 0)

    def test_get_item_count(self):
        # TDD süreci - bu metot hiç yoktu NotImplemented error veriyordu
        # Testi yazdım, patladığını gördüm sonra cart.py içine implement ettim
        self.cart.add_item("Apple", 1.50, 2)
        self.cart.add_item("Mango", 2.00, 1)
        
        # Toplamda benden 3 ürün dönmesi lazım
        self.assertEqual(self.cart.get_item_count(), 3)

if __name__ == '__main__':
    unittest.main()
