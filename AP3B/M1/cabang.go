package main

import (
	"fmt"
)

func main() {
	var nilai int
	fmt.Print("Masukkan Nilai Anda : ")
	fmt.Scan(&nilai)

	// if nilai >= 90 {
	// 	fmt.Println("Anda Mendapatkan Nilai A")
	// } else if nilai < 90 && nilai >= 80 {
	// 	fmt.Println("Anda Mendapatkan Nilai B")
	// } else if nilai < 80 && nilai >= 65 {
	// 	fmt.Println("Anda Mendapatkan Nilai C")
	// } else if nilai < 65 && nilai >= 40 {
	// 	fmt.Println("Anda Mendapatkan Nilai D")
	// } else {
	// 	fmt.Println("Anda Mendapatkan Nilai E")
	// }
	switch {
	case nilai >= 90:
		fmt.Println("Anda Mendapatkan Nilai A")
	case nilai < 90 && nilai >= 80:
		fmt.Println("Anda Mendapatkan Nilai B")
	case nilai < 80 && nilai >= 65:
		fmt.Println("Anda Mendapatkan Nilai C")
	case nilai < 65 && nilai >= 40:
		fmt.Println("Anda Mendapatkan Nilai D")
	default:
		fmt.Println("Anda Mendapatkan Nilai E")
	}

}








FORMAT ACT : NAMA_NPM_ACT 1.pdf
FORMAT LA : NAMA_NPM_LA 1.pdf

WA : 081213853153 - Wardiansyah F