"""
今有牛五、羊二，直金十兩。牛二、羊五直金八兩。問︰牛羊各直金幾何？
術曰：如方程。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。荅曰：牛 a ，直金 b兩 ，羊 c ，直金 d兩 。
"""

"""
This problem involves solving a system of linear equations to determine the price of a cow and a sheep. The ancient Chinese method described here is equivalent to solving simultaneous equations using elimination or substitution. Below is the Python implementation of the problem:


"""


from fractions import Fraction

# 牛五、羊二，直金十兩
牛1 = 5
羊1 = 2
金1 = 10

# 牛二、羊五，直金八兩
牛2 = 2
羊2 = 5
金2 = 8

# Using elimination to solve for 牛 (price of a cow) and 羊 (price of a sheep)
# Multiply the first equation by 羊2 and the second equation by 羊1 to align the coefficients of 羊
eq1_multiplier = 羊2
eq2_multiplier = 羊1

# Adjusted equations
adjusted_牛1 = 牛1 * eq1_multiplier
adjusted_羊1 = 羊1 * eq1_multiplier
adjusted_金1 = 金1 * eq1_multiplier

adjusted_牛2 = 牛2 * eq2_multiplier
adjusted_羊2 = 羊2 * eq2_multiplier
adjusted_金2 = 金2 * eq2_multiplier

# Eliminate 羊 by subtracting the second equation from the first
eliminated_牛 = adjusted_牛1 - adjusted_牛2
eliminated_金 = adjusted_金1 - adjusted_金2

# Solve for 牛 (price of a cow)
牛_price = Fraction(eliminated_金, eliminated_牛)

# Substitute 牛_price back into the first equation to solve for 羊 (price of a sheep)
羊_price = Fraction(金1 - 牛1 * 牛_price, 羊1)

# Assign results to variables
a = "牛"
b = 牛_price
c = "羊"
d = 羊_price

# Output results
print(f"{a} {b}兩, {c} {d}兩")


"""


### Explanation:
1. The problem gives two equations:
   - \( 5牛 + 2羊 = 10 \)
   - \( 2牛 + 5羊 = 8 \)
2. The elimination method is used to align the coefficients of \( 羊 \) and subtract the equations to eliminate \( 羊 \), solving for \( 牛 \).
3. Once \( 牛 \) is solved, its value is substituted back into one of the original equations to solve for \( 羊 \).
4. The results are expressed as fractions to maintain precision, as ancient Chinese mathematics often worked with exact ratios.

### Answer:
- 牛 \( b \) 兩
- 羊 \( d \) 兩
"""


"""
Variable 'a' has wrong value. Expected: 1, Actual: 牛
Variable 'c' has wrong value. Expected: 1, Actual: 羊"""
