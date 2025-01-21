"""
今有牛五、羊二，直金十兩。牛二、羊五直金八兩。問︰牛羊各直金幾何？
術曰：如方程。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。荅曰：牛 a ，直金 b兩 ，羊 c ，直金 d兩 。
"""

"""
This is a system of linear equations problem, and the solution involves solving for the values of the variables (the price of a cow and the price of a sheep). The procedure described corresponds to solving the equations using elimination or substitution. Here's the solution encoded in Python:


"""


"""
Suppose there are 5 cows and 2 sheep, worth a total of 10 liang of gold.
And 2 cows and 5 sheep are worth 8 liang of gold.
Question: how much is each cow and each sheep worth?

The procedure says: Solve using the method of equations (方程術).

The method of equations says: Place the coefficients of the variables (禾) in rows (秉) and the totals (實) on the right side.
Perform elimination by multiplying rows and dividing by the pivot (直), reducing the system step by step.
Finally, solve for each variable by back-substitution.

Answer: A cow is worth *a* liang of gold, and a sheep is worth *b* liang of gold.
"""

from fractions import Fraction

# Coefficients of the equations
# 5牛 + 2羊 = 10
# 2牛 + 5羊 = 8
牛1, 羊1, 金1 = 5, 2, 10
牛2, 羊2, 金2 = 2, 5, 8

# Eliminate 牛 from the second equation
# Multiply the first equation by 牛2 and the second equation by 牛1
牛1, 羊1, 金1 = 牛1 * 2, 羊1 * 2, 金1 * 2
牛2, 羊2, 金2 = 牛2 * 5, 羊2 * 5, 金2 * 5

# Subtract the first equation from the second to eliminate 牛
羊 = 羊2 - 羊1
金 = 金2 - 金1

# Solve for 羊 (price of a sheep)
羊價 = Fraction(金, 羊)

# Substitute 羊價 back into the first equation to solve for 牛 (price of a cow)
金1 -= 羊1 * 羊價
牛價 = Fraction(金1, 牛1)

# Results
a = 牛價  # Price of a cow
b = 羊價  # Price of a sheep


"""


### Explanation:
1. The first equation is `5牛 + 2羊 = 10`.
2. The second equation is `2牛 + 5羊 = 8`.
3. Eliminate one variable (牛) by multiplying the equations and subtracting.
4. Solve for the remaining variable (羊).
5. Substitute back to find the value of the eliminated variable (牛).

### Final Answer:
- `a` is the price of a cow in liang of gold.
- `b` is the price of a sheep in liang of gold.
"""


"""
Variable 'a' has wrong value. Expected: 1, Actual: 34/21
Variable 'b' has wrong value. Expected: 34/21, Actual: 20/21
Missing variable in output: 'c'
Missing variable in output: 'd'"""
