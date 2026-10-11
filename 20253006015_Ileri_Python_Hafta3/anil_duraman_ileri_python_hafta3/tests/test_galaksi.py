import pytest
from uzay_oyunu.galaksi import galaksi_kur, galaksi_yukle
from uzay_oyunu.araclar import en_bagli_gezegenler

def test_jsondan_galaksi_yukle():
    galaksi = galaksi_yukle()
    assert (galaksi["konum"], galaksi["yakit"]) == ("dünya", 100)

def test_yakit_varsayilani_50():
    galaksi = galaksi_kur(["mars"], {"mars": []}, "mars")
    assert galaksi["yakit"] == 50

def test_gecersiz_baslangic_value_error():
    with pytest.raises(ValueError):
        galaksi_kur(["mars"], {"mars": []}, "jupiter")

def test_bagli_gezegen_siralama():
    assert en_bagli_gezegenler(galaksi_yukle()) == ["sirius", "centauri", "dünya", "orion", "kara_delik"]
