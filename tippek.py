def main() -> None:

    szam_l_1 = int(input("Adjon meg egy számot 1-15 között. L: "))
    szam_l_2 = int(input("Adjon meg egy számot 1-15 között. L: "))
    szam_l_3 = int(input("Adjon meg egy számot 1-15 között. L: "))
    szam_l_4 = int(input("Adjon meg egy számot 1-15 között. L: "))

    szam_u_1 = int(input("Adjon meg egy számot 16-30 között. U: "))
    szam_u_2 = int(input("Adjon meg egy számot 16-30 között. U: "))
    szam_u_3 = int(input("Adjon meg egy számot 16-30 között. U: "))
    szam_u_4 = int(input("Adjon meg egy számot 16-30 között. U: "))

    szam_x_1 = int(input("Adjon meg egy számot 31-45 között. X: "))
    szam_x_2 = int(input("Adjon meg egy számot 31-45 között. X: "))
    szam_x_3 = int(input("Adjon meg egy számot 31-45 között. X: "))
    szam_x_4 = int(input("Adjon meg egy számot 31-45 között. X: "))

    szam_o_1 = int(input("Adjon meg egy számot 46-60 között. O: "))
    szam_o_2 = int(input("Adjon meg egy számot 46-60 között. O: "))
    szam_o_3 = int(input("Adjon meg egy számot 46-60 között. O: "))
    szam_o_4 = int(input("Adjon meg egy számot 46-60 között. O: "))

    szam_r_2 = int(input("Adjon meg egy számot 61-75 között. R: "))
    szam_r_3 = int(input("Adjon meg egy számot 61-75 között. R: "))
    szam_r_1 = int(input("Adjon meg egy számot 61-75 között. R: "))
    szam_r_4 = int(input("Adjon meg egy számot 61-75 között. R: "))

    with open('luxor_szamok.txt', 'w', encoding='utf-8') as szam:
        soremeles = '\n'
        szokoz = ' '
        szoveg = 'L számok: '
        szam.write(szoveg)
        szam.write(str(szam_l_1) + '')
        szam.write(szokoz)
        szam.write(str(szam_l_2) + '')
        szam.write(szokoz)
        szam.write(str(szam_l_3) + '')
        szam.write(szokoz)
        szam.write(str(szam_l_4) + '')
        szam.write(soremeles)
        szoveg1 = 'U számok: '
        szam.write(szoveg1)
        szam.write(str(szam_u_1) + '')
        szam.write(szokoz)
        szam.write(str(szam_u_2) + '')
        szam.write(szokoz)
        szam.write(str(szam_u_3) + '')
        szam.write(szokoz)
        szam.write(str(szam_u_4) + '')
        szam.write(soremeles)
        szoveg2 = 'X számok: '
        szam.write(szoveg2)
        szam.write(str(szam_x_1) + '')
        szam.write(szokoz)
        szam.write(str(szam_x_2) + '')
        szam.write(szokoz)
        szam.write(str(szam_x_3) + '')
        szam.write(szokoz)
        szam.write(str(szam_x_4) + '')
        szam.write(soremeles)
        szoveg3 = 'O számok: '
        szam.write(szoveg3)
        szam.write(str(szam_o_1) + '')
        szam.write(szokoz)
        szam.write(str(szam_o_2) + '')
        szam.write(szokoz)
        szam.write(str(szam_o_3) + '')
        szam.write(szokoz)
        szam.write(str(szam_o_4) + '')
        szam.write(soremeles)
        szoveg4 = 'R számok: '
        szam.write(szoveg4)
        szam.write(str(szam_r_1) + '')
        szam.write(szokoz)
        szam.write(str(szam_r_2) + '')
        szam.write(szokoz)
        szam.write(str(szam_r_3) + '')
        szam.write(szokoz)
        szam.write(str(szam_r_4) + '')


if __name__ == "__main__":
    main()
