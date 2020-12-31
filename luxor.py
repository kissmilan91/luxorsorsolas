import random
import datetime
from typing import Set, List


def main() -> None:

    #  Luxor számoszlopok L 1-15
    l: Set[int] = set()
    while len(l) < 4:
        l.add(random.randint(1, 15))
    # print(l)
    # Számok rendezett kiírása:
    l_rendezve: List[int] = []
    for szam in range(1, 16):  # 1..15
        if szam in l:
            l_rendezve.append(szam)
    print(f'Az "L" Számok növekvő sorrendben: {l_rendezve}')

    #  Luxor számoszlopok U 16-30
    u: Set[int] = set()
    while len(u) < 4:
        u.add(random.randint(16, 30))
    # print(u)
    # Számok rendezett kiírása:
    u_rendezve: List[int] = []
    for szam in range(16, 31):  # 16..30
        if szam in u:
            u_rendezve.append(szam)
    print(f'Az "U" Számok növekvő sorrendben: {u_rendezve}')

    #  Luxor számoszlopok X 31-45
    x: Set[int] = set()
    while len(x) < 4:
        x.add(random.randint(31, 45))
    # print(x)
    # Számok rendezett kiírása:
    x_rendezve: List[int] = []
    for szam in range(31, 46):  # 31..45
        if szam in x:
            x_rendezve.append(szam)
    print(f'Az "X" Számok növekvő sorrendben: {x_rendezve}')

    #  Luxor számoszlopok O 46-60
    o: Set[int] = set()
    while len(o) < 4:
        o.add(random.randint(46, 60))
    # print(o)
    # Számok rendezett kiírása:
    o_rendezve: List[int] = []
    for szam in range(46, 61):  # 46..60
        if szam in o:
            o_rendezve.append(szam)
    print(f'Az "O" Számok növekvő sorrendben: {o_rendezve}')

    #  Luxor számoszlopok R 61-75
    r: Set[int] = set()
    while len(r) < 4:
        r.add(random.randint(61, 75))
    # print(r)
    # Számok rendezett kiírása:
    r_rendezve: List[int] = []
    for szam in range(61, 76):  # 61..75
        if szam in r:
            r_rendezve.append(szam)
    print(f'Az "R" Számok növekvő sorrendben: {r_rendezve}')
    # print(f'\n Az összes szám: {l_rendezve}{u_rendezve}{x_rendezve}{o_rendezve}{r_rendezve}')

    teljes_szamsor = l_rendezve + u_rendezve + x_rendezve + o_rendezve + r_rendezve

    # teljes_szamsor = []
    # teljes_szamsor.append(l_rendezve + u_rendezve + x_rendezve + o_rendezve + r_rendezve)

    print(f'A kihúzott számok: {teljes_szamsor}')

    with open('szamok.txt', 'a', encoding='utf-8') as szamsor:
        szoveg = 'Luxor sorsolás eredménye: '
        soremeles = '\n'
        ido = datetime.datetime.now()
        szamsor.write(szoveg)
        szamsor.write((ido.strftime("%Y %B %d %X ")))
        szamsor.writelines(str(teljes_szamsor))
        szamsor.write(soremeles)

    paros_szamok: List[int] = []
    paratlan_szamok: List[int] = []
    szamok = teljes_szamsor
    for i in szamok:
        if i % 2 == 0:
            paros_szamok.append(i)
    for j in szamok:
        if j % 2 == 1:
            paratlan_szamok.append(j)

    print(f'A kihúzott páros számok: {paros_szamok}')
    print(f'A kihúzott páratlan számok: {paratlan_szamok}')

    #  legnagyobb páratlan szám értékét és indexét a listában
    legnagyobb_paratlan: int = -1
    for i, item in enumerate(teljes_szamsor):
        if item % 2 == 1:   # Ha páratlan
            if legnagyobb_paratlan == -1:   # Az első páratlan szám a listában
                legnagyobb_paratlan = i   # Erre tekintünk a legnagyobb páratlan számként
            else:
                if item > szamok[legnagyobb_paratlan]:
                    legnagyobb_paratlan = i
    if legnagyobb_paratlan == -1:
        print('Nincs a listában páratlan szám')
    else:
        print(f'A legnagyobb páratlan szám értéke: {szamok[legnagyobb_paratlan]}, indexe: {legnagyobb_paratlan}')


if __name__ == "__main__":
    main()
