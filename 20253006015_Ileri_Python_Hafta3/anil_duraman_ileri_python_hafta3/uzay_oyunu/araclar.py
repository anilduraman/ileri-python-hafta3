"""Closure, sıralama ve çalışma süresi araçları."""
from collections.abc import Callable
from functools import wraps
from time import perf_counter
from typing import Any, ParamSpec, TypeVar

P = ParamSpec("P")
R = TypeVar("R")

def hamle_sayaci() -> Callable[[], int]:
    """Her çağrıda bir artan sayacı kapatan bir fonksiyon döndürür."""
    sayi = 0
    def say() -> int:
        nonlocal sayi
        sayi += 1
        return sayi
    return say

def en_bagli_gezegenler(galaksi: dict[str, Any]) -> list[str]:
    """Gezegenleri bağlantı sayısı azalan, eşitlikte alfabetik sırayla döndürür."""
    baglantilar = galaksi["baglantilar"]
    gezegenler = galaksi["gezegenler"]
    return sorted(gezegenler, key=lambda gezegen: (-len(baglantilar.get(gezegen, [])), gezegen))

def sure_olc(fonksiyon: Callable[P, R]) -> Callable[P, R]:
    """Fonksiyonu sarmalar, çalıştırma süresini saniye cinsinden yazdırır."""
    @wraps(fonksiyon)
    def sarmalayici(*args: P.args, **kwargs: P.kwargs) -> R:
        baslangic = perf_counter()
        try:
            return fonksiyon(*args, **kwargs)
        finally:
            gecen = perf_counter() - baslangic
            print(f"{fonksiyon.__name__} çalışma süresi: {gecen:.6f} saniye")
    return sarmalayici
