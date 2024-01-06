package main

import "fmt"

func main() {
	nama := "Wardiansyah F"
	var umur int = 20

	var (
		kelas    string = "3IA01"
		jurusan  string = "Informatika"
		fakultas string = "Teknologi Industri"
	)

	fmt.Println("Nama saya : ", nama)
	fmt.Printf("Umur saya : %d\n", umur)
	fmt.Println("Kelas saya : ", kelas)
	fmt.Printf("Jurusan saya : %s\n", jurusan)
	fmt.Println("Fakultas saya : ", fakultas)

	fmt.Println()
	fmt.Println("Perulangan")
	for i := 0; i < 10; i++ {
		fmt.Print(" ", i)
	}
}
