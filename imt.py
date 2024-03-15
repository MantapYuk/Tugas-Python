print("\n Selamat Datang di program Indeks Masa Tubuh (IMT)")
print("===============================================================")
print("===================================================================>\n")

BB = int(input("Masukkan berat badan kg : "))
T_B = int(input("Masukkan tinggi badan cm : "))
TB = T_B / 100
IMT = BB / TB**2
print("Indeks Masa Tubuh Kamu = ", IMT) 
if IMT < 18.5 :
    print("Status Gizi anda : Underweight")
elif IMT <= 24.99 :
    print("Status Gizi anda : Normal range")
elif IMT <= 29.99 :
    print("Status Gizi anda : Overweight")
elif IMT <= 34.99 :
    print("Status Gizi anda : Obese class 1")
elif IMT <= 39.99 :
    print("Status Gizi anda : Obese class 2")
else : 
    print("Status Gizi anda : Obese class 3")
