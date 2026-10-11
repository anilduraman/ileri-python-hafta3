# İleri Python Programlama – Hafta 3 Lab Ödevi
**Öğrenci:** Anıl Duraman  
**Bölüm:** Yazılım Geliştirme  
**Öğrenci No:** 20253006015

Bu proje, verilen Hafta 3 PDF'sindeki görevleri temel alan, kendi başına çalıştırılabilir bir örnek çözümdür. Hafta 2'deki mevcut uzay oyunu deposu paylaşılmadığı için bu çözüm onunla birleştirilmiş değil; bağımsız bir başlangıç projesidir.

## Kurulum ve test
Python 3.11 veya üzeri önerilir.

```bash
uv sync
uv run pytest
```

Alternatif:
```bash
python -m pip install pytest
python -m pytest
```

## Çalıştırma
```bash
uv run python -m uzay_oyunu.oyun
```

Oyunda bağlantılı hedeflerden numara seç. Kara deliğe ulaşınca oyun sona erer.

## Görevlerin karşılığı
1. `uzay_oyunu/oyun.py`: `envanter_metni()` ve `hedef_menusu()` saf fonksiyonları.
2. `uzay_oyunu/kayit.py`: `gorev_kaydi()`; `*` ve `**` ile çağrı örnekleri.
3. `uzay_oyunu/galaksi.json` ve `uzay_oyunu/galaksi.py`: JSON haritası ve `galaksi_kur(**veri)`.
4. `tests/test_tuzaklar.py` ve `kapsam.md`: değiştirilebilir varsayılan argüman ve kapsam örnekleri.
5. `uzay_oyunu/araclar.py`: `hamle_sayaci()` ve `en_bagli_gezegenler()`.
6. Bonus: `sure_olc()` zaman ölçüm sarmalayıcısı.

**Not:** PDF, derste gösterilen üç kapsam örneğine atıf yapıyor ancak örnek kodları PDF'de bulunmuyor. `kapsam.md` içinde konuya uygun temsilî örnekler var; ders notlarındaki örneklerle karşılaştırıp gerekirse uyarlamalısın.

## Git commit önerisi
PDF her görev için en az bir commit istiyor. Her görevi tamamlayıp testleri çalıştırdıktan sonra ayrı commit oluştur. Örneğin:
```bash
git init
git add tests/test_fonksiyonlar.py uzay_oyunu/oyun.py
git commit -m "Görev 1: saf fonksiyonlar ve testler"
git add uzay_oyunu/kayit.py tests/test_kayit.py
git commit -m "Görev 2: esnek parametreler"
git add uzay_oyunu/galaksi.py uzay_oyunu/galaksi.json tests/test_galaksi.py
git commit -m "Görev 3: haritayı JSON dosyasına taşı"
git add tests/test_tuzaklar.py kapsam.md uzay_oyunu/tuzaklar.py
git commit -m "Görev 4: tuzaklar ve kapsam"
git add uzay_oyunu/araclar.py uzay_oyunu/oyun.py tests/test_araclar.py
git commit -m "Görev 5: closure ve lambda"
git add .
git commit -m "Bonus: çalışma süresi ölçümü"
```

GitHub deposunu kendi hesabında oluşturup yükledikten sonra bağlantısını teslim etmelisin.
