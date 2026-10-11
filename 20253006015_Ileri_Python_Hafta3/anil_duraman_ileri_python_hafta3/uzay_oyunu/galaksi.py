"""Galaksi haritasını kurma ve JSON dosyasından yükleme yardımcıları."""
import json
from pathlib import Path
from typing import Any

def galaksi_kur(
    gezegenler: list[str],
    baglantilar: dict[str, list[str]],
    baslangic: str,
    **kwargs: Any,
) -> dict[str, Any]:
    """Galaksi sözlüğünü kurar; yakıt belirtilmezse 50 kullanır.

    Başlangıç gezegeni listede değilse ValueError yükseltir.
    """
    if baslangic not in gezegenler:
        raise ValueError(f"Başlangıç gezegeni listede yok: {baslangic}")
    return {
        "gezegenler": list(gezegenler),
        "baglantilar": {gezegen: list(hedefler) for gezegen, hedefler in baglantilar.items()},
        "konum": baslangic,
        "yakit": kwargs.get("yakit", 50),
    }

def galaksi_yukle(dosya: str | Path | None = None) -> dict[str, Any]:
    """JSON dosyasını okuyup galaksi_kur fonksiyonuna açılmış argümanlarla verir."""
    json_yolu = Path(dosya) if dosya is not None else Path(__file__).with_name("galaksi.json")
    with json_yolu.open("r", encoding="utf-8") as dosya_objesi:
        veri = json.load(dosya_objesi)
    return galaksi_kur(**veri)
