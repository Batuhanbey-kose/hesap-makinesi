print("""********************************
İşlem Listesi

1. Toplama İşlemi
2. Çıkarma İşlemi
3. Çarpma İşlemi1   
4. Bölme İşlemi
****************************************
""")   #burası ardınyodan bıldıgımız gibi print kısmı
while True:
    islem = input("İşlem Seçiniz (Çıkış için 'q' ya basalım): ")
    if islem == 'q':
        print("xbn fgb")
        quit()   #if islem dıyerek eger komutu verıyor mesela q basarsan quıt dıyıp parantesz acıyor
    elif islem == "1":
        print("------Toplama İşlemi------")
        sayi1 = int(input("1.Sayıyı Giriniz: "))
        sayi2 = int(input("2.Sayıyı Giriniz: "))
        sayi3 = int(input("3.Sayıyı Giriniz: "))
        print("{}  +   {} + {}   =  {}".format(sayi1, sayi2, sayi3, sayi1+sayi2+sayi3)) 
    elif islem == "2":
        print("------Çıkarma İşlemi------")
        sayi1 = int(input("1.Sayıyı Giriniz: "))
        sayi2 = int(input("2.Sayıyı Giriniz: "))
        sayi3 = int(input("3.Sayıyı Giriniz: "))
        print("{}  -   {}  -   {}    =  {}".format(sayi1, sayi2, sayi3, sayi1-sayi2-sayi3))
    elif islem == "3":
        print("------Çarpma İşlemi------")
        sayi1 = int(input("1.Sayıyı Giriniz: "))
        sayi2 = int(input("2.Sayıyı Giriniz: "))
        print("{}  x   {}    =  {}".format(sayi1, sayi2, sayi1*sayi2))
    elif islem == "4":
        print("------Bölme İşlemi------")
        try:
            sayi1 = int(input("1.Sayıyı Giriniz: "))
            sayi2 = int(input("2.Sayıyı Giriniz: "))
            print("{}  /   {}    =  {}".format(sayi1, sayi2, sayi1/sayi2))



        except ZeroDivisionError:
            print("Bir sayıyı 0'a bölemezsiniz!")
        except ValueError:
            print("Lütfen sadece sayı girin!")
    else:
        print("Geçersiz Seçenek...")