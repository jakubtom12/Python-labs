import os
import pickle
import timeit

def decorator(function):  
    def wrapper(n):
        myfile = 'result.pkl'

        if os.path.exists(myfile):
            with open(myfile, 'rb') as file:
                result = pickle.load(file)
                print("File exists. Reading result:")
        
        else:
            result = function(n)
            with open(myfile, 'wb') as file:
                pickle.dump(result, file)
            print("Result calculated and saved to new file:")

        return result
    return wrapper

@decorator
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(timeit.timeit("fibonacci(10)", setup="from __main__ import fibonacci", number=1))