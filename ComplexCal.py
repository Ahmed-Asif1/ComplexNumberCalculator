# ComplexCal.py
class Complex:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, other):
        return Complex(self.real + other.real, self.imaginary + other.imaginary)

    def __sub__(self, other):
        return Complex(self.real - other.real, self.imaginary - other.imaginary)

    def __mul__(self, other):
        real_part = self.real * other.real - self.imaginary * other.imaginary
        imag_part = self.real * other.imaginary + self.imaginary * other.real
        return Complex(real_part, imag_part)

    def __truediv__(self, other):
        denom = other.real ** 2 + other.imaginary ** 2
        real_part = (self.real * other.real + self.imaginary * other.imaginary) / denom
        imag_part = (self.imaginary * other.real - self.real * other.imaginary) / denom
        return Complex(real_part, imag_part)

    def __str__(self):
        return f"{self.real} + {self.imaginary}i" if self.imaginary >= 0 else f"{self.real} - {abs(self.imaginary)}i"

try:
    # Prompt user to input two complex numbers as ordered pairs
    print("Enter the first complex number as an ordered pair (real, imaginary):")
    real_part_1 = int(input("Real part: "))
    imaginary_part_1 = int(input("Imaginary part: "))
    z1 = Complex(real_part_1, imaginary_part_1)

    print("Enter the second complex number as an ordered pair (real, imaginary):")
    real_part_2 = int(input("Real part: "))
    imaginary_part_2 = int(input("Imaginary part: "))
    z2 = Complex(real_part_2, imaginary_part_2)

    # Shows the output for each arithmatic operation
    print("Sum:", z1 + z2)
    print("Difference:", z1 - z2)
    print("Product:", z1 * z2)
    print("Division:", z1 / z2)

except Exception as e:
    print(f"An error occurred: {e}")
    input("Press Enter to exit...")

print("Press Enter to exit...")
input()

#Formulas:
# (a + bi) + (c + di) = (a + c) + i(b + d)
# (a + ib) – (c + id) = (a – c) + i(b – d)
# (a + ib). (c + id) = (ac – bd) + i(ad + bc)
# (a + ib) / (c + id) = (ac+bd)/ (c^2 + d^2) + i(bc – ad) / (c^2 + d^2)