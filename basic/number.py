from decimal import *
from fractions import Fraction

getcontext().prec = 30

width: int = 32

float_num: float = 0.12345678901234567890
decimal_num: Decimal = Decimal(10) / 3
fraction_num: Fraction = Fraction(5, 3) + Fraction(1, 2)
complex_num: complex = complex(2, 3) - complex(5, 6)

output: str = f"""
{'Type'                 :{width}}Value
{str(type(float_num))   :{width}}{float_num}
{str(type(decimal_num)) :{width}}{decimal_num}
{str(type(fraction_num)):{width}}{fraction_num}
{str(type(complex_num)) :{width}}{complex_num}
"""
print(output)
