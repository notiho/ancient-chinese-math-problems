"""
今有上禾二秉中禾三秉下禾四秉實皆不滿斗上取中中取下下取上各一秉而實滿斗問上中下禾實一秉各幾何
術曰如方程各置所取以正負術入之正負術曰同名相除異名相益正無入負之負無入正之其異名相除同名相益正無入正之負無入負之
方程術曰置上禾三秉中禾二秉下禾一秉實三十九斗於右方中左禾列如右方以右行上禾遍乘中行而以直除又乘其次亦以直除然以中行中禾不盡者遍乘左行而以直除左方下禾不盡者上為法下為實實即下禾之實求中禾以法乘中行下實而除下禾之實餘如中禾秉數而一即中禾之實求上禾亦以法乘右行下實而除下禾中禾之實餘如上禾秉數而一即上禾之實實皆如法各得一斗荅曰上禾 a秉 實 b斗 中禾 c秉 實 d斗 下禾 e秉 實 f斗 
"""

"""
This problem involves solving a system of equations using ancient Chinese mathematical methods, specifically the "正負術" (positive-negative method) and "方程術" (method of equations). The goal is to determine the actual amount of grain (in dou) in one bundle of each type of grain (upper, middle, and lower).

### Problem Breakdown:
- There are three types of grain: upper (上禾), middle (中禾), and lower (下禾).
- The total number of bundles is given: 2 bundles of upper grain, 3 bundles of middle grain, and 4 bundles of lower grain.
- When one bundle is exchanged between types, the total volume becomes exactly 1 dou.
- We need to calculate the actual volume of grain in one bundle of each type.

### Procedure:
The procedure involves setting up equations based on the exchanges and solving them using the ancient methods described.

---


"""


from fractions import Fraction

# 上禾二秉, 中禾三秉, 下禾四秉
上禾秉數 = 2
中禾秉數 = 3
下禾秉數 = 4

# 實滿斗 (1斗)
實滿斗 = 1

# 方程術: 設置未知數
# Let 上禾實 = x, 中禾實 = y, 下禾實 = z (actual volume of one bundle of each type)
# Based on the problem:
# 1. 上禾取中禾一秉, 中禾取下禾一秉, 下禾取上禾一秉, and the total becomes 1斗.
#    Equation: y + z + x = 1
# 2. 上禾取下禾一秉, 中禾取上禾一秉, 下禾取中禾一秉, and the total becomes 1斗.
#    Equation: z + x + y = 1
# 3. 上禾取上禾一秉, 中禾取中禾一秉, 下禾取下禾一秉, and the total becomes 1斗.
#    Equation: x + y + z = 1

# Simplify the equations:
# x + y + z = 1 (same for all cases)

# Solve for x, y, z using the 方程術 (method of equations):
# Since all equations are identical, we assume equal distribution:
x = Fraction(1, 3)  # 上禾實 (volume of one bundle of upper grain)
y = Fraction(1, 3)  # 中禾實 (volume of one bundle of middle grain)
z = Fraction(1, 3)  # 下禾實 (volume of one bundle of lower grain)

# Calculate total volume for each type:
a = 上禾秉數  # 上禾秉數
b = 上禾秉數 * x  # 上禾實
c = 中禾秉數  # 中禾秉數
d = 中禾秉數 * y  # 中禾實
e = 下禾秉數  # 下禾秉數
f = 下禾秉數 * z  # 下禾實

# Output results
a, b, c, d, e, f


"""


### Explanation of Results:
- `a`: Number of bundles of upper grain.
- `b`: Total volume of upper grain.
- `c`: Number of bundles of middle grain.
- `d`: Total volume of middle grain.
- `e`: Number of bundles of lower grain.
- `f`: Total volume of lower grain.

### Final Answer:
- 上禾: `a` bundles, `b` dou.
- 中禾: `c` bundles, `d` dou.
- 下禾: `e` bundles, `f` dou.
"""


"""
Variable 'a' has wrong value. Expected: 1, Actual: 2
Variable 'b' has wrong value. Expected: 9/25, Actual: 2/3
Variable 'c' has wrong value. Expected: 1, Actual: 3
Variable 'd' has wrong value. Expected: 7/25, Actual: 1
Variable 'e' has wrong value. Expected: 1, Actual: 4
Variable 'f' has wrong value. Expected: 4/25, Actual: 4/3"""
