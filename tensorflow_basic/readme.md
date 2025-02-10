# Tensör Nedir?
Tensör, temel olarak çok boyutlu bir veri yapısıdır. TensorFlow'da, tensörler verileri temsil etmek için kullanılır. Tensörler, sayıları düzenli bir şekilde saklamak için bir tür konteyner gibidir.

## Tensörlerin Boyutları
Tensörlerin boyutları, onların kaç boyutlu olduğunu belirtir. İşte bazı örnekler:

### 1. Skalar (0. Dereceden Tensör)
Tek bir sayı. Örneğin, 5 bir skaler tensördür. TensorFlow'da şöyle tanımlanır:

```python
scalar = tf.constant(5)
```

### 2. Vektör (1. Dereceden Tensör)
Bir dizi sayı. Örneğin, [1, 2, 3] bir vektördür. TensorFlow'da şöyle tanımlanır:

```python
vector = tf.constant([1, 2, 3])
```

### 3. Matris (2. Dereceden Tensör)
Satır ve sütunlardan oluşan bir dizi. Örneğin, 

```python
matrix = tf.constant([[1, 2, 3], [4, 5, 6]])
```

### 4. Tensör (3. Dereceden veya daha yüksek)
3. dereceden bir tensör, bir matrisin içinde matrisler barındırır. Örneğin, bir renkli görüntü, 3 boyutlu bir tensör olarak düşünülebilir (yükseklik, genişlik, renk kanalları).

```python
     tensör_3d = tf.constant([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
```


## Tensörlerin Kullanımı
TensorFlow'da tensörler, makine öğrenimi ve derin öğrenme modellerinde verileri temsil etmek için kullanılır. Örneğin, bir görüntü verisi, bir tensör olarak temsil edilir ve bu tensör, modelin eğitilmesi veya tahmin yapılması için kullanılır.

## Özet

- Tensörler, sayıları düzenli bir şekilde saklamak için kullanılan çok boyutlu veri yapılarıdır.
- Farklı boyutlarda (skalar, vektör, matris, vb.) olabilirler.
- TensorFlow, bu tensörleri kullanarak verileri işler ve makine öğrenimi modelleri oluşturur.