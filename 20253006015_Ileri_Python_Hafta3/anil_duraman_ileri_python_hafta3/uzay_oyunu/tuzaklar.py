"""Değiştirilebilir varsayılan argüman örneğinin düzeltilmiş hali."""

def yakit_ekle(miktar: int, depo: list[int] | None = None) -> list[int]:
    """Yakıt miktarını depoya ekler; yeni çağrılar arasında liste paylaşmaz."""
    if depo is None:
        depo = []
    depo.append(miktar)
    return depo
