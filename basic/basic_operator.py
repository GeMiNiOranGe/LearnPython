width: int = 8

number: int = 1
other_number: int = 50

sum: int = number.__add__(other_number)
difference: int = number.__sub__(other_number)
product: int = number.__mul__(other_number)
quotient: float = number.__truediv__(other_number)

other_sum: int = number + other_number
other_difference: int = number - other_number
other_product: int = number * other_number
other_quotient: float = number / other_number

result: str = f"""
{'Method'   :<{width}}Operator
{sum        :<{width}}{other_sum}
{difference :<{width}}{other_difference}
{product    :<{width}}{other_product}
{quotient   :<{width}}{other_quotient}
"""
print(result)
