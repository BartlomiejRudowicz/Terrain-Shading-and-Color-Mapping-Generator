from __future__ import division
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import colorsys as cs
import math

def hsv2rgb(h, s, v):
    return cs.hsv_to_rgb(h, s, v)

def przelicz_kolor(wartosc, jasnosc, max_w, min_w):
    odcien=(max_w-wartosc)*(1/3)/(max_w-min_w)
    nasycenie=1
    return hsv2rgb(odcien, nasycenie, jasnosc)

def generuj_mape_cieniowania(dane, szerokosc, wysokosc, max_w, min_w):
    kierunek_swiatla=[0.5, 0.5, 1]
    dlugosc_wektora=math.sqrt(sum([x**2 for x in kierunek_swiatla]))
    kierunek_swiatla=[x/dlugosc_wektora for x in kierunek_swiatla]
    obraz=[[[0, 0, 0] for _ in range(wysokosc)] for _ in range(szerokosc)]
    for i in range(1, szerokosc):
        for j in range(1, wysokosc):
            v1=[1, 0, dane[i-1][j]-dane[i][j]]
            v2=[0, 1, dane[i][j-1]-dane[i][j]]
            normalna=[
                v1[1]*v2[2]-v1[2]*v2[1],
                v1[2]*v2[0]-v1[0]*v2[2],
                v1[0]*v2[1]-v1[1]*v2[0]
            ]
            dlugosc_normalnej=math.sqrt(sum([x**2 for x in normalna]))
            normalna=[x/dlugosc_normalnej for x in normalna]
            iloczyn_skalarny=sum([normalna[k]*kierunek_swiatla[k] for k in range(3)])
            jasnosc=max(iloczyn_skalarny, 0.2)
            obraz[i][j]=przelicz_kolor(dane[i][j], jasnosc, max_w, min_w)
    plt.figure(figsize=(10, 10))
    plt.imshow(obraz)
    plt.savefig('kolorowanie.pdf')

with open("big.dem", "r") as f:
    linie=f.readlines()

szerokosc, wysokosc, odleglosc=map(int, linie[0].split())
dane=[list(map(float, linia.split())) for linia in linie[1:]]

max_wartosc=max(map(max, dane))
min_wartosc=min(map(min, dane))
generuj_mape_cieniowania(dane, szerokosc, wysokosc, max_wartosc, min_wartosc)