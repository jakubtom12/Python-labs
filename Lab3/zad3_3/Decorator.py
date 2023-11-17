import os
import pickle
import timeit

def decorator(function):
    
    def wrapper(n):
        fibonacci_file = f'fibonacci_{n}.pkl'

        if os.path.exists(fibonacci_file):
            with open(fibonacci_file, 'rb') as file:
                result = pickle.load(file)
            print("existing")
        
        else:
            result = function(n)
            with open(fibonacci_file, 'wb') as file:
                pickle.dump(result, file)
            print("new")

        return result

    return wrapper

@decorator
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(timeit.timeit("fibonacci(10)", setup="from __main__ import fibonacci", number=1))