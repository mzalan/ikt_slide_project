from Globals import *

def Fajlolvas():
    f = open("progress.txt", "r", encoding="utf-8")
    for sor in f:
        if sor.strip().split(':')[0] == "coins":
            r.Coins = int(sor.strip().split(':')[1])
        elif sor.strip().split(':')[0] == "best":
            r.Best = float(sor.strip().split(':')[1])
        else:
            sor = sor.strip().split(':')[1]
            r.beolvasottadatok.append(int(sor))
    f.close()
    for i in range(len(r.beolvasottadatok)):
        r.power_upgrades.append(r.default_upgrades[i]+r.default_upgrades[i]/5*r.beolvasottadatok[i])