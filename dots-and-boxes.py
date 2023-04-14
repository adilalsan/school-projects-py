dikey = ["A", "B", "C", "D", "E", "F", "G", "H"]
yatay = [1, 2, 3, 4, 5, 6, 7]


def sayi_al(alt_sinir, ust_sinir):
    sayi = input()
    while not sayi.isdigit():
        sayi = input("Lütfen bir tam sayı değer giriniz:")
    while int(sayi) < alt_sinir or int(sayi) > ust_sinir:
        sayi = input("Hatalı giriş yaptınız, lütfen tekrar giriniz:")
    return int(sayi)


print("Oynamak istediğiniz yatay çizgi sayısını giriniz:", end="")
yatay_sayisi = sayi_al(3, 7)
dikey_sayisi = yatay_sayisi + 1
dikey = dikey[0:dikey_sayisi]
yatay = yatay[0:yatay_sayisi]
konumlar = {}
for i in dikey:
    for j in range(yatay_sayisi):
        keyname = f"{j + 1}" + i
        konumlar[keyname] = " "


def tablo_yazdir():
    print("  ", end="")
    for z in dikey:
        print(z, end="   ")
    print()
    for i in range(2 * yatay_sayisi - 1):
        for j in range(2 * dikey_sayisi - 1):
            if i % 2 == 0 and j % 2 == 0:
                if j == 0:
                    print(int(((i + 1) / 2) + 1), end=" ")
                print(konumlar[f"{int((i + 1) / 2) + 1}"+dikey[int((j + 1) / 2)]], end="")
                if j == (2 * dikey_sayisi - 2):
                    print(" ", end="")
                    print(int(((i + 1) / 2) + 1), end=" ")
            elif i % 2 == 0 and j % 2 != 0:
                print("---", end="")
            if i % 2 != 0 and j % 2 == 0:
                print("  |", end="")
            elif i % 2 != 0 and j % 2 != 0:
                print(" ", end="")
        print()
    print("  ", end="")
    for z in dikey:
        print(z, end="   ")
    print()
def tas_yerlestirme():
    for i in range(int((len(konumlar)/2))):
        print("Hamle sırası beyazdadır.")
        print("Taşınızı yerleştirmek istediğiniz konumu giriniz:" ,end="")
        beyaz_konum=input()
        while beyaz_konum not in konumlar.keys() or beyaz_konum not in konumlar or konumlar[beyaz_konum] in ["S","B"] :
            print("Seçtiğiniz konum geçerli değilidir. Lütfen geçerli bir konum giriniz:" ,end="")
            beyaz_konum=input()
        konumlar[beyaz_konum] = "B"
        tablo_yazdir()
        print("Hamle sırası siyahtadır.")
        print("Taşınızı yerleştirmek istediğiniz konumu giriniz:", end="")
        siyah_konum = input()
        while siyah_konum not in konumlar.keys() or konumlar[siyah_konum] in ["S","B"] or siyah_konum not in konumlar:
            print("Seçtiğiniz konum geçerli değilidir. Lütfen geçerli bir konum giriniz:" ,end="")
            siyah_konum=input()
        konumlar[siyah_konum] = "S"
        tablo_yazdir()
def kare_sayma():
    beyaz_kare_elemanlari=[]
    siyah_kare_elemanlari=[]
    kare_sorgulayici = []
    for c in range (len(dikey)-1):
        for r in range (len(yatay)-1):
            kare_sorgulayici.append(konumlar[f"{yatay[r]}"+dikey[c]])
            kare_sorgulayici.append(konumlar[f"{yatay[r+1]}"+dikey[c]])
            kare_sorgulayici.append(konumlar[f"{yatay[r]}"+dikey[c+1]])
            kare_sorgulayici.append(konumlar[f"{yatay[r+1]}"+dikey[c+1] ])
            if kare_sorgulayici == ["B","B","B","B"]:
                beyaz_kare_elemanlari.append(f"{yatay[r]}"+dikey[c])
                beyaz_kare_elemanlari.append(f"{yatay[r+1]}"+dikey[c])
                beyaz_kare_elemanlari.append(f"{yatay[r]}"+dikey[c+1])
                beyaz_kare_elemanlari.append(f"{yatay[r+1]}"+dikey[c+1])
            elif kare_sorgulayici == ["S", "S", "S", "S"]:
                siyah_kare_elemanlari.append(f"{yatay[r]}"+dikey[c])
                siyah_kare_elemanlari.append(f"{yatay[r+1]}"+dikey[c])
                siyah_kare_elemanlari.append(f"{yatay[r]}"+dikey[c+1])
                siyah_kare_elemanlari.append(f"{yatay[r+1]}"+dikey[c+1])
            kare_sorgulayici = []
    return beyaz_kare_elemanlari, siyah_kare_elemanlari
def ilk_tas_eleme():
    beyaz_kare_elemanlari, siyah_kare_elemanlari=kare_sayma()
    beyaz_kare_sayisi=int(len(beyaz_kare_elemanlari)/4)
    siyah_kare_sayisi=int(len(siyah_kare_elemanlari)/4)
    for i in range (beyaz_kare_sayisi):
        print(f"Hamle sırası beyazdadır.{beyaz_kare_sayisi-i} adet taş eleme hakkına sahipsiniz. ", end="")
        elenen_siyah= input("Elemek istediğiniz siyah taşın konumunu giriniz:")
        while elenen_siyah not in konumlar or konumlar[elenen_siyah] in [" ", "B"] or elenen_siyah in (siyah_kare_elemanlari):
            print("Seçtiğiniz konum geçerli değilidir. Lütfen geçerli bir konum giriniz:", end="")
            elenen_siyah = input()
        konumlar[elenen_siyah]=" "
        tablo_yazdir()
    for i in range (siyah_kare_sayisi):
        print(f"Hamle sırası siyahtadır.{siyah_kare_sayisi-i} adet taş eleme hakkına sahipsiniz. ", end="")
        elenen_beyaz= input("Elemek istediğiniz beyaz taşın konumunu giriniz:")
        while elenen_beyaz not in konumlar or konumlar[elenen_beyaz] in [" ", "S"] or elenen_beyaz in (beyaz_kare_elemanlari):
            print("Seçtiğiniz konum geçerli değilidir. Lütfen geçerli bir konum giriniz:", end="")
            elenen_beyaz = input()
        konumlar[elenen_beyaz]=" "
        tablo_yazdir()
    if beyaz_kare_sayisi == 0 and siyah_kare_sayisi == 0:
        print(f"Hamle sırası beyazdadır.1 adet taş eleme hakkına sahipsiniz. ", end="")
        elenen_siyah = input("Elemek istediğiniz siyah taşın konumunu giriniz:")
        while elenen_siyah not in konumlar or konumlar[elenen_siyah] in [" ", "B"] or elenen_siyah in (
                siyah_kare_elemanlari):
            print("Seçtiğiniz konum geçerli değilidir. Lütfen geçerli bir konum giriniz:", end="")
            elenen_siyah = input()

def hareket_al(x):
    print("Yerini değiştirmek istediğiniz taşın şuanki konumunu ve taşın yeni konumunu giriniz:", end="")
    hareket = input()
    hareket_listesi = hareket.split(" ")
    while " " not in hareket or hareket_listesi[0] not in konumlar.keys() or hareket_listesi[1] not in konumlar.keys() \
            or konumlar[hareket_listesi[0]] != x or konumlar[hareket_listesi[1]] != " " or (hareket[0:1] != hareket[3:4] and hareket[1:2] != hareket[4:5]):
        print("Geçersiz bir hareket girdiniz. Lütfen tekrar giriniz:", end="")
        hareket = input()
        hareket_listesi =hareket.split (" ")
    return hareket

def final():
    def yeni_kare_kontrol(x):
        i = int(hareket[3:4])-1
        j = int(dikey.index(hareket[4:5]))
        try:
            kare_sorgulayici=[]
            kare_sorgulayici.append(konumlar[f"{yatay[i-1]}" + f"{dikey[j]}"])
            kare_sorgulayici.append(konumlar[f"{yatay[i-1]}" + f"{dikey[j+1]}"])
            kare_sorgulayici.append(konumlar[f"{yatay[i]}" + f"{dikey[j+1]}"])
            kare_sorgulayici.append(konumlar[f"{yatay[i]}" + f"{dikey[j]}"])
            if kare_sorgulayici == [x, x, x,x]:
                return True
        except IndexError:
            ""
        except KeyError:
            ""
        try:
            kare_sorgulayici = []
            kare_sorgulayici.append(konumlar[f"{yatay[i - 1]}" + f"{dikey[j-1]}"])
            kare_sorgulayici.append(konumlar[f"{yatay[i - 1]}" + f"{dikey[j]}"])
            kare_sorgulayici.append(konumlar[f"{yatay[i]}" + f"{dikey[j - 1]}"])
            kare_sorgulayici.append(konumlar[f"{yatay[i]}" + f"{dikey[j]}"])
            if kare_sorgulayici == [x, x, x,x]:
                return True
        except IndexError:
            ""
        except KeyError:
            ""
        try:
            kare_sorgulayici = []
            kare_sorgulayici.append(konumlar[f"{yatay[i + 1]}" + f"{dikey[j]}"])
            kare_sorgulayici.append(konumlar[f"{yatay[i + 1]}" + f"{dikey[j - 1]}"])
            kare_sorgulayici.append(konumlar[f"{yatay[i]}" + f"{dikey[j - 1]}"])
            kare_sorgulayici.append(konumlar[f"{yatay[i]}" + f"{dikey[j]}"])
            if kare_sorgulayici == [x, x, x,x]:
                return True
        except IndexError:
            ""
        except KeyError:
            ""
        try:
            kare_sorgulayici = []
            kare_sorgulayici.append(konumlar[f"{yatay[i+1]}" + f"{dikey[j]}"])
            kare_sorgulayici.append(konumlar[f"{yatay[i + 1]}" + f"{dikey[j + 1]}"])
            kare_sorgulayici.append(konumlar[f"{yatay[i]}" + f"{dikey[j + 1]}"])
            kare_sorgulayici.append(konumlar[f"{yatay[i]}" + f"{dikey[j]}"])
            if kare_sorgulayici == [x, x, x,x]:
                return True
        except IndexError:
            ""
        except KeyError:
            ""
    beyaz_kare_elemanlari, siyah_kare_elemanlari = kare_sayma()
    print("Hamle sırası beyazdadır.")
    while True:
        hareket = hareket_al("B")
        if hareket[1:2] == hareket[4:5]:
            aradaki_kare_sayisi = int(hareket[0:1]) - int(hareket[3:4]) - 1
            if aradaki_kare_sayisi < 0:
                index = int(hareket[0:1]) + 1
                for i in range(abs(aradaki_kare_sayisi)):
                    if konumlar[f"{index + i}" + hareket[1:2]] != " ":
                        ""
                    else:
                        break
                break
            else:
                index = int(hareket[0:1]) - 1
                for i in range(aradaki_kare_sayisi):
                    if konumlar[f"{index - i}" + hareket[1:2]] != " ":
                        ""
                    else:
                        break
                break
        else:
            aradaki_kare_sayisi = dikey.index(hareket[1:2]) - dikey.index(hareket[4:5]) - 1
            if aradaki_kare_sayisi < 0:
                index = dikey.index(hareket[1:2]) + 1
                for i in range(abs(aradaki_kare_sayisi)):
                    if konumlar[f"{hareket[0:1]}" + dikey[index + i]] != " ":
                        ""
                    else:
                        break
                break
            else:
                index = dikey.index(hareket[1:2]) - 1
                for i in range(aradaki_kare_sayisi):
                    if konumlar[f"{hareket[0:1]}" + dikey[index - i]] != " ":
                        ""
                    else:
                        break
                break
        print("Yapmaya çalıştığınız hareket geçerli değildir.")
    konumlar[hareket[3:5]] = "B"
    konumlar[hareket[0:2]] = " "
    tablo_yazdir()
    if yeni_kare_kontrol("B"):
        elenen_siyah = input("Elemek istediğiniz siyah taşın konumunu giriniz:")
        while elenen_siyah not in konumlar or konumlar[elenen_siyah] in [" ", "B"] or elenen_siyah in (
        siyah_kare_elemanlari):
            print("Seçtiğiniz konum geçerli değilidir. Lütfen geçerli bir konum giriniz:", end="")
            elenen_siyah = input()
        konumlar[elenen_siyah] = " "
        tablo_yazdir()
    print("Hamle sırası siyahtadır.")
    while True:
        hareket = hareket_al("S")
        if hareket[1:2] == hareket[4:5]:
            aradaki_kare_sayisi = int(hareket[0:1]) - int(hareket[3:4]) - 1
            if aradaki_kare_sayisi < 0:
                index = int(hareket[0:1]) + 1
                for i in range(abs(aradaki_kare_sayisi)):
                    if konumlar[f"{index + i}" + hareket[1:2]] != " ":
                        ""
                    else:
                        break
                break
            else:
                index = int(hareket[0:1]) - 1
                for i in range(aradaki_kare_sayisi):
                    if konumlar[f"{index - i}" + hareket[1:2]] != " ":
                        ""
                    else:
                        break
                break
        else:
            aradaki_kare_sayisi = dikey.index(hareket[1:2]) - dikey.index(hareket[4:5]) - 1
            if aradaki_kare_sayisi < 0:
                index = dikey.index(hareket[1:2]) + 1
                for i in range(abs(aradaki_kare_sayisi)):
                    if konumlar[f"{hareket[0:1]}" + dikey[index + i]] != " ":
                        ""
                    else:
                        break
                break
            else:
                index = dikey.index(hareket[1:2]) - 1
                for i in range(aradaki_kare_sayisi):
                    if konumlar[f"{hareket[0:1]}" + dikey[index - i]] != " ":
                        ""
                    else:
                        break
                break
        print("Yapmaya çalıştığınız hareket geçerli değildir.")
    konumlar[hareket[3:5]] = "S"
    konumlar[hareket[0:2]] = " "
    tablo_yazdir()
    if yeni_kare_kontrol("S"):
        elenen_beyaz = input("Elemek istediğiniz beyaz taşın konumunu giriniz:")
        while elenen_beyaz not in konumlar or konumlar[elenen_beyaz] in [" ", "S"] or elenen_beyaz in (
        beyaz_kare_elemanlari):
            print("Seçtiğiniz konum geçerli değilidir. Lütfen geçerli bir konum giriniz:", end="")
            elenen_beyaz = input()
        konumlar[elenen_beyaz] = " "
        tablo_yazdir()
def main():
    tablo_yazdir()
    tas_yerlestirme()
    ilk_tas_eleme()
    masadaki_taslar=[]
    for key in konumlar.keys():
        masadaki_taslar.append(konumlar[key])
    while masadaki_taslar.count("B") > 3 and masadaki_taslar.count("S") > 3:
        final()
        masadaki_taslar = []
        for key in konumlar.keys():
            masadaki_taslar.append(konumlar[key])
    if masadaki_taslar.count("B") <= 3 and masadaki_taslar.count("S") > 3:
        print("Oyunu siyahlar kazanmıştır.")
    elif masadaki_taslar.count("B") > 3 and masadaki_taslar.count("S") <= 3:
        print("Oyunu beyazlar kazanmıştır.")
main()
