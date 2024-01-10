package main

import (
	"encoding/json"
	"fmt"
) // import json

// Deklarasi struktur User
type User struct {
	FullName string `json:"Name"`
	Age      int
}

func main() {
	// Membuat slice User
	var object = []User{{"Wardiansyah", 20}, {"Fauzi", 20}}

	// Mengubah slice User menjadi data JSON
	var jsonData, err = json.Marshal(object)
	if err != nil {
		// Handle error jika terjadi kesalahan saat marshalling
		fmt.Println(err.Error())
		return
	}

	// Mengonversi data JSON ke string
	var jsonString = string(jsonData)

	// Menampilkan hasil string JSON ke konsol
	fmt.Println(jsonString)
}
