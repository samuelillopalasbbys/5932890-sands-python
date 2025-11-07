from signals import create_cossine_wave

def test1():
    t, y = create_cossine_wave(444, 2)
    assert y[0] == 1

test1()

from signals import create_sine_wave

def test2():
    t, y = create_sine_wave(20,20)
    assert y[0] == 0

