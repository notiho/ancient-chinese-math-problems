"""
今有上禾二秉中禾三秉下禾四秉實皆不滿斗上取中中取下下取上各一秉而實滿斗問上中下禾實一秉各幾何
術曰如方程各置所取以正負術入之正負術曰同名相除異名相益正無入負之負無入正之其異名相除同名相益正無入正之負無入負之
方程術曰置上禾三秉中禾二秉下禾一秉實三十九斗於右方中左禾列如右方以右行上禾遍乘中行而以直除又乘其次亦以直除然以中行中禾不盡者遍乘左行而以直除左方下禾不盡者上為法下為實實即下禾之實求中禾以法乘中行下實而除下禾之實餘如中禾秉數而一即中禾之實求上禾亦以法乘右行下實而除下禾中禾之實餘如上禾秉數而一即上禾之實實皆如法各得一斗
荅曰上禾一秉實 a斗 中禾一秉實 b斗 下禾一秉實 c斗 
"""

"""
This problem involves solving a system of linear equations based on the given relationships between the quantities of the three types of grain (upper, middle, and lower) and their contributions to a full dou. Below is the Python implementation of the procedure:


"""


from fractions import Fraction

# 上禾二秉, 中禾三秉, 下禾四秉
上禾秉數 = 2
中禾秉數 = 3
下禾秉數 = 4

# 實皆不滿斗, 上取中, 中取下, 下取上, 各一秉而實滿斗
# Let 上禾一秉實 = x, 中禾一秉實 = y, 下禾一秉實 = z
# The equations are:
# 1. x + y = 1 (上禾取中禾一秉, 中禾取下禾一秉, 合為一斗)
# 2. y + z = 1 (中禾取下禾一秉, 下禾取上禾一秉, 合為一斗)
# 3. z + x = 1 (下禾取上禾一秉, 上禾取中禾一秉, 合為一斗)

# 方程術: Solve the system of equations
# From equation 1: x + y = 1 -> y = 1 - x
# Substitute y into equation 2: (1 - x) + z = 1 -> z = x
# Substitute z into equation 3: x + x = 1 -> x = 1/2
x = Fraction(1, 2)

# Solve for y and z
y = 1 - x
z = x

# 上禾一秉實 = x, 中禾一秉實 = y, 下禾一秉實 = z
a = x
b = y
c = z

# Output the results
print(f"上禾一秉實: {a}斗")
print(f"中禾一秉實: {b}斗")
print(f"下禾一秉實: {c}斗")


"""


### Explanation:
1. The problem is modeled as a system of three linear equations:
   - \( x + y = 1 \)
   - \( y + z = 1 \)
   - \( z + x = 1 \)
   Here, \( x \), \( y \), and \( z \) represent the amount of grain in one bundle of upper, middle, and lower grain, respectively.

2. Using substitution, the equations are solved step by step:
   - From the first equation, \( y = 1 - x \).
   - Substitute \( y \) into the second equation to find \( z = x \).
   - Substitute \( z \) into the third equation to solve for \( x = \frac{1}{2} \).

3. The values of \( y \) and \( z \) are then calculated:
   - \( y = 1 - x = \frac{1}{2} \)
   - \( z = x = \frac{1}{2} \)

### Final Answer:
- 上禾一秉實 \( a = \frac{1}{2} \) 斗
- 中禾一秉實 \( b = \frac{1}{2} \) 斗
- 下禾一秉實 \( c = \frac{1}{2} \) 斗
"""


"""
Variable 'a' has wrong value. Expected: 9/25, Actual: 1/2
Variable 'b' has wrong value. Expected: 7/25, Actual: 1/2
Variable 'c' has wrong value. Expected: 4/25, Actual: 1/2"""
