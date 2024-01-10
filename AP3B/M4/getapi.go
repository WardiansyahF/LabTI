package main

import (
	"encoding/json"
	"fmt"
	"log"
	"net/http"
)

// Jadwal
type Jadwal struct {
	Kode_mk     int    `json:"kode"`
	Nama_matkul string `json:"matkul"`
	Sks         int    `json:"sks"`
}

// NewJadwal
func NewJadwal() []Jadwal {
	// Inisialisasi slice Jadwal dengan data jadwal matakuliah
	mhs := []Jadwal{
		Jadwal{
			Kode_mk:     45217,
			Nama_matkul: "Matematika Lanjut 1",
			Sks:         2,
		},
		Jadwal{
			Kode_mk:     8954263,
			Nama_matkul: "Struktur Data",
			Sks:         2,
		},
		Jadwal{
			Kode_mk:     45215,
			Nama_matkul: "Matematika Informatika 3",
			Sks:         2,
		},
		Jadwal{
			Kode_mk:     8412345,
			Nama_matkul: "Informatika Kesehatan",
			Sks:         2,
		},
		Jadwal{
			Kode_mk:     8532217,
			Nama_matkul: "Pengenalan Teknologi dan New Media",
			Sks:         2,
		},
	}
	return mhs
}

// GetJadwal
func GetJadwal(w http.ResponseWriter, r *http.Request) {
	// Handler untuk mengambil data jadwal matakuliah saat request GET
	if r.Method == "GET" {
		// Panggil fungsi NewJadwal untuk mendapatkan data jadwal
		mhs := NewJadwal()

		// Marshal data jadwal ke dalam format JSON
		datajadwal, err := json.Marshal(mhs)
		if err != nil {
			// Jika terjadi error, kirim response error internal server error
			http.Error(w, err.Error(), http.StatusInternalServerError)
			return
		}

		// Set header dan kirim response dengan data JSON
		w.Header().Set("Content-Type", "application/json")
		w.WriteHeader(http.StatusOK)
		w.Write(datajadwal)
		return
	}

	// Jika bukan request GET, kirim response Access Denied
	http.Error(w, "Access Denied", http.StatusNotFound)
}

func main() {
	// Menetapkan handler untuk endpoint "/Jadwal"
	http.HandleFunc("/Jadwal", GetJadwal)

	// Menjalankan server pada port 8014
	port := ":8014"
	fmt.Printf("Server running on http://localhost%s/Jadwal\n", port)
	if err := http.ListenAndServe(port, nil); err != nil {
		log.Fatal(err)
	}
}
