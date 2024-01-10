package main

import (
	"encoding/json"
	"fmt"
)

// Deklarasi struct User
type User struct {
	FullName string `json:"Name"`
	Age      int
}

func main() {
	// Data JSON dalam bentuk string
	var jsonString = `{"Name": "Wardi", "Age": 20}`

	// Mengonversi string JSON menjadi slice byte
	var jsonData = []byte(jsonString)

	// Membuat variabel untuk menyimpan data hasil unmarshalling
	var data User

	// Mengonversi data JSON menjadi data struktur User
	var err = json.Unmarshal(jsonData, &data)
	if err != nil {
		// Handle error jika terjadi kesalahan saat unmarshalling
		fmt.Println(err.Error())
		return
	}

	// Menampilkan hasil data struktur
	fmt.Println("user :", data.FullName)
	fmt.Println("age  :", data.Age)
}
