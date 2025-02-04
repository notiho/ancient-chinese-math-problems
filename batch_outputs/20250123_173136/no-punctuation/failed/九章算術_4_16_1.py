"""
今有積一千五百一十八步四分步之三問為圓周幾何
開圓術曰置積步數以十二乘之以開方除之即得周
荅曰 a步 
"""

"""
Suppose there is an area of 1518 and 3/4 bu². 
Question: what is the circumference of the circle?

The procedure for circles says: Place the area (in bu²). Multiply it by 12. 
Take the square root of the result and divide it by π (approximated as 3.14159). 
This gives the circumference.

Answer: *a* bu.
"""

# 積一千五百一十八步四分步之三
積步數 = Fraction(1518) + Fraction(3, 4)

# 置積步數以十二乘之
積乘十二 = 12 * 積步數

# 開方 (square root approximation using exponentiation)
開方 = 積乘十二 ** Fraction(1, 2)

# 以開方除之即得周 (divide by π to approximate circumference)
π = 3.14159
a = 開方 / π
"""
Variable 'a' has wrong value. Expected: 135, Actual: 42.97187093159833"""
