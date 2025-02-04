"""
今有馬六千二百四十三匹，匹給粟五升三合。問：計㡬何？
術曰：列馬六千二百四十三匹，以五升三合乘之即得。
答曰： a斛 。
"""

"""
To solve this problem, we need to calculate the total amount of grain (in "斛") required for 6,243 horses, where each horse is given 5升 (sheng) and 3合 (he). 

### Conversion:
1 斛 = 10 升  
1 升 = 10 合  

Thus, 5升3合 = \( 5 + \frac{3}{10} \) 升 = \( \frac{50}{10} + \frac{3}{10} = \frac{53}{10} \) 升.  
Now, convert 升 to 斛:  
\( \frac{53}{10} \) 升 = \( \frac{53}{10 \times 10} = \frac{53}{100} \) 斛.

### Total Calculation:
Multiply the total number of horses (6,243) by the grain required per horse (\( \frac{53}{100} \) 斛).

Here's the Python code:


"""


from fractions import Fraction

# Given values
horses = 6243
grain_per_horse = Fraction(53, 100)  # 53/100 斛

# Total grain required
a = horses * grain_per_horse

# Result
a  # Total grain in 斛


"""


The variable `a` will hold the total amount of grain in 斛.
"""


"""
Variable 'a' has wrong value. Expected: 330879/1000, Actual: 330879/100"""
