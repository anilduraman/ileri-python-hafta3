from uzay_oyunu.tuzaklar import yakit_ekle

def test_yakit_ekle_ayri_cagrilarda_depo_paylasmaz():
    ilk = yakit_ekle(10)
    ikinci = yakit_ekle(20)
    assert ilk == [10]
    assert ikinci == [20]
    assert ilk is not ikinci

def test_verilen_depo_kullanilir():
    depo = [5]
    sonuc = yakit_ekle(10, depo)
    assert sonuc == [5, 10]
    assert sonuc is depo
