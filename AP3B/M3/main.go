package main

import (
	"database/sql"
	"fmt"
	"os"

	_ "github.com/go-sql-driver/mysql"
)

type tbl_mhs struct {
	npm     int
	nama    string
	kelas   string
	jurusan string
}

func connect() (*sql.DB, error) {
	db, err := sql.Open("mysql", "root:@tcp(127.0.0.1:3306)/test_mhs")
	if err != nil {
		return nil, err
	}
	return db, nil
}

func insertData(db *sql.DB) {
	var npm int
	var nama, kelas, jurusan string

	fmt.Print("Enter NPM: ")
	fmt.Scan(&npm)
	fmt.Print("Enter Name: ")
	fmt.Scan(&nama)
	fmt.Print("Enter Class: ")
	fmt.Scan(&kelas)
	fmt.Print("Enter Major: ")
	fmt.Scan(&jurusan)

	_, err := db.Exec("insert into tbl_mhs values (?,?,?,?)", npm, nama, kelas, jurusan)
	if err != nil {
		fmt.Println(err.Error())
		return
	}
	fmt.Printf("Data berhasil ditambah\n")
}

func updateData(db *sql.DB) {
	var npm int
	var nama string

	fmt.Print("Enter NPM to update: ")
	fmt.Scan(&npm)
	fmt.Print("Enter new Name: ")
	fmt.Scan(&nama)

	_, err := db.Exec("update tbl_mhs set nama= ? where npm = ?", nama, npm)
	if err != nil {
		fmt.Println(err.Error())
		return
	}
	fmt.Printf("Data berhasil diubah\n")
}

func deleteData(db *sql.DB) {
	var npm int

	fmt.Print("Enter NPM to delete: ")
	fmt.Scan(&npm)

	_, err := db.Exec("delete from tbl_mhs where npm=?", npm)
	if err != nil {
		fmt.Println(err.Error())
		return
	}
	fmt.Printf("Data berhasil dihapus\n")
}

func selectData(db *sql.DB) {
	rows, err := db.Query("select * from tbl_mhs")
	if err != nil {
		fmt.Println(err.Error())
		return
	}
	defer rows.Close()

	var result []tbl_mhs

	for rows.Next() {
		var each = tbl_mhs{}
		var err = rows.Scan(&each.npm, &each.nama, &each.kelas, &each.jurusan)

		if err != nil {
			fmt.Println(err.Error())
			return
		}

		result = append(result, each)
	}
	if err = rows.Err(); err != nil {
		fmt.Println(err.Error())
		return
	}

	for _, each := range result {
		fmt.Print(each.npm)
		fmt.Print(" | ")
		fmt.Print(each.nama)
		fmt.Print(" | ")
		fmt.Print(each.kelas)
		fmt.Print(" | ")
		fmt.Print(each.jurusan, "\n")
	}
}

func main() {
	db, err := connect()
	if err != nil {
		fmt.Println(err.Error())
		return
	}
	defer db.Close()

	var choice int

	for {
		fmt.Println("\t\t\tPROGRAM DATABASE SEDERHANA")
		fmt.Println("1. Insert Data")
		fmt.Println("2. Update Data")
		fmt.Println("3. Delete Data")
		fmt.Println("4. Select Data")
		fmt.Println("5. Exit")

		fmt.Print("Enter your choice: ")
		fmt.Scan(&choice)

		switch choice {
		case 1:
			insertData(db)
		case 2:
			updateData(db)
		case 3:
			deleteData(db)
		case 4:
			selectData(db)
		case 5:
			fmt.Println("PROGRAM SELESAI")
			os.Exit(0)
		default:
			fmt.Println("Invalid choice. Please enter a valid option.")
		}
	}
}
