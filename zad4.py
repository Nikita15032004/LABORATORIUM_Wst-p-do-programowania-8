import numpy as np
import matplotlib.pyplot as plt

lista_wagi = [128, 64, 32, 16, 8, 4, 2, 1]
wagi = np.array(lista_wagi)

liczba_bin = np.random.randint(0, 2, size=8)

def wartosc_liczby_bin(wagi, liczba_bin):
    return np.sum(wagi * liczba_bin)

print("wagi:      ", wagi)
print("liczba_bin:", liczba_bin)
print("Wartość dziesiętna:", wartosc_liczby_bin(wagi, liczba_bin))
