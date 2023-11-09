class Complex_Numbers:
    def __init__(self, real = 0, imag = 0):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return Complex_Numbers(self.real + other.real, self.imag + other.imag)
    
    def __sub__(self, other):
        return Complex_Numbers(self.real - other.real, self.imag - other.imag)
    
    def __str__(self):
        return f"{self.real}{'+' if self.imag > 0 else ''}{self.imag}i"

a = Complex_Numbers(2, 5)
b = Complex_Numbers(-1, -4)

suma = a + b
roznica = a - b

print("Suma: ", suma)
print("Roznica: ", roznica)
