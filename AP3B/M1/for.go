package main

import (
	"fmt"
)

func main()  {
	var tinggi int

	fmt.Print("Masukkan tinggi : ")
	fmt.Scan(&tinggi)


	for i := 0; i < tinggi; i++ {
		for j := i; j < tinggi; j++{
			fmt.Print("*")
		}
		fmt.Println()
	}
}