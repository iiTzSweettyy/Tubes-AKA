import matplotlib.pyplot as plt
import time
import random
import sys

# Perbesar batas rekursi untuk menangani N yang agak besar
sys.setrecursionlimit(100000)

def bubble_sort_iterative(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break

def bubble_sort_recursive(arr, n):
    if n == 1:
        return
    
    count = 0
    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
            count += 1
    
    if count == 0:
        return

    bubble_sort_recursive(arr, n - 1)

def main():
    print("==============================================================")
    print("   Logika Sorting Angka Terbesar ke Terkecil (SATUAN DETIK)")
    print("==============================================================")
    
    try:
        # 1. Input User
        num_scenarios = int(input("Masukkan jumlah skenario percobaan (misal: 3): "))
        input_sizes = []
        for i in range(num_scenarios):
            n = int(input(f"Masukkan nilai n (jumlah angka random) ke-{i+1}: "))
            input_sizes.append(n)
    except ValueError:
        print("Input harus berupa angka!")
        return

    iterative_times = []
    recursive_times = []
    
    print("\n\n>>> HASIL PENGUJIAN <<<")
    print("+----------+---------------------------+---------------------------+")
    print(f"| {'n':<8} | {'Recursive Time (s)':<25} | {'Iterative Time (s)':<25} |")
    print("+----------+---------------------------+---------------------------+")

    for n in input_sizes:
        data_original = [random.randint(1, 10000) for _ in range(n)]
        
        data_iter = data_original.copy()
        data_rec = data_original.copy()

        #UKUR ITERATIF
        start_time = time.perf_counter()
        bubble_sort_iterative(data_iter)
        end_time = time.perf_counter()
        
        #UKUR REKURSIF
        time_iter = (end_time - start_time)
        iterative_times.append(time_iter)

        time_rec = -1.0
        try:
            start_time = time.perf_counter()
            bubble_sort_recursive(data_rec, n)
            end_time = time.perf_counter()
            
            time_rec = (end_time - start_time)
            recursive_times.append(time_rec)
        except RecursionError:
            time_rec = -1.0
            recursive_times.append(None)
        str_rec = "StackOverflow" if time_rec == -1.0 else f"{time_rec:.6f}"
        str_iter = f"{time_iter:.6f}"
        
        print(f"| {n:<8} | {str_rec:<25} | {str_iter:<25} |")

    print("+----------+---------------------------+---------------------------+")
    print("Processing selesai. Menampilkan grafik...")

    #Membuat Grafik
    plt.figure(figsize=(10, 6))
    
    plt.plot(input_sizes, iterative_times, marker='o', linestyle='-', color='blue', label='Iterative')
    
    rec_x = [n for i, n in enumerate(input_sizes) if recursive_times[i] is not None]
    rec_y = [t for t in recursive_times if t is not None]
    
    plt.plot(rec_x, rec_y, marker='o', linestyle='-', color='red', label='Recursive')

    plt.title('Performance Comparison: Recursive vs Iterative')
    plt.xlabel('Input Size (n)')
    plt.ylabel('Execution Time (seconds)')
    plt.grid(True)
    plt.legend()
    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()