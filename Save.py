from Globals import *

def Fajlolvas():
    adatok = []
    f = open("progress.txt", "r", encoding="utf-8")
    for sor in f:
        sor = sor.strip().split(':')[1]
        adatok.append(int(sor))
    f.close()
    for i in range(len(adatok)):
        r.power_upgrades.append(r.default_upgrades[i]+r.default_upgrades[i]/5*adatok[i])
    print(r.power_upgrades)