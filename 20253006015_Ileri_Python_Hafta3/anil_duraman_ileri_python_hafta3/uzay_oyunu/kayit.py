"""Görev kayıtlarını biçimlendirme yardımcıları."""
from typing import Any

def gorev_kaydi(
    baslik: str,
    *adimlar: str,
    oncelik: str = "normal",
    **ekler: Any,
) -> str:
    """Görev başlığını, adımlarını, önceliğini ve ek bilgileri metne dönüştürür.

    `oncelik` yalnızca isimli argüman olarak verilebilir.
    """
    oncelik_etiketleri = {"dusuk": "DÜŞÜK", "normal": "NORMAL", "yuksek": "YÜKSEK"}
    etiket = oncelik_etiketleri.get(oncelik.lower(), oncelik.upper())
    satirlar = [f"[{etiket}] {baslik}"]
    satirlar.extend(f"  {sira}. {adim}" for sira, adim in enumerate(adimlar, start=1))
    satirlar.extend(f"  {anahtar}: {deger}" for anahtar, deger in ekler.items())
    return "\n".join(satirlar)

if __name__ == "__main__":
    adimlar = ["Kredi kazan", "Pilot bul", "Hiperdrive al"]
    ekler = {"sorumlu": "Ayşe"}
    print(gorev_kaydi("Kara deliğe atla", *adimlar, oncelik="yuksek", **ekler))
    print()
    print(gorev_kaydi("Yeni görev", *["Haritayı incele"], oncelik="normal", **{"sorumlu": "Anıl"}))
