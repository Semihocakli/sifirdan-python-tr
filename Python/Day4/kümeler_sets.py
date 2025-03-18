# kümeler (sets), matematikteki kümelerle aynı işlevi görürler.
# Kümeler, sıralı olmayan ve benzersiz elemanlardan oluşan bir veri yapısıdır.

boş_küme = set() 
print(boş_küme)

küme = set(["elma", "armut", "kebap"])

import random

liste = [random.randint(0, 10000) for i in range(1000)]

for i in liste:
    if i < 100:
        print(i)

# küme comprehension
küme = {i for i in liste if i < 100}
print(küme)

# add() metodu, kümelere eleman eklemek için kullanılır.
küme.add(100)
print(küme)

# remove() metodu, kümeden eleman silmek için kullanılır.
küme.remove(100)
print(küme)

# discard() metodu, kümeden eleman silmek için kullanılır.
küme.discard(100)
print(küme)

# pop() metodu, kümeden rastgele bir elemanı siler ve geri döndürür.
print(küme.pop())

# union() metodu, iki kümenin birleşimini döndürür.
küme1 = {1, 2, 3, 4, 5}
küme2 = {4, 5, 6, 7, 8}
print(küme1.union(küme2))

# intersection() metodu, iki kümenin kesişimini döndürür.
print(küme1.intersection(küme2))

# difference() metodu, iki kümenin farkını döndürür.
print(küme1.difference(küme2))

# symmetric_difference() metodu, iki kümenin simetrik farkını döndürür.
print(küme1.symmetric_difference(küme2))

# issubset() metodu, bir kümenin başka bir kümenin alt kümesi olup olmadığını kontrol eder.
küme3 = {1, 2, 3}
print(küme3.issubset(küme1))

