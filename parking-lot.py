def gun_saat_dakika(dakika):
    gun = int(dakika / 1440)
    saat = int((dakika % 1440) / 60)
    dakika = ((dakika % 1440) % 60)
    return gun, saat, dakika


TON_BASI_UCRET = 2.5  # (Aracın ağırlığının her 1 tonu için 2,5 TL giriş ücreti)
BIR_SAAT_AZ = 3 # Bir saatten az kalan araçlar için otopark ücreti
BIR_3_SAAT_AZ = 5 # 1-3 saat arası ücret
UC_5_SAAT_AZ = 7 # 3-5 saat arası
BES_10_SAAT_AZ = 10 # 5-10 saat arası
ON_24_SAAT_AZ = 14 # 10-24 saat arası
HER_24 = 15 # Her 24 saat için ödenecek ücret. Sonraki 24 saate kadar normal tarife uygulanacak.

MOTOSIKLET_KATSAYISI = 1
BINEK_KATSAYI = 2
MINIBUS_KATSAYISI = 3
OTOBUS_KATSAYISI = 3
KAMYON_KATSAYISI = 4
TIR_KATSAYISI = 4

GAZI_KATSAYI = 1.0
ENGELLI_KATSAYI = 0.5
# Gazi ve engelliler için indirim katsayısı

toplam_arac_say = 0
toplam_motor_say = 0
toplam_binek_say = 0
toplam_minibus_say = 0
toplam_otobus_say = 0
toplam_kamyon_say = 0
toplam_tır_say = 0

otopark_top_gelir = 0 #Otoparkın toplam geliri

motordan_gelir = 0
binekten_gelir = 0
minibusten_gelir = 0
otobusten_gelir = 0
kamyondan_gelir = 0
tırdan_gelir = 0

motor_sure=0
binek_sure=0
minibus_sure=0
otobus_sure=0
kamyon_sure=0
tır_sure=0
# Dakika cinsinden araç tiplerinin kaldığı süreler

bir_ton_az = 0 # Ağırlığı 1 tondan az olan binek araç sayısı
on_ton_fazla = 0 # Ağırlığı 10 tondan fazla olan otobüs, kamyon ve tır sınıfı araç sayısı
otuz_dkdan_az = 0 # 30 dakika veya daha kısa süre kalan motosiklet ve binek araç sayısı
bir_gun_uzun = 0 # 1 günden uzun kalan minibüs ve otobüs sayısı
otuz_gun_uzun = 0 # 30 günden uzun veya 1000 TL' den daha fazla gelir elde edilen araç sayısı

gazi_say=0
gazi_sure=0
engelli_say=0
engelli_sure=0
uc_saatten_uzun_indirimli=0
en_uzun_kalan=0 # En uzun kalan aracın kaldığı süre
en_uzundan_gelir=0

en_cok_gelir=-1 # Bir araçtan elde edilen en çok gelir
en_cok_gelirin_suresi=0


devam = 'E'

while devam == 'e' or devam == 'E':
    toplam_arac_say += 1
    indirim = 0
    ozel_durum=None
    arac_plaka = input("Araç plakasını giriniz:")

    arac_sinifi_kodu = int(input("Araç sınıfı kodunu giriniz(1-6 arasında):"))
    while arac_sinifi_kodu <= 0 or arac_sinifi_kodu > 6:
        arac_sinifi_kodu = int(input("Lütfen 1-6 arasında geçerli bir değer giriniz"))

    arac_agirligi = float(input("Araç ağırlığını kg cinsinden giriniz:"))
    while arac_agirligi <= 0:
        arac_agirligi = float(input("Lütfen geçerli bir değer giriniz:"))

    if arac_agirligi < 1000 and arac_sinifi_kodu == 2 :
        bir_ton_az += 1

    if arac_agirligi > 10000 and (arac_sinifi_kodu == 4 or arac_sinifi_kodu == 5 or arac_sinifi_kodu == 6) :
        on_ton_fazla += 1

    kalinan_sure = int(input("Otoparkta kalınan süreyi dakika cinsinden giriniz:"))
    while kalinan_sure <= 0:
        kalinan_sure = int(input("Lütfen geçerli bir değer giriniz"))

    if kalinan_sure <= 30 and (arac_sinifi_kodu == 1 or arac_sinifi_kodu == 2):
        otuz_dkdan_az += 1

    if kalinan_sure > 1440 and (arac_sinifi_kodu == 3 or arac_sinifi_kodu == 4):
        bir_gun_uzun += 1

    kalinan_gun, kalinan_saat, kalinan_dakika = gun_saat_dakika(kalinan_sure)

    surucu_ad_soyad = input("Sürücünün adını soyadını giriniz:")

    if arac_sinifi_kodu == 1 or arac_sinifi_kodu == 2:
        ozel_durum = input("Sürücünün özel durumunu giriniz (Yok/Gazi/Engelli) (Y/y/G/g/E/e karakterleri):")
        if ozel_durum == "G" or ozel_durum == "g":
            indirim = GAZI_KATSAYI
            gazi_say+=1
            gazi_sure+=kalinan_sure
        elif ozel_durum == "E" or ozel_durum == "e":
            indirim = ENGELLI_KATSAYI
            engelli_say+=1
            engelli_sure+=kalinan_sure
        while ozel_durum not in ["e","E","g","G","y","Y"]:
            ozel_durum = input("Lütfen geçerli bir değer giriniz (Y/y/G/g/E/e karakterleri):")

    if indirim > 0 and kalinan_sure > 180:
        uc_saatten_uzun_indirimli += 1

    if arac_sinifi_kodu == 1:
        arac_sinifi = 'Motosiklet'
        ucret_katsayisi = MOTOSIKLET_KATSAYISI
        toplam_motor_say += 1

    elif arac_sinifi_kodu == 2:
        arac_sinifi = 'Binek'
        ucret_katsayisi = BINEK_KATSAYI
        toplam_binek_say += 1

    elif arac_sinifi_kodu == 3:
        arac_sinifi = 'Minibüs'
        ucret_katsayisi = MINIBUS_KATSAYISI
        toplam_minibus_say += 1

    elif arac_sinifi_kodu == 4:
        arac_sinifi = 'Otobüs'
        ucret_katsayisi = OTOBUS_KATSAYISI
        toplam_otobus_say += 1

    elif arac_sinifi_kodu == 5:
        arac_sinifi = 'Kamyon'
        ucret_katsayisi = KAMYON_KATSAYISI
        toplam_kamyon_say += 1

    else:
        arac_sinifi = 'Tır'
        ucret_katsayisi = TIR_KATSAYISI
        toplam_tır_say += 1

    giris_ucreti = (arac_agirligi / 1000) * 2.5
    if kalinan_sure < 60:
        indirimsiz_ucret = (giris_ucreti + ucret_katsayisi * BIR_SAAT_AZ)
    elif kalinan_sure < 180:
        indirimsiz_ucret = (giris_ucreti + ucret_katsayisi * BIR_3_SAAT_AZ)
    elif kalinan_sure < 300:
        indirimsiz_ucret = (giris_ucreti + ucret_katsayisi * UC_5_SAAT_AZ)
    elif kalinan_sure < 600:
        indirimsiz_ucret = (giris_ucreti + ucret_katsayisi * BES_10_SAAT_AZ)
    elif kalinan_sure < 1440:
        indirimsiz_ucret = (giris_ucreti + ucret_katsayisi * ON_24_SAAT_AZ)
    else:
        if kalinan_sure % 1440 == 0:
            indirimsiz_ucret = (giris_ucreti + ((kalinan_gun* HER_24)) * ucret_katsayisi)
        elif kalinan_sure % 1440 < 60:
            indirimsiz_ucret = (giris_ucreti + ((kalinan_gun * HER_24) + BIR_SAAT_AZ) * ucret_katsayisi)
        elif kalinan_sure % 1440 < 180:
            indirimsiz_ucret = (giris_ucreti + ((kalinan_gun * HER_24) + BIR_3_SAAT_AZ) * ucret_katsayisi)
        elif kalinan_sure % 1440 < 300:
            indirimsiz_ucret = (giris_ucreti + ((kalinan_gun * HER_24) + UC_5_SAAT_AZ) * ucret_katsayisi)
        elif kalinan_sure % 1440 < 600:
            indirimsiz_ucret = (giris_ucreti + ((kalinan_gun * HER_24) + BES_10_SAAT_AZ) * ucret_katsayisi)
        else:
            indirimsiz_ucret = (giris_ucreti + ((kalinan_gun * HER_24) + ON_24_SAAT_AZ) * ucret_katsayisi)

    ucret = indirimsiz_ucret - indirimsiz_ucret * indirim
    otopark_top_gelir += ucret

    if kalinan_sure > en_uzun_kalan:
        en_uzun_kalan = kalinan_sure
        en_uzundan_gelir = ucret

    if kalinan_sure > 43200 or ucret > 1000 :
        otuz_gun_uzun += 1

    if arac_sinifi_kodu == 1 :
        motordan_gelir += ucret
        motor_sure += kalinan_sure

    elif arac_sinifi_kodu == 2 :
        binekten_gelir += ucret
        binek_sure += kalinan_sure
        if ucret > en_cok_gelir:
            en_cok_gelir = ucret
            en_cok_gelirin_suresi = kalinan_sure

    elif arac_sinifi_kodu == 3 :
        minibusten_gelir += ucret
        minibus_sure += kalinan_sure

    elif arac_sinifi_kodu == 4 :
        otobusten_gelir += ucret
        otobus_sure += kalinan_sure

    elif arac_sinifi_kodu == 5 :
        kamyondan_gelir += ucret
        kamyon_sure += kalinan_sure

    else:
        tırdan_gelir += ucret
        tır_sure += kalinan_sure

    print('Araç plakası:', arac_plaka)
    print('Araç sınıfı adı:', arac_sinifi)
    print(f"Araç ağırlığı: {arac_agirligi:.2f} kg")
    print(f"Aracın otoparkta kaldığı süre: {kalinan_gun} gün,{kalinan_saat} saat,{kalinan_dakika} dakika")
    print("Sürücünün adı soyadı:", surucu_ad_soyad)
    if ozel_durum == "G" or ozel_durum == "g":
        print("Sürücünün özel durumu: Gazi")
        print(f"Sürücüye uygulanan indirim oranı: %{100*indirim}")
    elif ozel_durum == "E" or ozel_durum == "e":
        print("Sürücünün özel durumu: Engelli")
        print(f"Sürücüye uygulanan indirim oranı: %{100*indirim}")
    print(f"Otopark ücreti : {ucret:.2f} TL")
    devam = input("Başka araç var mı? (e/E/h/H):")

print(f"Otoparkı kullanan toplam araç sayısı: {toplam_arac_say}")
print(f"Otoparkı kullanan motosiklet sayısı: {toplam_motor_say}. "
      f"Tüm araçlara oranı: %{toplam_motor_say/toplam_arac_say*100: .2f}")
print(f"Otoparkı kullanan binek sayısı: {toplam_binek_say}. "
      f"Tüm araçlara oranı: %{toplam_binek_say/toplam_arac_say*100: .2f}")
print(f"Otoparkı kullanan minibüs sayısı: {toplam_minibus_say}."
      f"Tüm araçlara oranı: %{toplam_minibus_say/toplam_arac_say*100: .2f}")
print(f"Otoparkı kullanan otobüs sayısı: {toplam_otobus_say}."
      f"Tüm araçlara oranı: %{toplam_otobus_say/toplam_arac_say*100: .2f}")
print(f"Otoparkı kullanan kamyon sayısı: {toplam_kamyon_say}."
      f"Tüm araçlara oranı: %{toplam_kamyon_say/toplam_arac_say*100: .2f}")
print(f"Otoparkı kullanan tır sayısı: {toplam_tır_say}."
      f" Tüm araçlara oranı: %{toplam_tır_say/toplam_arac_say*100: .2f}")

print(f"Otoparkın toplam geliri: {otopark_top_gelir:.2f} TL")
print(f"Motosiklet sınıfı için toplam gelir: {motordan_gelir:.2f} TL."
      f" Tüm gelire oranı: %{motordan_gelir/otopark_top_gelir*100: .2f}")
print(f"Binek sınıfı için toplam gelir: {binekten_gelir:.2f} TL."
      f" Tüm gelire oranı: %{binekten_gelir/otopark_top_gelir*100: .2f}")
print(f"Minibüs sınıfı için toplam gelir: {minibusten_gelir:.2f} TL."
      f" Tüm gelire oranı: %{minibusten_gelir/otopark_top_gelir*100: .2f}")
print(f"Otobüs sınıfı için toplam gelir: {otobusten_gelir:.2f} TL."
      f" Tüm gelire oranı: %{otobusten_gelir/otopark_top_gelir*100: .2f}")
print(f"Kamyon sınıfı için toplam gelir: {kamyondan_gelir:.2f} TL."
      f" Tüm gelire oranı: %{kamyondan_gelir/otopark_top_gelir*100: .2f}")
print(f"Tır sınıfı için toplam gelir: {tırdan_gelir:.2f} TL."
      f" Tüm gelire oranı: %{tırdan_gelir/otopark_top_gelir*100: .2f}")

motor_gun, motor_saat, motor_dakika = gun_saat_dakika(int(motor_sure/toplam_motor_say))
binek_gun, binek_saat, binek_dakika = gun_saat_dakika(int(binek_sure/toplam_binek_say))
minibus_gun, minibus_saat, minibus_dakika = gun_saat_dakika(int(minibus_sure/toplam_minibus_say))
otobus_gun, otobus_saat, otobus_dakika = gun_saat_dakika(int(otobus_sure/toplam_otobus_say))
kamyon_gun, kamyon_saat, kamyon_dakika = gun_saat_dakika(int(kamyon_sure/toplam_kamyon_say))
tır_gun, tır_saat, tır_dakika = gun_saat_dakika(int(tır_sure/toplam_tır_say))

print(f"Motosiklet sınıfının otoparkta ortalama kalma süresi: {motor_gun} gün,{motor_saat} saat, {motor_dakika} dakika."
      f"Motosiklet başına ortalama gelir: {(motordan_gelir/toplam_motor_say):.2f} TL.")

print(f"Binek sınıfının otoparkta ortalama kalma süresi: {binek_gun} gün,{binek_saat} saat, {binek_dakika} dakika."
      f"Binek başına ortalama gelir: {(binekten_gelir/toplam_binek_say):.2f} TL.")

print(f"Minibüs sınıfının otoparkta ortalama kalma süresi: {minibus_gun} gün,{minibus_saat} saat, {minibus_dakika} dakika."
      f"Minibüs başına ortalama gelir: {(minibusten_gelir/toplam_minibus_say):.2f} TL.")

print(f"Otobüs sınıfının otoparkta ortalama kalma süresi: {otobus_gun} gün,{otobus_saat} saat, {otobus_dakika} dakika."
      f"Otobüs başına ortalama gelir: {(otobusten_gelir/toplam_otobus_say):.2f} TL.")

print(f"Kamyon sınıfının otoparkta ortalama kalma süresi: {kamyon_gun} gün,{kamyon_saat} saat, {kamyon_dakika} dakika."
      f"Kamyon başına ortalama gelir: {(kamyondan_gelir/toplam_kamyon_say):.2f} TL.")

print(f"Tır sınıfının otoparkta ortalama kalma süresi: {tır_gun} gün,{tır_saat} saat, {tır_dakika} dakika."
      f"Tır başına ortalama gelir: {(tırdan_gelir/toplam_tır_say):.2f} TL.")

print(f"Ağırlığı 1 tondan az olan binek araçların tüm binek araçlar içindeki oranı: %{(bir_ton_az/toplam_binek_say)*100: .2f} ")
print(f"Ağırlığı 10 tondan fazla olan otobüs, kamyon ve tır sınıfı araçların, tüm otobüs, kamyon ve tır sınıfı araçlar içindeki oranı: %{on_ton_fazla/(toplam_otobus_say+toplam_kamyon_say+toplam_tır_say)*100: .2f} ")
print(f"Otoparkta 30 dakika veya daha kısa süre kalan motosiklet ve binek tipi araçların, tüm motosiklet ve binek tipi araçlar içindeki oranı: %{otuz_dkdan_az/(toplam_motor_say+toplam_binek_say)*100: .2f}")
print(f"Otoparkta 1 günden daha uzun süre kalan minibüs ve otobüs tipi araçların, tüm minibüs ve otobüs tipi araçlar içindeki oranı: %{bir_gun_uzun/(toplam_minibus_say+toplam_otobus_say)*100: .2f}")
print(f"Otoparkta 30 günden daha uzun süre kalan veya 1000 TL’den daha yüksek gelir edilen araçların, tüm araçlar içindeki oranı: %{otuz_gun_uzun/toplam_arac_say*100:.2f}")

engelli_gun, engelli_saat, engelli_dakika = gun_saat_dakika(int(engelli_sure/engelli_say))
gazi_gun, gazi_saat, gazi_dakika = gun_saat_dakika(gazi_sure/gazi_say)
print(f"Sürücüsü gazi olan araçların sayıları: {gazi_say}, tüm araçlar içindeki oranı: %{gazi_say/toplam_arac_say:.2f}, araç başına ortalama otoparkta kalma süreleri: {gazi_gun} gün, {gazi_saat} saat, {gazi_dakika} dakika.")
print(f"Sürücüsü engelli olan araçların sayıları: {engelli_say}, tüm araçlar içindeki oranı: %{engelli_say/toplam_arac_say:.2f}, araç başına ortalama otoparkta kalma süreleri: {engelli_gun} gün, {engelli_saat} saat, {engelli_dakika} dakika.")
print(f"Otoparkta 3 saatten daha uzun süre kalan indirim uygulanan araçların, tüm indirim uygulanan araçlar içindeki oranı: %{uc_saatten_uzun_indirimli/(gazi_say+engelli_say)*100: .2f}")

max_sure_gun, max_sure_saat, max_sure_dk = gun_saat_dakika(en_uzun_kalan)
print("En uzun süre otoparkta kalan aracın otoparkta kaldığı süre:", (max_sure_gun),"gün,", (max_sure_saat), "saat", (max_sure_dk), "dakika.")
print(f"Elde edilen gelir {en_uzundan_gelir: .2f} TL.")
max_gelir_gun, max_gelir_saat, max_gelir_dk = gun_saat_dakika(en_cok_gelirin_suresi)
print("En çok gelir getiren binek aracın otoparkta kaldığı süre:", (max_gelir_gun),"gün,", (max_gelir_saat), "saat", (max_gelir_dk), "dakika.")
print(f"Elde edilen gelir {en_cok_gelir: .2f} TL.")