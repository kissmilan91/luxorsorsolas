import random
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


if __name__ == "__main__":
    main()
