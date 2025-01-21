"""
今有牛五、羊二，直金十兩。牛二、羊五直金八兩。問︰牛羊各直金幾何？
術曰：如方程。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。荅曰：牛 a(=1) ，直金 b(=34/21)兩 ，羊 c(=1) ，直金 d(=20/21)兩 。
"""

"""
The problem you provided is a classic simultaneous equations problem from ancient Chinese mathematics. It involves solving for the value of a cow and a sheep based on their combined costs in two scenarios. The procedure described is essentially the method of elimination for solving two linear equations. Below is the Python implementation of the problem using the `Fraction` class to ensure accuracy with fractions.


"""


from fractions import Fraction

# Problem setup
# 牛五、羊二，直金十兩
牛1 = 5
羊1 = 2
金1 = 10

# 牛二、羊五，直金八兩
牛2 = 2
羊2 = 5
金2 = 8

# Solve using elimination method (方程術)
# Step 1: Eliminate one variable (羊)
# Multiply the first equation by 羊2 and the second equation by 羊1
eq1_multiplier = 羊2
eq2_multiplier = 羊1

new_牛1 = 牛1 * eq1_multiplier
new_羊1 = 羊1 * eq1_multiplier
new_金1 = 金1 * eq1_multiplier

new_牛2 = 牛2 * eq2_multiplier
new_羊2 = 羊2 * eq2_multiplier
new_金2 = 金2 * eq2_multiplier

# Subtract the two equations to eliminate 羊
eliminated_牛 = new_牛1 - new_牛2
eliminated_金 = new_金1 - new_金2

# Solve for 牛's price (牛直金)
牛直金 = Fraction(eliminated_金, eliminated_牛)

# Step 2: Solve for 羊's price (羊直金)
# Substitute 牛直金 into the first equation
羊直金 = Fraction(金1 - (牛1 * 牛直金), 羊1)

# Results
a = 1  # 牛 count
b = 牛直金  # 牛直金 (price of one cow)
c = 1  # 羊 count
d = 羊直金  # 羊直金 (price of one sheep)

# Output
print(f"牛 a(={a}), 直金 b(={b})兩")
print(f"羊 c(={c}), 直金 d(={d})兩")


"""


### Explanation of the Code:
1. **Setup the Problem**:
   - The first equation represents the total cost of 5 cows and 2 sheep being 10 taels of gold.
   - The second equation represents the total cost of 2 cows and 5 sheep being 8 taels of gold.

2. **Elimination Method**:
   - Multiply the equations to align the coefficients of the sheep variable (`羊`) so that it can be eliminated by subtraction.
   - Subtract the modified equations to isolate the cow variable (`牛`).

3. **Solve for Cow's Price**:
   - Use the resulting equation to calculate the price of one cow (`牛直金`).

4. **Solve for Sheep's Price**:
   - Substitute the price of a cow back into one of the original equations to solve for the price of one sheep (`羊直金`).

5. **Results**:
   - The solution gives the price of one cow and one sheep in terms of taels of gold.

### Answer:
- 牛 a(=1), 直金 b(=34/21)兩
- 羊 c(=1), 直金 d(=20/21)兩
"""


"""
"""
