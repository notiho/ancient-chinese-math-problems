"""
今有上禾二秉，中禾三秉，下禾四秉，實皆不滿斗。上取中，中取下，下取上各一秉而實滿斗。問︰上、中、下禾實一秉各幾何？
術曰：如方程，各置所取，以正負術入之。正負術曰：同名相除，異名相益，正無入負之，負無入正之。其異名相除，同名相益，正無入正之，負無入負之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。荅曰：上禾 a秉 實 b斗 ，中禾 c秉 實 d斗 ，下禾 e秉 實 f斗 。
"""

"""
This problem involves solving a system of equations using ancient Chinese mathematical methods, specifically the "正負術" (positive and negative method) and "方程術" (method of simultaneous equations). Below is the Python implementation of the problem:


"""


from fractions import Fraction

# 上禾、 中禾、 下禾秉數
上禾秉數 = 2
中禾秉數 = 3
下禾秉數 = 4

# 方程術：設置方程
# Let 上禾實 = x, 中禾實 = y, 下禾實 = z
# Equations:
# 1. x + y = 1 (上取中，實滿斗)
# 2. y + z = 1 (中取下，實滿斗)
# 3. z + x = 1 (下取上，實滿斗)

# Solve the system of equations
# From equation 1: x = 1 - y
# Substitute x into equation 3: z + (1 - y) = 1 => z - y = 0 => z = y
# Substitute z = y into equation 2: y + y = 1 => 2y = 1 => y = 1/2
y = Fraction(1, 2)
z = y  # z = y
x = 1 - y  # x = 1 - y

# 計算每秉的實
上禾實 = x
中禾實 = y
下禾實 = z

# 計算每禾的總實
上禾總實 = 上禾秉數 * 上禾實
中禾總實 = 中禾秉數 * 中禾實
下禾總實 = 下禾秉數 * 下禾實

# 答案
a = 上禾秉數
b = 上禾總實
c = 中禾秉數
d = 中禾總實
e = 下禾秉數
f = 下禾總實

print(f"上禾 {a}秉 實 {b}斗")
print(f"中禾 {c}秉 實 {d}斗")
print(f"下禾 {e}秉 實 {f}斗")


"""


### Explanation:
1. **Equations Setup**:
   - The problem gives three relationships between the amounts of grain in the bundles:
     - \( x + y = 1 \) (上禾取中禾，實滿斗)
     - \( y + z = 1 \) (中禾取下禾，實滿斗)
     - \( z + x = 1 \) (下禾取上禾，實滿斗)

2. **Solve the System**:
   - Using substitution, we solve for \( x \), \( y \), and \( z \) step by step.

3. **Calculate Totals**:
   - Multiply the amount per bundle (\( x, y, z \)) by the number of bundles (\( 2, 3, 4 \)) to get the total amount of grain for each type of grain.

4. **Output**:
   - The results are printed as the total number of bundles and the total amount of grain for each type.

### Final Answer:
- 上禾 \( 2 \) 秉，實 \( 1 \) 斗
- 中禾 \( 3 \) 秉，實 \( 1.5 \) 斗
- 下禾 \( 4 \) 秉，實 \( 2 \) 斗
"""


"""
Variable 'a' has wrong value. Expected: 1, Actual: 2
Variable 'b' has wrong value. Expected: 9/25, Actual: 1
Variable 'c' has wrong value. Expected: 1, Actual: 3
Variable 'd' has wrong value. Expected: 7/25, Actual: 3/2
Variable 'e' has wrong value. Expected: 1, Actual: 4
Variable 'f' has wrong value. Expected: 4/25, Actual: 2"""
