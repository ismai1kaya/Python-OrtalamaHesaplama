print("****Sınav Notu Ortalaması Hesaplama Programı****")

vize = int(input("Vize notunuzu giriniz: "))
vize_yuzde = int(input("Vize yüzde kaç etki ediyor:"))
final = int(input("Final notunuzu giriniz: "))
final_yuzde = int(input("Final yüzde kaç etkiliyor: "))
ortalama = (vize*vize_yuzde + final*final_yuzde)/100

if (ortalama >= 90):
    print(ortalama," ortalaması ile AA Harf notunuzdur")
elif (ortalama >= 85):
    print(ortalama, " ortalaması ile BA Harf notunuzdur")
elif (ortalama >= 80):
    print(ortalama," ortalaması ile BB Harf notunuzdur")
elif (ortalama >= 75):
    print(ortalama," ortalaması ile CB Harf notunuzdur")
elif (ortalama >= 70):
    print(ortalama," ortalaması ile CC Harf notunuzdur")
elif (ortalama >= 65):
    print(ortalama," ortalaması ile DC Harf notunuzdur")
elif (ortalama >= 60):
    print(ortalama," ortalaması ile DD Harf notunuzdur")
elif (ortalama >= 55):
    print(ortalama," ortalaması ile FD Harf notunuzdur")
elif (ortalama < 50):
    print(ortalama," ortalaması ile FF Harf notunuzdur")