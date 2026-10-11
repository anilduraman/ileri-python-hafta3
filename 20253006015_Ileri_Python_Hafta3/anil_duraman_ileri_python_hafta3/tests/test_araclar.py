from uzay_oyunu.araclar import hamle_sayaci, sure_olc

def test_hamle_sayaci_artar():
    say = hamle_sayaci()
    assert say() == 1
    assert say() == 2
    assert say() == 3

def test_sure_olc_argumanlari_aktarir(capsys):
    def carp(a: int, b: int = 1) -> int:
        return a * b
    olculu_carp = sure_olc(carp)
    assert olculu_carp(6, b=7) == 42
    assert "çalışma süresi" in capsys.readouterr().out
