package main

import "fmt"

func main() {
	// Deklarasi variabel dan pointer
	var num1, num2 int
	var sum, product int
	var ptrSum, ptrProduct *int

	// Inisialisasi pointer
	ptrSum = &sum
	ptrProduct = &product

	// Meminta pengguna untuk memasukkan dua angka
	fmt.Print("Masukkan angka pertama: ")
	fmt.Scan(&num1)
	fmt.Print("Masukkan angka kedua: ")
	fmt.Scan(&num2)

	// Menggunakan pointer untuk menghitung penjumlahan dan perkalian
	*ptrSum = num1 + num2
	*ptrProduct = num1 * num2

	// Menampilkan hasil
	fmt.Printf("\nHasil Penjumlahan: %d\n", *ptrSum)
	fmt.Printf("Hasil Perkalian: %d\n", *ptrProduct)
}
