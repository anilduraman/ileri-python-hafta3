"""Uzay oyunu: saf metin fonksiyonları ve etkileşimli yolculuk."""
from collections.abc import Callable
from typing import Any
from .araclar import hamle_sayaci
from .galaksi import galaksi_yukle

def envanter_metni(credits: bool, engines: bool, copilot: bool) -> str:
    """Mevcut eşyaları 'Sende: ...' biçiminde döndürür; eşya yoksa boş döndürür."""
    esyalar: list[str] = []
    if credits:
        esyalar.append("bol kredi")
    if engines:
        esyalar.append("güçlü motorlar")
    if copilot:
        esyalar.append("yetenekli bir pilot")
    return f"Sende: {', '.join(esyalar)}" if esyalar else ""

def hedef_menusu(hedefler: list[str]) -> str:
    """Hedefleri numaralı bir menü metni olarak döndürür."""
    satirlar = ["Nereye gitmek istersin?"]
    satirlar.extend(f"[{sira}] {hedef}" for sira, hedef in enumerate(hedefler, start=1))
    return "\n".join(satirlar)

def travel(
    galaksi: dict[str, Any],
    envanter: dict[str, bool] | None = None,
    input_fn: Callable[[str], str] = input,
    output_fn: Callable[[str], None] = print,
) -> None:
    """Oyuncuyu bağlantılı hedefler arasında gezdirir; kara deliğe varınca oyunu bitirir."""
    esyalar = envanter if envanter is not None else {
        "credits": True, "engines": False, "copilot": True
    }
    sayac = hamle_sayaci()
    while galaksi["konum"] != "kara_delik" and galaksi["yakit"] > 0:
        konum = galaksi["konum"]
        output_fn(f"Konum: {konum} | Yakıt: {galaksi['yakit']}")
        metin = envanter_metni(
            esyalar.get("credits", False),
            esyalar.get("engines", False),
            esyalar.get("copilot", False),
        )
        if metin:
            output_fn(metin)
        hedefler = galaksi["baglantilar"].get(konum, [])
        if not hedefler:
            output_fn("Buradan gidilebilecek bir hedef yok.")
            break
        output_fn(hedef_menusu(hedefler))
        secim = input_fn("Hedef numarası (çıkmak için q): ").strip().lower()
        if secim == "q":
            output_fn("Yolculuk sonlandırıldı.")
            return
        try:
            indeks = int(secim) - 1
        except ValueError:
            output_fn("Lütfen geçerli bir hedef numarası gir.")
            continue
        if not 0 <= indeks < len(hedefler):
            output_fn("Bu numarada bir hedef yok.")
            continue
        galaksi["konum"] = hedefler[indeks]
        galaksi["yakit"] -= 1
        sayac()
    if galaksi["konum"] == "kara_delik":
        output_fn(f"Oyunu {sayac()} hamlede bitirdin!")
    elif galaksi["yakit"] <= 0:
        output_fn("Yakıtın bitti; yolculuk sona erdi.")

if __name__ == "__main__":
    travel(galaksi_yukle())
