package main

import (
	"fmt"
)

func main() {
	for {
		var rows, choice int

		fmt.Println("\n==========PROGRAM SEGITIGA - WARDIANSYAH F==========")
		// Input jumlah baris dari pengguna
		fmt.Print("Masukkan jumlah baris untuk segitiga: ")
		fmt.Scan(&rows)

		// Pilihan jenis segitiga
		fmt.Println("Pilih jenis segitiga:")
		fmt.Println("1. Segitiga Siku-Siku")
		fmt.Println("2. Segitiga Terbalik")
		fmt.Println("3. Segitiga Sama Sisi")
		fmt.Println("4. Segitiga Sama Sisi Terbalik")
		fmt.Print("Masukkan pilihan (1/2/3/4): ")
		fmt.Scan(&choice)

		// Memberikan spasi antara judul dan output segitiga
		fmt.Println()

		// Membuat segitiga sesuai dengan pilihan
		switch choice {
		case 1:
			fmt.Println("Segitiga Siku-Siku:")
			for i := 1; i <= rows; i++ {
				for j := 1; j <= i; j++ {
					fmt.Print("* ")
				}
				fmt.Println()
			}
		case 2:
			fmt.Println("Segitiga Terbalik:")
			for i := rows; i >= 1; i-- {
				for j := 1; j <= i; j++ {
					fmt.Print("* ")
				}
				fmt.Println()
			}
		case 3:
			fmt.Println("Segitiga Sama Sisi:")
			for i := 1; i <= rows; i++ {
				// Mencetak spasi sebelum bintang
				for k := 1; k <= rows-i; k++ {
					fmt.Print(" ")
				}
				// Mencetak bintang untuk setiap baris
				for j := 1; j <= 2*i-1; j++ {
					fmt.Print("*")
				}
				// Pindah ke baris baru setelah setiap baris selesai
				fmt.Println()
			}
		case 4:
			fmt.Println("Segitiga Sama Sisi Terbalik:")
			for i := rows; i >= 1; i-- {
				// Mencetak spasi sebelum bintang
				for k := 1; k <= rows-i; k++ {
					fmt.Print(" ")
				}
				// Mencetak bintang untuk setiap baris
				for j := 1; j <= 2*i-1; j++ {
					fmt.Print("*")
				}
				// Pindah ke baris baru setelah setiap baris selesai
				fmt.Println()
			}
		default:
			fmt.Println("Pilihan tidak valid. Silakan pilih 1, 2, 3, atau 4.")
		}

		// Minta input untuk melanjutkan atau tidak
		var ask string
		fmt.Print("\nIngin melanjutkan? (Y/T): ")
		fmt.Scan(&ask)

		// Hentikan program jika input 'T' atau 't'
		if ask != "Y" && ask != "y" {
			fmt.Println("\n==========Program Selesai, Terimakasih!==========")
			break
		}
	}
}
