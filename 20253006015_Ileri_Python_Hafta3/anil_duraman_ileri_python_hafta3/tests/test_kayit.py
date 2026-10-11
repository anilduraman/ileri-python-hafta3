from uzay_oyunu.kayit import gorev_kaydi

def test_gorev_kaydi_ornek_ve_esnek_argumanlar():
    adimlar = ["Kredi kazan", "Pilot bul", "Hiperdrive al"]
    ekler = {"sorumlu": "Ayşe"}
    assert gorev_kaydi("Kara deliğe atla", *adimlar, oncelik="yuksek", **ekler) == (
        "[YÜKSEK] Kara deliğe atla\n"
        "  1. Kredi kazan\n"
        "  2. Pilot bul\n"
        "  3. Hiperdrive al\n"
        "  sorumlu: Ayşe"
    )

def test_oncelik_varsayilani():
    assert gorev_kaydi("Haritayı tara") == "[NORMAL] Haritayı tara"
