"""
今有二馬、一牛價過一萬，如半馬之價。一馬、二牛價不滿一萬，如半牛之價。問︰牛、馬價各幾何？
術曰：如方程，損益之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。荅曰：馬價 a錢 ，牛價 b錢 。
"""

"""
This problem involves solving a system of linear equations using the ancient Chinese method of elimination, which is similar to Gaussian elimination. Let's translate the problem into Python code step by step.

### Problem Setup:
We are given:
1. The price of two horses and one cow exceeds 10,000 by the price of half a horse.
2. The price of one horse and two cows is less than 10,000 by the price of half a cow.

We need to find the price of one horse (*a*) and one cow (*b*).

### Procedure:
The procedure follows the ancient Chinese method of elimination ("方程術"), which involves systematically eliminating variables to solve for unknowns.


"""


from fractions import Fraction

# Define the equations:
# 2馬 + 1牛 = 10000 + 0.5馬
# 1馬 + 2牛 = 10000 - 0.5牛

# Convert the equations into standard linear form:
# 2.5馬 + 1牛 = 10000
# 1馬 + 2.5牛 = 10000

# Coefficients of the equations:
# Equation 1: 2.5馬 + 1牛 = 10000
eq1_horse_coeff = Fraction(5, 2)  # 2.5
eq1_cow_coeff = 1
eq1_constant = 10000

# Equation 2: 1馬 + 2.5牛 = 10000
eq2_horse_coeff = 1
eq2_cow_coeff = Fraction(5, 2)  # 2.5
eq2_constant = 10000

# Step 1: Eliminate one variable (e.g., 馬) using the elimination method.
# Multiply the first equation by 1 (eq2_horse_coeff) and the second equation by 2.5 (eq1_horse_coeff).
factor1 = eq2_horse_coeff
factor2 = eq1_horse_coeff

# New equations after scaling:
# Equation 1: (2.5 * 1)馬 + (1 * 1)牛 = 10000 * 1
# Equation 2: (1 * 2.5)馬 + (2.5 * 2.5)牛 = 10000 * 2.5

new_eq1_cow_coeff = eq1_cow_coeff * factor1
new_eq1_constant = eq1_constant * factor1

new_eq2_cow_coeff = eq2_cow_coeff * factor2
new_eq2_constant = eq2_constant * factor2

# Subtract the first equation from the second to eliminate 馬:
# (2.5 * 2.5 - 2.5 * 1)牛 = (10000 * 2.5 - 10000 * 1)
eliminated_cow_coeff = new_eq2_cow_coeff - new_eq1_cow_coeff
eliminated_constant = new_eq2_constant - new_eq1_constant

# Solve for 牛 (cow price):
牛價 = Fraction(eliminated_constant, eliminated_cow_coeff)

# Step 2: Substitute 牛價 back into one of the original equations to solve for 馬 (horse price).
# Using the first equation: 2.5馬 + 1牛 = 10000
馬價 = Fraction(eq1_constant - (eq1_cow_coeff * 牛價), eq1_horse_coeff)

# Final answers:
a = 馬價
b = 牛價

print(f"馬價: {a}錢, 牛價: {b}錢")


"""


### Explanation:
1. The equations are converted into standard linear form.
2. The elimination method is used to remove one variable (in this case, 馬).
3. The remaining variable (牛) is solved for.
4. The value of 牛 is substituted back into one of the original equations to solve for 馬.
5. The final prices of the horse (*a*) and cow (*b*) are printed as fractions for exactness.

### Output:
The program will output the exact prices of the horse and cow in terms of "錢".
"""


"""
Variable 'a' has wrong value. Expected: 60000/11, Actual: 20000/7
Variable 'b' has wrong value. Expected: 20000/11, Actual: 20000/7"""
