/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 */
package Main;

import java.util.Arrays;
import java.util.Random;
import java.util.Scanner;

public class LeaderboardRandom {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Random rand = new Random();

        System.out.println("=============================================");
        System.out.println("   LEADERBOARD GAME: ANALISIS BUBBLE SORT");
        System.out.println("   (Input Jumlah -> Generate Skor Random)");
        System.out.println("=============================================");

        // --- 1. INPUT JUMLAH DATA ---
        System.out.print("\nMasukkan jumlah skor yang ingin digenerate: ");
        int n = scanner.nextInt();

        // Generate data random
        int[] dataAsli = new int[n];
        for (int i = 0; i < n; i++) {
            dataAsli[i] = rand.nextInt(10000) + 1; // Skor random 1 - 10000
        }

        // Copy array supaya adil
        int[] dataIteratif = Arrays.copyOf(dataAsli, n);
        int[] dataRekursif = Arrays.copyOf(dataAsli, n);

        // Tampilkan data awal (Hanya jika data sedikit)
        System.out.println("\n---------------------------------------------");
        if (n <= 20) {
            System.out.println("Data Awal: " + Arrays.toString(dataAsli));
        } else {
            System.out.println("Data Awal: [Terlalu banyak untuk ditampilkan (" + n + " data)]");
            System.out.println("           Fokus pada analisis waktu...");
        }
        System.out.println("---------------------------------------------");

        // --- 2. JALANKAN VERSI ITERATIF ---
        System.out.println("\n>> Sedang mengurutkan dengan Iteratif (Loop)...");
        long startIteratif = System.nanoTime();
        
        bubbleSortIteratif(dataIteratif);
        
        long endIteratif = System.nanoTime();
        double durasiIteratif = (endIteratif - startIteratif) / 1_000_000.0; // ke milidetik

        // --- 3. JALANKAN VERSI REKURSIF ---
        System.out.println(">> Sedang mengurutkan dengan Rekursif (Fungsi)...");
        
        // Cek Stack Overflow untuk data terlalu besar
        long startRekursif = System.nanoTime();
        try {
            bubbleSortRekursif(dataRekursif, dataRekursif.length);
        } catch (StackOverflowError e) {
            System.out.println("   [ERROR] Data terlalu banyak untuk Rekursif (Stack Overflow)!");
        }
        long endRekursif = System.nanoTime();
        double durasiRekursif = (endRekursif - startRekursif) / 1_000_000.0; // ke milidetik

        // --- 4. OUTPUT & ANALISIS ---
        System.out.println("\n================ HASIL AKHIR ================");
        
        // HASIL ITERATIF
        System.out.println("1. BUBBLE SORT ITERATIF");
        System.out.printf("   Waktu  : %.4f ms\n", durasiIteratif);
        if (n <= 20) System.out.println("   Hasil  : " + Arrays.toString(dataIteratif));

        // HASIL REKURSIF
        System.out.println("\n2. BUBBLE SORT REKURSIF");
        System.out.printf("   Waktu  : %.4f ms\n", durasiRekursif);
        if (n <= 20) System.out.println("   Hasil  : " + Arrays.toString(dataRekursif));
        
        System.out.println("=============================================");
    }
    
    // METODE 1: ITERATIF (Menggunakan Loop Biasa)
    static void bubbleSortIteratif(int[] arr) {
        int n = arr.length;
        for (int i = 0; i < n - 1; i++) {
            for (int j = 0; j < n - i - 1; j++) {
                // Descending (Besar ke Kecil)
                if (arr[j] < arr[j + 1]) {
                    int temp = arr[j];
                    arr[j] = arr[j + 1];
                    arr[j + 1] = temp;
                }
            }
        }
    }
    
    // METODE 2: REKURSIF (Tanpa Loop Luar)
    static void bubbleSortRekursif(int[] arr, int n) {
        if (n == 1) return; // Base Case

        // Satu pass (Loop Dalam)
        for (int j = 0; j < n - 1; j++) {
            if (arr[j] < arr[j + 1]) {
                int temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
            }
        }

        // Panggil diri sendiri (Loop Luar diganti Rekursi)
        bubbleSortRekursif(arr, n - 1);
    }
}
