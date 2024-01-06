package main

import "fmt"

// Struct untuk menyimpan informasi tentang seseorang
type Person struct {
	Name string
	Age  int
}

func main() {
	// Deklarasi variabel menggunakan struct Person
	var person1 Person
	var person2 Person

	// Memasukkan data ke variabel struct
	person1.Name = "John"
	person1.Age = 25

	person2.Name = "Alice"
	person2.Age = 30

	// Menampilkan informasi tentang orang-orang
	fmt.Println("Informasi Orang 1:")
	displayPersonInfo(person1)

	fmt.Println("\nInformasi Orang 2:")
	displayPersonInfo(person2)
}

// Fungsi untuk menampilkan informasi tentang seseorang
func displayPersonInfo(p Person) {
	fmt.Printf("Nama: %s\n", p.Name)
	fmt.Printf("Usia: %d\n", p.Age)
}
