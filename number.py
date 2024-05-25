from decimal import *
from fractions import Fraction

getcontext().prec = 30

width: int = 32

float_num: float = 0.12345678901234567890
decimal_num: Decimal = Decimal(10) / 3
fraction_num: Fraction = Fraction(5, 3) + Fraction(1, 2)
complex_num: complex = complex(2, 3) - complex(5, 6)

print(f"{'Type':{width}}Value")
print(f"{str(type(float_num)):{width}}{float_num}")
print(f"{str(type(decimal_num)):{width}}{decimal_num}")
print(f"{str(type(fraction_num)):{width}}{fraction_num}")
print(f"{str(type(complex_num)):{width}}{complex_num}")
