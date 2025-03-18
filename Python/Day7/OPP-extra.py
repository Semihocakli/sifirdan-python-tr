# 1.)
"""
Sınıflar, nesneleri oluşturmak için kullanılan bir şablondur. 
Örneğin, bir "Araba" sınıfı, arabaların nasıl oluşturulacağını ve davranacağını tanımlar. 
Nesneler ise sınıflardan türetilen örneklerdir. Yani, bir "Araba" sınıfından bir "Toyota" nesnesi oluşturabilirsiniz
"""

class Araba:
    def __init__(self, marka, model):
        self.marka = marka
        self.model = model

araba1 = Araba("Toyota", "Corolla")

# 2.)
"""
Sınıflar, özellikler (attributes) ve metotlar (methods) içerebilir. 
Özellikler, nesnenin durumunu temsil ederken, metotlar nesnenin davranışlarını tanımlar.
"""
class Araba:
    def __init__(self, marka, model):
        self.marka = marka
        self.model = model

    def calistir(self):
        print(f"{self.marka} {self.model} çalıştırıldı.")

araba1 = Araba("Toyota", "Corolla")
araba1.calistir()  # Çıktı: "Toyota Corolla çalıştırıldı."
"""
Araba = bir sınıftır.
araba1 = bir nesnedir.
marka ve model = özelliklerdir (attributes), çünkü bunlar araba1 nesnesinin durumunu temsil ederler.
calistir = bir metottur (method), çünkü bu metot araba1 nesnesinin davranışını tanımlar.
"""

# 3.)
"""
Miras(Inheritance), bir sınıfın diğer bir sınıftan özellikler ve metotlar almasına olanak tanır. 
Bu, kodunuzu yeniden kullanılabilir hale getirir.
"""
class Otobus(Araba):
    def __init__(self, marka, model, yolcu_sayisi):
        super().__init__(marka, model)
        self.yolcu_sayisi = yolcu_sayisi

    def taşı(self):
        print(f"{self.marka} {self.model}, {self.yolcu_sayisi} yolcu taşıyor.")

otobus1 = Otobus("Mercedes", "Sprinter", 20)
otobus1.calistir()  # Miras aldığı metodu kullanabilir.
otobus1.taşı()     # Kendi metodu da kullanılabilir.

# 4.)
"""
Çok biçimlilik(Polymorphism), farklı sınıfların aynı metodları farklı şekillerde uygulayabilmesini ifade eder. 
Bu, kodunuzun daha esnek olmasını sağlar.
"""
class Sekil:
    def alan_hesapla(self):
        pass

class Dikdortgen(Sekil):
    def __init__(self, uzunluk, genislik):
        self.uzunluk = uzunluk
        self.genislik = genislik

    def alan_hesapla(self):
        return self.uzunluk * self.genislik

class Daire(Sekil):
    def __init__(self, yaricap):
        self.yaricap = yaricap

    def alan_hesapla(self):
        return 3.14 * self.yaricap ** 2

sekil1 = Dikdortgen(5, 4)
sekil2 = Daire(3)

print(sekil1.alan_hesapla())  # Çıktı: 20
print(sekil2.alan_hesapla())  # Çıktı: 28.26
