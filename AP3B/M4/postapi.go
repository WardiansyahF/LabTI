package main

import (
	"encoding/json"
	"fmt"
	"log"
	"net/http"
	"strconv"
)

// Matakuliah
type Matakuliah struct {
	Kode_mk string `json:"kode_mk"`
	Name_mk string `json:"name_mk"`
	Sks     int    `json:"sks"`
}

// PostMatakuliah
func PostMatakuliah(w http.ResponseWriter, r *http.Request) {
	// Mengatur header untuk response sebagai JSON
	w.Header().Set("Content-Type", "application/json")

	var Mk Matakuliah

	// Memeriksa jenis metode HTTP
	if r.Method == "POST" {
		// Memeriksa header Content-Type
		if r.Header.Get("Content-Type") == "application/json" {
			// Parse data JSON dari body request
			decodeJSON := json.NewDecoder(r.Body)
			if err := decodeJSON.Decode(&Mk); err != nil {
				log.Fatal(err)
			}
		} else {
			// Parse data dari form
			getSks := r.PostFormValue("sks")
			sks, _ := strconv.Atoi(getSks)
			kode_mk := r.PostFormValue("kode_mk")
			name_mk := r.PostFormValue("name_mk")
			Mk = Matakuliah{
				Kode_mk: kode_mk,
				Name_mk: name_mk,
				Sks:     sks,
			}
		}

		// Marshal struct Matakuliah ke dalam format JSON
		dataMatakuliah, _ := json.Marshal(Mk)

		// Kirim data JSON sebagai response
		w.Write(dataMatakuliah)

		// Cetak di browser
		return
	}

	// Jika bukan request POST, kirim response error
	http.Error(w, "hayo mau ngapain", http.StatusNotFound)
	return
}

func main() {
	// Mengatur route dan handler untuk endpoint /Jadwal
	http.HandleFunc("/Jadwal", PostMatakuliah)

	// Menjalankan server pada port 8014
	port := ":8014"
	fmt.Printf("Server running on http://localhost%s/Jadwal\n", port)
	if err := http.ListenAndServe(port, nil); err != nil {
		log.Fatal(err)
	}
}
