"""
今有牛五、羊二，直金十兩。牛二、羊五直金八兩。問︰牛羊各直金幾何？
術曰：如方程。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：牛一，直金 a兩 ，羊一，直金 b兩 。
"""

"""
To solve this problem, we will use the method of solving simultaneous equations, as described in the ancient "方程術" (method of equations). The problem involves two equations:

1. 5牛 + 2羊 = 10兩  
2. 2牛 + 5羊 = 8兩  

We aim to find the value of one 牛 (牛價) and one 羊 (羊價). Below is the Python implementation of the procedure:


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

# 方程術：消去法
# Step 1: Eliminate one variable (e.g., 羊)
# Multiply the first equation by 羊2 and the second equation by 羊1
eq1_multiplier = 羊2
eq2_multiplier = 羊1

new_牛1 = eq1_multiplier * 牛1
new_羊1 = eq1_multiplier * 羊1
new_金1 = eq1_multiplier * 金1

new_牛2 = eq2_multiplier * 牛2
new_羊2 = eq2_multiplier * 羊2
new_金2 = eq2_multiplier * 金2

# Subtract the second equation from the first to eliminate 羊
eliminated_牛 = new_牛1 - new_牛2
eliminated_金 = new_金1 - new_金2

# Solve for 牛價 (price of one 牛)
牛價 = Fraction(eliminated_金, eliminated_牛)

# Step 2: Solve for 羊價 (price of one 羊)
# Substitute 牛價 into the first equation
羊價 = Fraction(金1 - 牛1 * 牛價, 羊1)

# Results
a = 牛價
b = 羊價

# 牛一，直金 a兩；羊一，直金 b兩
print(f"牛一，直金 {a} 兩；羊一，直金 {b} 兩。")
#----- content ends here -----


"""


### Explanation of the Code:
1. **Input the equations:** The coefficients of 牛 and 羊, as well as the total 金 (gold), are entered as variables.
2. **Eliminate one variable:** Using the method of elimination, we multiply the equations to align the coefficients of 羊, then subtract one equation from the other to eliminate 羊 and solve for 牛價.
3. **Substitute back:** Once 牛價 is found, it is substituted back into one of the original equations to solve for 羊價.
4. **Output the results:** The values of 牛價 and 羊價 are printed as fractions for precision.

### Answer:
The values of 牛價 (a) and 羊價 (b) will be computed and displayed when the code is executed.
"""


"""
"""
