"""
今有牛五、羊二，直金十兩。牛二、羊五直金八兩。問︰牛羊各直金幾何？
術曰：如方程。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：牛一，直金 a兩 ，羊一，直金 b兩 。
"""

"""
This problem is a classic system of linear equations, where the value of a cow and a sheep is to be determined based on the given relationships. The procedure described corresponds to solving simultaneous equations using elimination. Below is the translation of the problem into Python code, following the described procedure.


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

# Step 1: Eliminate one variable (羊) by aligning coefficients
# Multiply the first equation by 羊2 and the second equation by 羊1
eq1_multiplier = 羊2
eq2_multiplier = 羊1

牛1_new = 牛1 * eq1_multiplier
羊1_new = 羊1 * eq1_multiplier
金1_new = 金1 * eq1_multiplier

牛2_new = 牛2 * eq2_multiplier
羊2_new = 羊2 * eq2_multiplier
金2_new = 金2 * eq2_multiplier

# Subtract the second equation from the first to eliminate 羊
牛_diff = 牛1_new - 牛2_new
金_diff = 金1_new - 金2_new

# Step 2: Solve for 牛 (value of one cow)
牛_value = Fraction(金_diff, 牛_diff)

# Step 3: Substitute 牛_value back into one of the original equations to solve for 羊
# Using the first equation: 牛1 * 牛_value + 羊1 * 羊_value = 金1
羊_value = Fraction(金1 - (牛1 * 牛_value), 羊1)

# Results
a = 牛_value  # Value of one cow in taels
b = 羊_value  # Value of one sheep in taels

# Output the results
a, b


"""


### Explanation of the Code:
1. **Input the equations**: The problem gives two equations based on the value of cows and sheep.
   - \( 5 \text{牛} + 2 \text{羊} = 10 \text{金} \)
   - \( 2 \text{牛} + 5 \text{羊} = 8 \text{金} \)

2. **Eliminate one variable**: By aligning the coefficients of the sheep (\(羊\)) in both equations, we can subtract one equation from the other to eliminate \(羊\) and solve for \(牛\).

3. **Solve for the remaining variable**: Once \(牛\) is determined, substitute its value back into one of the original equations to solve for \(羊\).

4. **Output the results**: The values of \(牛\) and \(羊\) are expressed as fractions to ensure precision.

### Answer:
The value of one cow is \(a\) taels, and the value of one sheep is \(b\) taels.
"""


"""
"""
