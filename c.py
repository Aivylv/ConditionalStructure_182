#1. menerima input persentase dari user
percentage = float(input("Enter the student's percentage: ")) #meminta user untuk memasukkan nilai persentase siswa.
if percentage >= 90:
    print("Excellent performance") #Jika nilai ≥ 90, maka "Excellent performance".
elif percentage >= 80:
    print("Very Good performance") #Jika nilai ≥ 80 tapi < 90, maka "Very Good performance".
elif percentage >= 70:
    print("Good performance") #Jika nilai ≥ 70 tapi < 80, maka "Good performance".
elif percentage >= 60:
    print("Average performance") #Jika nilai ≥ 60 tapi < 70, maka "Average performance".
else:
    print("Poor performance") #Jika nilai < 60, maka "Poor performance".
    
#2. mengambil input tiga angka dari user
num1 = int(input("Masukkan angka pertama: ")) #Meminta pengguna untuk memasukkan 3 angka.
num2 = int(input("Masukkan angka kedua: "))
num3 = int(input("Masukkan angka ketiga: "))

if num1 >= num2 and num1 >= num3:
    print("angka terbesar adalah", num1) #Jika num1 terbesar, maka cetak num1.
elif num2 >= num1 and num2 >= num3:
    print("angka terbesar adalah", num2) #Jika num2 terbesar, maka cetak num2.
else:
    print("angka terbesar adalah", num3) #Jika tidak, maka num3 terbesar.
    
#3. mencetak deret Fibonacci hingga nilai n yang ditentukan oleh user
def fibonacci(n): #Mendefinisikan fungsi fibonacci dengan parameter n sebagai batas deret Fibonacci.
    a, b = 0, 1 #Inisialisasi dua variabel awal Fibonacci: a = 0 dan b = 1.
    series = [] #Membuat list kosong series untuk menyimpan deret Fibonacci.
    while a <= n: #menggunakan loop while untuk terus menghitung nilai Fibonacci sampai nilai berikutnya lebih besar dari n
        series.append(a) #Menambahkan nilai a ke list series.
        a, b = b, a + b #Menghitung angka Fibonacci berikutnya dengan memperbarui a dan b.
    return series #Mengembalikan list series yang berisi deret Fibonacci.
n = int(input("Masukkan nilai n: ")) #Menerima input n, lalu memanggil fungsi fibonacci dan mencetak hasilnya.
print(fibonacci(n))

#4. meminta input nilai n dari user, kemudian mencetak bilangan ganjil hingga nilai n
n = int(input("Masukkan nilai n: ")) #Mengambil input n dari pengguna dan mengubahnya menjadi integer.
for i in range(1, n + 1, 2): #Loop dari 1 hingga n dengan langkah 2, hanya menghasilkan bilangan ganjil.
    if i % 2 != 0: #Memeriksa apakah i adalah bilangan ganjil (sisa bagi dengan 2 bukan 0).
        print(i, end=" ") #Mencetak bilangan ganjil di baris yang sama, dipisahkan dengan spasi.

#5. mencetak pola sesuai input n menggunakan loop for, di mana setiap baris diulang berdasarkan nilai dari loop    
n = int(input("Masukkan nilai n: ")) #Mengambil input n dari pengguna dan mengubahnya menjadi integer.
for i in range(1, n+1): #Loop luar berjalan dari 1 hingga n, untuk menentukan angka yang akan dicetak.
    for j in range(i): #Loop dalam berjalan sebanyak i kali, untuk mencetak angka i sebanyak i kali dalam satu baris.
        print(i, end=" ") #Mencetak angka i di baris yang sama dengan spasi sebagai pemisah.
    print() #Mencetak baris baru setelah setiap baris selesai.