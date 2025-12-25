import matplotlib.pyplot as plt
import time
import random
import sys
import numpy as np 
from scipy.interpolate import make_interp_spline

# batas rekursi
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
    print("   Bubble Sort : Terbesar ke Terkecil (Worst Case)")
    print("==============================================================")
    
    try:
        num_scenarios = int(input("Masukkan jumlah skenario percobaan (misal: 5): "))
        input_sizes = []
        for i in range(num_scenarios):
            n = int(input(f"Masukkan nilai n (jumlah angka) ke-{i+1}: "))
            input_sizes.append(n)
        
        input_sizes.sort()
        
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
        # Agar grafik stabil naik kita gunakan data random
        # yang diurutkan terbalik (Descending) sebelum disorting.
        raw_random = [random.randint(1, 10000) for _ in range(n)]
        data_master = sorted(raw_random, reverse=True)
        
        # DUPLIKASI DATA
        data_iter = data_master.copy() 
        data_rec  = data_master.copy() 

        #  UKUR ITERATIF 
        start_time = time.perf_counter()
        bubble_sort_iterative(data_iter)
        end_time = time.perf_counter()
        
        time_iter = end_time - start_time 
        iterative_times.append(time_iter)

        #  UKUR REKURSIF 
        time_rec = -1.0
        try:
            start_time = time.perf_counter()
            bubble_sort_recursive(data_rec, n)
            end_time = time.perf_counter()
            
            time_rec = end_time - start_time
            recursive_times.append(time_rec)
        except RecursionError:
            time_rec = -1.0
            recursive_times.append(None)

        str_rec = "StackOverflow" if time_rec == -1.0 else f"{time_rec:.6f}"
        str_iter = f"{time_iter:.6f}"
        
        print(f"| {n:<8} | {str_rec:<25} | {str_iter:<25} |")

    print("+----------+---------------------------+---------------------------+")
    print("Processing selesai. Menampilkan grafik stabil...")

    # MEMBUAT GRAFIK
    plt.figure(figsize=(10, 6))

    x = np.array(input_sizes)
    y_iter = np.array(iterative_times)

    # Plot Iterative
    x_new = np.linspace(x.min(), x.max(), 300) 
    
    try:
        spl_iter = make_interp_spline(x, y_iter, k=2) 
        y_smooth_iter = spl_iter(x_new)
        plt.plot(x_new, y_smooth_iter, color='blue', linestyle='-', label='Iterative (Smooth)')
    except:
        plt.plot(x, y_iter, color='blue', linestyle='-', label='Iterative')

    plt.scatter(x, y_iter, color='blue')

    # Plot Recursive
    rec_valid_indices = [i for i, val in enumerate(recursive_times) if val is not None]
    
    if len(rec_valid_indices) > 1:
        x_rec = np.array([input_sizes[i] for i in rec_valid_indices])
        y_rec = np.array([recursive_times[i] for i in rec_valid_indices])
        
        x_new_rec = np.linspace(x_rec.min(), x_rec.max(), 300)
        
        try:
            spl_rec = make_interp_spline(x_rec, y_rec, k=2)
            y_smooth_rec = spl_rec(x_new_rec)
            plt.plot(x_new_rec, y_smooth_rec, color='red', linestyle='-', label='Recursive (Smooth)')
        except:
             plt.plot(x_rec, y_rec, color='red', linestyle='-', label='Recursive')

        plt.scatter(x_rec, y_rec, color='red')

    plt.title('Bubble Sort Performance: Worst Case Scenario (Reverse Sorted)')
    plt.xlabel('Input Size (n)')
    plt.ylabel('Execution Time (seconds)')
    plt.grid(True)
    plt.legend()
    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()