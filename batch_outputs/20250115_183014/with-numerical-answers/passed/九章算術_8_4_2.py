"""
今有上禾六秉，損實一斗八升，當下禾一十秉。下禾十五秉，損實五升，當上禾五秉。問︰上、下禾實一秉各幾何？
術曰：如方程，置上禾六秉正，下禾一十秉負，損實一斗八升正。次置上禾五秉負，下禾一十五秉正，損實五升正。以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。荅曰：上禾 a(=1)秉 實 b(=8)升 ，下禾 c(=1)秉 實 d(=3)升 。
"""

"""
This problem involves solving a system of equations using ancient Chinese "fangcheng" (linear algebra) methods. Let's break it down and translate it into Python code.

### Problem Description:
We are given:
1. 6 bundles of upper millet lose 1 dou 8 sheng of grain, equivalent to 18 sheng, when compared to 10 bundles of lower millet.
2. 15 bundles of lower millet lose 5 sheng of grain when compared to 5 bundles of upper millet.

The goal is to find the grain content per bundle of upper millet and lower millet.

### Procedure:
The procedure involves setting up and solving a system of linear equations using the ancient "fangcheng" method. The equations are:
1. \( 6x - 10y = 18 \)
2. \( -5x + 15y = 5 \)

Where:
- \( x \) is the grain content per bundle of upper millet (in sheng),
- \( y \) is the grain content per bundle of lower millet (in sheng).

The solution involves using elimination and substitution methods to solve for \( x \) and \( y \).

---

### Python Code:


"""


from fractions import Fraction

# Coefficients and constants for the equations
# Equation 1: 6x - 10y = 18
上禾1 = 6  # Coefficient of x (upper millet)
下禾1 = -10  # Coefficient of y (lower millet)
損實1 = 18  # Constant term (in sheng)

# Equation 2: -5x + 15y = 5
上禾2 = -5  # Coefficient of x (upper millet)
下禾2 = 15  # Coefficient of y (lower millet)
損實2 = 5  # Constant term (in sheng)

# Step 1: Eliminate one variable (using the fangcheng method)
# Multiply the first equation by 5 and the second equation by 6 to align coefficients of x
上禾1_調整 = 5 * 上禾1
下禾1_調整 = 5 * 下禾1
損實1_調整 = 5 * 損實1

上禾2_調整 = 6 * 上禾2
下禾2_調整 = 6 * 下禾2
損實2_調整 = 6 * 損實2

# Add the two equations to eliminate x
下禾_合併 = 下禾1_調整 + 下禾2_調整
損實_合併 = 損實1_調整 + 損實2_調整

# Solve for y (grain content per bundle of lower millet)
下禾實 = Fraction(損實_合併, 下禾_合併)

# Step 2: Solve for x (grain content per bundle of upper millet)
# Substitute y back into one of the original equations
損實_代入 = 損實1 - (下禾1 * 下禾實)
上禾實 = Fraction(損實_代入, 上禾1)

# Results
a = 1  # Upper millet per bundle (in dou)
b = 上禾實  # Upper millet per bundle (in sheng)
c = 1  # Lower millet per bundle (in dou)
d = 下禾實  # Lower millet per bundle (in sheng)

# Output
print(f"上禾每秉實: {b}升")
print(f"下禾每秉實: {d}升")


"""


---

### Explanation of the Code:
1. **Equation Setup**: The two equations are set up based on the problem description.
2. **Elimination**: The coefficients of \( x \) are aligned by multiplying the equations by appropriate factors, and then \( x \) is eliminated by adding the equations.
3. **Solve for \( y \)**: The resulting equation is solved for \( y \) (grain content per bundle of lower millet).
4. **Substitute for \( x \)**: The value of \( y \) is substituted back into one of the original equations to solve for \( x \) (grain content per bundle of upper millet).
5. **Results**: The results are printed in terms of sheng (grain content per bundle).

---

### Answer:
- Upper millet: \( a = 1 \) dou, \( b = 8 \) sheng.
- Lower millet: \( c = 1 \) dou, \( d = 3 \) sheng.
"""


"""
"""
