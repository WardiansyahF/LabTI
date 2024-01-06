package main

import (
	"fmt"
)

func main() {
	var jumlahMahasiswa int
	fmt.Println("\t\tPROGRAM HITUNG RATA RATA NILAI\n")
	// Meminta pengguna memasukkan jumlah mahasiswa
	fmt.Print("Masukkan jumlah mahasiswa: ")
	fmt.Scan(&jumlahMahasiswa)	

	// Menggunakan slice untuk menyimpan nilai mahasiswa
	var nilai []int

	// Meminta pengguna memasukkan nilai untuk setiap mahasiswa
	for i := 1; i <= jumlahMahasiswa; i++ {
		var nilaiMahasiswa int
		fmt.Printf("Masukkan nilai mahasiswa ke-%d: ", i)
		fmt.Scan(&nilaiMahasiswa)
		nilai = append(nilai, nilaiMahasiswa)
	}

	// Menghitung total nilai
	total := 0
	for i := 0; i < len(nilai); i++ {
		total += nilai[i]
	}
	// for _, n := range nilai {
	// 	total += n
	// }

	// Menghitung rata-rata nilai
	avg := float64(total) / float64(jumlahMahasiswa)

	fmt.Println("\n\t\tHASIL PERHITUNGAN")
	// Menampilkan hasil
	fmt.Println("Nilai mahasiswa:")
	fmt.Println(nilai)
	fmt.Printf("Maka nilai rata-rata dari %d mahasiswa tersebut adalah %.2f\n", jumlahMahasiswa, avg)
}
