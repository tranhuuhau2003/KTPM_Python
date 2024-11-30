
from main import tinhtiendien

def test_tinhtiendien_usage():
    assert tinhtiendien(20) == 20 * 1.678

def test_tinhtiendien_usage_1():
    assert tinhtiendien(75) == (75 - 50) * 1.734 + 50 * 1.678

def test_tinhtiendien_usage_2():
    assert tinhtiendien(124) == (124 - 100) * 2.014 + 50 * 1.734 + 50 * 1.678

def test_tinhtiendien_usage_3():
    assert tinhtiendien(250) == (250 - 200) * 2.536 + 100 * 2.014 + 50 * 1.734 + 50 * 1.678

def test_tinhtiendien_usage_5():
    assert tinhtiendien(320) == (320 - 300) * 2.834 + 100 * 2.536 + 100 * 2.014 + 50 * 1.734 + 50 * 1.678

def test_tinhtiendien_usage_6():
    assert tinhtiendien(475) == (475 - 400) * 2.927 + 100 * 2.834 + 100 * 2.536 + 100 * 2.014 + 50 * 1.734 + 50 * 1.678
