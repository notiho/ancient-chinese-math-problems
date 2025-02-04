"""
今有甲乙二人持錢不知其數甲得乙半而錢五十乙得甲太半而亦錢五十問甲乙持錢各幾何
術曰如方程損益之
方程術曰置上禾三秉中禾二秉下禾一秉實三十九斗於右方中左禾列如右方以右行上禾遍乘中行而以直除又乘其次亦以直除然以中行中禾不盡者遍乘左行而以直除左方下禾不盡者上為法下為實實即下禾之實求中禾以法乘中行下實而除下禾之實餘如中禾秉數而一即中禾之實求上禾亦以法乘右行下實而除下禾中禾之實餘如上禾秉數而一即上禾之實實皆如法各得一斗
荅曰甲持 a錢 乙持 b錢 
"""

"""
To solve this problem, we will translate the ancient Chinese "fangcheng" (simultaneous equations) method into Python code. The problem involves two unknowns, the amount of money held by person A (甲) and person B (乙). Here's the step-by-step breakdown:

### Problem:
甲 gets half of 乙's money plus 50, and 乙 gets more than half of 甲's money plus 50. We need to determine how much money each holds.

### Procedure:
The "fangcheng" method involves setting up equations and solving them systematically. Here's the Python implementation:


"""


from fractions import Fraction

# Define the equations based on the problem:
# Equation 1: 甲 = 乙 / 2 + 50
# Equation 2: 乙 = 甲 * (3/2) - 50

# Let 甲 = x and 乙 = y
# Rewrite the equations:
# x = y / 2 + 50
# y = (3/2) * x - 50

# Solve the equations using substitution:
# Substitute y from the second equation into the first:
# x = ((3/2) * x - 50) / 2 + 50

# Clear the fractions:
# 2x = (3/2) * x - 50 + 100
# 2x = (3/2) * x + 50
# Multiply through by 2 to eliminate the fraction:
# 4x = 3x + 100
# x = 100

# Substitute x = 100 into the second equation to find y:
# y = (3/2) * 100 - 50
# y = 150 - 50
# y = 100

# Final result:
a = 100  # 甲's money
b = 100  # 乙's money

print(f"甲持 {a} 錢, 乙持 {b} 錢")


"""


### Explanation:
1. The equations are derived from the problem statement:
   - 甲 gets half of 乙's money plus 50.
   - 乙 gets more than half of 甲's money plus 50.
2. Substitution is used to solve the equations step by step.
3. The solution shows that both 甲 and 乙 hold 100 units of money each.

### Answer:
甲持 100 錢, 乙持 100 錢
"""


"""
Variable 'a' has wrong value. Expected: 75/2, Actual: 100
Variable 'b' has wrong value. Expected: 25, Actual: 100"""
