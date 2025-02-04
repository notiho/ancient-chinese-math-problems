"""
今有牛五、羊二，直金十兩。牛二、羊五直金八兩。問︰牛羊各直金幾何？
術曰：如方程。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：牛一，直金 a兩 ，羊一，直金 b兩 。
"""

"""
This problem involves solving a system of linear equations to determine the value of one cow and one sheep in terms of gold taels. The procedure described corresponds to solving simultaneous equations using elimination or substitution, which can be implemented step by step in Python.

The problem is as follows:
- 5 cows and 2 sheep are worth 10 taels of gold.
- 2 cows and 5 sheep are worth 8 taels of gold.
- We need to find the value of one cow (*a*) and one sheep (*b*).

Let's translate the procedure into Python code:


"""

#----- content starts here -----

from fractions import Fraction

# 牛五、羊二，直金十兩
牛1 = 5
羊1 = 2
金1 = 10

# 牛二、羊五，直金八兩
牛2 = 2
羊2 = 5
金2 = 8

# Step 1: Eliminate one variable (e.g., 牛)
# Multiply the first equation by 牛2 and the second equation by 牛1 to align 牛 coefficients
eq1_multiplier = 牛2
eq2_multiplier = 牛1

new_牛1 = 牛1 * eq1_multiplier
new_羊1 = 羊1 * eq1_multiplier
new_金1 = 金1 * eq1_multiplier

new_牛2 = 牛2 * eq2_multiplier
new_羊2 = 羊2 * eq2_multiplier
new_金2 = 金2 * eq2_multiplier

# Subtract the second equation from the first to eliminate 牛
羊_diff = new_羊1 - new_羊2
金_diff = new_金1 - new_金2

# Step 2: Solve for 羊 (b)
b = Fraction(金_diff, 羊_diff)

# Step 3: Substitute 羊 value back into one of the original equations to solve for 牛 (a)
a = Fraction(金1 - 羊1 * b, 牛1)

# Results
print(f"牛一，直金 {a} 兩")
print(f"羊一，直金 {b} 兩")
#----- content ends here -----


"""


### Explanation of the Code:
1. **Input the equations**: The coefficients of cows, sheep, and gold are input as variables.
2. **Eliminate one variable**: By multiplying the equations to align the coefficients of cows, we subtract one equation from the other to eliminate the cow variable.
3. **Solve for sheep**: The resulting equation contains only the sheep variable, which is solved using division.
4. **Substitute back**: The value of sheep is substituted into one of the original equations to solve for the value of a cow.
5. **Output the results**: The values of one cow and one sheep are printed as fractions.

### Answer:
The value of one cow is *a* taels of gold, and the value of one sheep is *b* taels of gold.
"""


"""
"""
