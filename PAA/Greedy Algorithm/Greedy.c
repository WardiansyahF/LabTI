// import library stdio.h
#include <stdio.h>
// define size itu bernilai 99
#define size 99

// buat prototype untuk function sort
void sort(int[], int);

// function main()
int main() {
  // deklarasi variable
  int jenis_koin[size], i, uang, banyak_jenis_koin, hasil[size], jumlah;
  // beri nilai jumlah sama dengan 0
  jumlah =  0;

  // meminta banyak jenis koin dari user
  printf("\nBanyak Jenis Koin : ");
  scanf("%d", &banyak_jenis_koin);

  // meminta jenis koin apa saja dari user
  printf("\nMasukan Jenis Koin : \n");
  for (i = 0; i < banyak_jenis_koin; i++) {
    scanf("\n %d", &jenis_koin[i]); 
  }

  // melakukan sort terhadap jenis koin, dan jumlah nya
  sort(jenis_koin, banyak_jenis_koin); 

  // print koin yang tersedia dari besar hinga terkecil
  printf("\nKoin yang tersedia : \n");
  for (i = 0; i < banyak_jenis_koin; i++) {
    printf("%d", jenis_koin[i]); 
    printf("\n");
  }

  // meminta nilai yang ingin dipecah dari user
  printf("\nMasukan Nilai yang dipecah : ");
  scanf("%d", &uang); 
  printf("\n");

  // for loop untuk memecah uang yang diminta user
  for (i = 0; i < banyak_jenis_koin; i++) {
    // memberi nilai kepada variable hasil indeks ke-i dengan nilai bulat dari pembagian uang dan jenis koin indeks ke-i
    hasil[i] = uang / jenis_koin[i];
    // beri nilai uang dari modulo uang dengan jenis_koin indeks ke-i
    uang = uang % jenis_koin[i];
  }

  // for loop pecahan uang yang sudah code hitung
  for (i = 0; i < banyak_jenis_koin; i++) {
    printf("Keping %d", jenis_koin[i]);
    printf("-an sebanyak : %d", hasil[i]);
    jumlah = jumlah + hasil[i];
    printf("\n");
  }

  // tampilkan uang dan jumlah nya
  printf("\nSisanya adalah %d", uang);
  printf("\n");
  printf("Jumlah koin minimum adalah %d\n", jumlah);

  return 0;
}

void sort(int array[], int siz) {
  // deklarasi variable 
  int i, hold, j;

  // loop pertama untuk loop semua jenis koin
  for (i = 0; i < siz; i++) {
    // loop kedua untuk membandingkan array indeks ke-j dengan array indeks ke-j+1
    for (j = 0; j < siz - 1; j++) {
      // perbandingan jika array j lebih kecil dari array j + 1
      if (array[j] < array[j + 1]) {
        // menukarkan value dari array j+1 ke array j
        hold = array[j];
        array[j] = array[j + 1];
        array[j + 1] = hold;
      }
    }
  }  
}
