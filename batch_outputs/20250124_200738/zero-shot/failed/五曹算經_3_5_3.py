"""
今有豆八百四十九斛，凡豆九斗易麻七斗。問：得麻㡬何？
術曰：列豆八百四十九斛，以七十乘之得五萬九千四百三十斛，以九十除之即得。
答曰： a斛 奇 b升 。
"""

"""
To solve this problem, we need to determine how much sesame (麻) can be obtained by trading 849斛 of beans (豆), given that 9斗 of beans can be exchanged for 7斗 of sesame. The answer is expressed in terms of 斛 (a unit of volume) and 升 (a smaller unit of volume, where 1斛 = 10斗 and 1斗 = 10升).

Here is the Python code to compute the values of `a` (in 斛) and `b` (in 升):


"""

#----- content starts here -----

from fractions import Fraction

# Given data
beans_in_hu = 849  # 849斛 of beans
beans_per_trade = 9  # 9斗 of beans per trade
sesame_per_trade = 7  # 7斗 of sesame per trade

# Convert beans to sesame
# 1斛 = 10斗
beans_in_dou = beans_in_hu * 10  # Convert beans to 斗
sesame_in_dou = Fraction(beans_in_dou * sesame_per_trade, beans_per_trade)  # Sesame in 斗

# Convert sesame to 斛 and 升
sesame_in_hu = sesame_in_dou // 10  # Whole 斛
sesame_in_sheng = (sesame_in_dou % 10) * 10  # Remaining 升

# Assign results to variables
a = sesame_in_hu
b = sesame_in_sheng

# Results
a, b
#----- content ends here -----


"""


### Explanation:
1. Convert the total beans from 斛 to 斗 by multiplying by 10 (since 1斛 = 10斗).
2. Use the exchange rate (9斗 of beans for 7斗 of sesame) to calculate the total sesame in 斗.
3. Convert the sesame from 斗 to 斛 and 升:
   - Divide the total sesame in 斗 by 10 to get the whole number of 斛.
   - Take the remainder in 斗, multiply by 10 to convert it to 升.

### Output:
The variables `a` and `b` will contain the values of sesame in 斛 and 升, respectively.
"""


"""
Variable 'a' has wrong value. Expected: 660333/1000, Actual: 660
Variable 'b' has wrong value. Expected: 3, Actual: 100/3"""
