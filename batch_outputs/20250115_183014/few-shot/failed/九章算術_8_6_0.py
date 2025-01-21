"""
今有牛五、羊二，直金十兩。牛二、羊五直金八兩。問︰牛羊各直金幾何？
術曰：如方程。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。荅曰：牛 a ，直金 b兩 ，羊 c ，直金 d兩 。
"""

"""
This problem is a system of linear equations, and the solution involves solving for the values of the variables (牛 and 羊). The ancient Chinese method described here is equivalent to solving simultaneous equations using elimination or substitution. Below is the Python implementation of the solution:


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

# Using the method of elimination to solve for 牛 and 羊
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

# Solve for 牛
a = Fraction(eliminated_金, eliminated_牛)

# Substitute 牛's value back into the first equation to solve for 羊
b = Fraction(金1 - 牛1 * a, 羊1)

# 牛 a ，直金 b兩 ，羊 c ，直金 d兩
c = a
d = b

# Output the results
a, b, c, d


"""


### Explanation of the Code:
1. The problem is modeled as two linear equations:
   - \( 5牛 + 2羊 = 10 \)
   - \( 2牛 + 5羊 = 8 \)
2. The method of elimination is used to eliminate one variable (羊) by aligning the coefficients of 羊 in both equations.
3. After eliminating 羊, the value of 牛 is solved.
4. The value of 牛 is substituted back into one of the original equations to solve for 羊.
5. The results are expressed as fractions to ensure precision.

### Final Answer:
- 牛 \( a \) (price per 牛 in 金两)
- 羊 \( b \) (price per 羊 in 金两)
"""


"""
Variable 'a' has wrong value. Expected: 1, Actual: 34/21
Variable 'b' has wrong value. Expected: 34/21, Actual: 20/21
Variable 'c' has wrong value. Expected: 1, Actual: 34/21"""
