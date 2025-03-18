demet = (1,2,3,4, "isa", "musa" )

print(demet)
print(type(demet))

# Alt çizgi içermeyen list metodlarını listele ve yazdır
filtered_methods = [i for i in dir(list) if not "_" in i]
#                  [ifade for eleman in koleksiyon if koşul]
print(filtered_methods)

"""
1.) dir(list) ile list sınıfının tüm metod ve özelliklerini al.
2.) Bu metod ve özellikler üzerinde for döngüsüyle tek tek gez.
3.) Her elemanı i değişkenine ata.
4.) Eğer i içinde alt çizgi ("_") yoksa, bu elemanı sonuç listesine ekle.
5.) Tüm döngü bittiğinde, alt çizgi içermeyen metod ve özelliklerin listesini oluştur.
"""


for i in range(10):
    a = i * i
    print(f"{i}. indis a = {a} ")

