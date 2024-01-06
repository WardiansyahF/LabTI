package main

import "fmt"

// Struct untuk menyimpan informasi buah
type Fruit struct {
	Name  string
	Color string
}

func main() {
	
	// Meminta pengguna untuk memasukkan jumlah buah yang ingin diinput
	var jumlahBuah int
	fmt.Print("Masukkan jumlah buah yang ingin diinput: ")
	fmt.Scan(&jumlahBuah)

	// Membuat array buah-buahan berdasarkan jumlah yang dimasukkan oleh pengguna
	fruits := make([]Fruit, jumlahBuah)

	// Mengisi informasi buah-buahan menggunakan input user
	for i := 0; i < jumlahBuah; i++ {
		fmt.Printf("Masukkan informasi untuk Buah %d:\n", i+1)
		fmt.Print("Nama buah: ")
		fmt.Scan(&fruits[i].Name)
		fmt.Print("Warna buah: ")
		fmt.Scan(&fruits[i].Color)
	}

	// Pointer untuk menunjuk ke array buah-buahan
	var ptrFruits = &fruits

	// Menampilkan informasi buah-buahan menggunakan pointer
	fmt.Println("\nInformasi Buah-buahan:")
	displayFruits(ptrFruits)
}

// Fungsi untuk menampilkan informasi buah-buahan menggunakan pointer
func displayFruits(ptrFruits *[]Fruit) {
	for i := 0; i < len(*ptrFruits); i++ {
		// Menggunakan pointer untuk mengakses elemen array
		fruit := (*ptrFruits)[i]
		// Menampilkan informasi buah
		fmt.Printf("Buah %d:\n", i+1)
		fmt.Printf("Nama: %s\n", fruit.Name)
		fmt.Printf("Warna: %s\n", fruit.Color)
		fmt.Println("----------------------")
	}
}
