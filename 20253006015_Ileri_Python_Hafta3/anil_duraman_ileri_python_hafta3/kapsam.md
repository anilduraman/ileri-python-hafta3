# Görev 4(b) – Kapsam örnekleri

PDF, derste gösterilen üç örneğe atıf yapıyor ancak bu örneklerin kodları PDF'de bulunmuyor. Aşağıdakiler konuyu açıklayan temsilî örneklerdir; öğretim üyesinin sınıfta verdiği örneklerle aynı oldukları iddia edilmemektedir.

## Örnek 1 – Yerel değişken
```python
def selamla():
    mesaj = "Merhaba"
    return mesaj
print(selamla())
```
- Tahmin: `Merhaba`
- Gerçek çıktı: `Merhaba`
- Neden: `mesaj`, fonksiyon içindeki yerel değişkendir ve `return` ile dışarı döndürülür.

## Örnek 2 – İç fonksiyon dış değişkeni okuyabilir
```python
def dis_fonksiyon():
    renk = "mavi"
    def ic_fonksiyon():
        return renk
    return ic_fonksiyon()
print(dis_fonksiyon())
```
- Tahmin: `mavi`
- Gerçek çıktı: `mavi`
- Neden: İç fonksiyon, kapsayan fonksiyonun kapsamındaki değişkeni okuyabilir.

## Örnek 3 – UnboundLocalError
```python
sayac = 10
def artir():
    sayac = sayac + 1
    return sayac
artir()
```
- Tahmin: `UnboundLocalError`
- Gerçek sonuç: `UnboundLocalError` (tam hata metni Python sürümüne göre değişebilir).
- Neden: Fonksiyon içinde `sayac` adına atama bulunduğundan Python onu yerel kabul eder. Sağ tarafta okunurken henüz yerel değer atanmış değildir. Ödev `global` kullanımını yasakladığı için çözüm olarak parametre/return veya iç fonksiyonla `nonlocal` yaklaşımı kullanılabilir.

## Değiştirilebilir varsayılan argüman tuzağı
Hatalı biçimde `def yakit_ekle(miktar, depo=[]):` yazılırsa, varsayılan liste fonksiyon tanımlanırken bir kez oluşturulur ve çağrılar arasında paylaşılır. `depo=None` kullanıp içeride liste oluşturmak bu sorunu giderir. Düzeltilmiş kod `uzay_oyunu/tuzaklar.py` içindedir.
