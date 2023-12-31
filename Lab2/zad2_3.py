import random
import time
import matplotlib.pyplot as plt
from zad2_2 import parallel_sort

def generate_random_data(length): #funkcja do tworzenia danych losowych
    return [random.randint(0, 10**6) for _ in range(length)]

data_sizes = [10**2, 10**3, 10**4, 10**5] #Test funkcji
process_counts = [1, 2, 3, 4]

results = {}

if __name__ == '__main__':
    for size in data_sizes:
        data = generate_random_data(size)
        for processes in process_counts:
            start_time = time.time()
            parallel_sort(data, processes)
            end_time = time.time()
            elapsed_time = end_time - start_time
            results[(size, processes)] = elapsed_time

    #Pokazanie rezultatu 
    fig, ax = plt.subplots()

    for processes in process_counts:
        times = [results[(size, processes)] for size in data_sizes]
        ax.plot(data_sizes, times, label=f'{processes} processes')

    ax.set_xlabel('Data size')
    ax.set_ylabel('Time (seconds)')
    ax.legend()
    ax.grid(True)

    plt.show()
