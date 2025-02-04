"""
今有豆八百四十九斛，凡豆九斗易麻七斗。問：得麻㡬何？
術曰：列豆八百四十九斛，以七十乘之得五萬九千四百三十斛，以九十除之即得。
答曰： a斛 奇 b升 。
"""

"""
To solve this problem, we need to calculate how much 麻 (ma) can be obtained by exchanging 849 斛 (hu) of 豆 (dou), given the exchange rate of 9 斗 (dou) for 7 斗 (ma). 

### Step-by-step solution:
1. Convert the exchange rate into a fraction: \( \frac{7}{9} \) (7 斗 of 麻 for 9 斗 of 豆).
2. Multiply the total amount of 豆 (849 斛) by the fraction \( \frac{7}{9} \) to determine the equivalent amount of 麻.
3. Convert the result into 斛 and 升 (1 斛 = 10 斗, 1 斗 = 10 升).

Here is the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Given data
total_dou = 849  # in 斛
exchange_rate = Fraction(7, 9)  # 7 斗 麻 for 9 斗 豆

# Step 1: Calculate the total 麻 in 斛
total_ma = total_dou * exchange_rate

# Step 2: Convert to 斛 and 升
a = total_ma.numerator // total_ma.denominator  # Integer part (斛)
remainder = total_ma - a  # Fractional part
b = remainder * 10  # Convert fractional part to 升

# Final result
a = a  # 斛
b = b.numerator // b.denominator  # 升
#----- content ends here -----


"""


### Explanation of the result:
- `a` represents the number of 斛 (integer part of the 麻 obtained).
- `b` represents the number of 升 (fractional part converted to 升).

This code will compute the values of `a` and `b` as required.
"""


"""
Variable 'a' has wrong value. Expected: 660333/1000, Actual: 660"""
