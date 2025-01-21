"""
今有牛五羊二直金十兩牛二羊五直金八兩問牛羊各直金幾何
術曰如方程
方程術曰置上禾三秉中禾二秉下禾一秉實三十九斗於右方中左禾列如右方以右行上禾遍乘中行而以直除又乘其次亦以直除然以中行中禾不盡者遍乘左行而以直除左方下禾不盡者上為法下為實實即下禾之實求中禾以法乘中行下實而除下禾之實餘如中禾秉數而一即中禾之實求上禾亦以法乘右行下實而除下禾中禾之實餘如上禾秉數而一即上禾之實實皆如法各得一斗荅曰牛 a 直金 b兩 羊 c 直金 d兩 
"""

"""
This problem involves solving a system of linear equations to determine the value of a cow and a sheep in terms of gold. The ancient Chinese method described here is equivalent to solving simultaneous equations using elimination or substitution. Let's translate this into Python code step by step.

The problem can be represented as:
1. \( 5x + 2y = 10 \) (where \( x \) is the value of a cow and \( y \) is the value of a sheep in gold).
2. \( 2x + 5y = 8 \).

We will solve this using the ancient "fangcheng" (方程) method.


"""


from fractions import Fraction

# 牛五羊二直金十兩 (5 cows + 2 sheep = 10 gold)
牛1 = 5
羊1 = 2
金1 = 10

# 牛二羊五直金八兩 (2 cows + 5 sheep = 8 gold)
牛2 = 2
羊2 = 5
金2 = 8

# 方程術: Eliminate one variable (羊) by aligning coefficients and subtracting equations.
# Multiply the first equation by 羊2 (5) and the second equation by 羊1 (2).
eq1_multiplier = 羊2
eq2_multiplier = 羊1

# Adjusted equations:
adjusted_牛1 = 牛1 * eq1_multiplier
adjusted_羊1 = 羊1 * eq1_multiplier
adjusted_金1 = 金1 * eq1_multiplier

adjusted_牛2 = 牛2 * eq2_multiplier
adjusted_羊2 = 羊2 * eq2_multiplier
adjusted_金2 = 金2 * eq2_multiplier

# Subtract the second adjusted equation from the first to eliminate 羊.
牛_diff = adjusted_牛1 - adjusted_牛2
金_diff = adjusted_金1 - adjusted_金2

# Solve for 牛 (value of a cow in gold).
牛_value = Fraction(金_diff, 牛_diff)

# Substitute 牛_value back into the first equation to solve for 羊 (value of a sheep in gold).
羊_value = Fraction(金1 - 牛1 * 牛_value, 羊1)

# Results
a = 牛_value  # Value of a cow in gold
b = 1         # Unit of gold for a cow
c = 羊_value  # Value of a sheep in gold
d = 1         # Unit of gold for a sheep

print(f"牛 {a} 直金 {b}兩 羊 {c} 直金 {d}兩")


"""


### Explanation:
1. The equations are scaled to align the coefficients of one variable (in this case, sheep).
2. Subtraction eliminates one variable, allowing us to solve for the other.
3. The value of the eliminated variable is substituted back into one of the original equations to solve for the remaining variable.
4. The results are expressed as fractions to ensure precision, as was common in ancient Chinese mathematics.

### Answer:
The value of a cow is \( a \) gold, and the value of a sheep is \( c \) gold.
"""


"""
Variable 'a' has wrong value. Expected: 1, Actual: 34/21
Variable 'b' has wrong value. Expected: 34/21, Actual: 1
Variable 'c' has wrong value. Expected: 1, Actual: 20/21
Variable 'd' has wrong value. Expected: 20/21, Actual: 1"""
