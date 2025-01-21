"""
今有上禾六秉損實一斗八升當下禾一十秉下禾十五秉損實五升當上禾五秉問上下禾實一秉各幾何
術曰如方程置上禾六秉正下禾一十秉負損實一斗八升正次置上禾五秉負下禾一十五秉正損實五升正以正負術入之
方程術曰置上禾三秉中禾二秉下禾一秉實三十九斗於右方中左禾列如右方以右行上禾遍乘中行而以直除又乘其次亦以直除然以中行中禾不盡者遍乘左行而以直除左方下禾不盡者上為法下為實實即下禾之實求中禾以法乘中行下實而除下禾之實餘如中禾秉數而一即中禾之實求上禾亦以法乘右行下實而除下禾中禾之實餘如上禾秉數而一即上禾之實實皆如法各得一斗荅曰上禾 a秉 實 b升 下禾 c秉 實 d升 
"""

"""
This problem involves solving a system of equations using ancient Chinese methods, specifically the "fangcheng" (方程) or matrix-like method. The goal is to determine the yield per bundle of "upper millet" (上禾) and "lower millet" (下禾) based on the given relationships.

### Problem Breakdown:
- **First equation**: 6 bundles of upper millet (上禾) and 10 bundles of lower millet (下禾) yield a total of 1 dou and 8 sheng (18 sheng).
- **Second equation**: 5 bundles of upper millet (上禾) and 15 bundles of lower millet (下禾) yield a total of 5 sheng.

We need to solve for the yield per bundle of upper millet and lower millet.

---

### Fangcheng Procedure:
1. **Set up the equations**:
   - First equation: \( 6x + 10y = 18 \)
   - Second equation: \( 5x + 15y = 5 \)
   Here, \( x \) is the yield per bundle of upper millet, and \( y \) is the yield per bundle of lower millet.

2. **Eliminate one variable**:
   - Multiply the first equation by 5 and the second equation by 6 to align the coefficients of \( x \):
     - \( 30x + 50y = 90 \)
     - \( 30x + 90y = 30 \)

   - Subtract the first equation from the second to eliminate \( x \):
     - \( 40y = -60 \)
     - \( y = -\frac{60}{40} = -\frac{3}{2} \)

3. **Substitute \( y \) back into one of the original equations**:
   - Using the first equation: \( 6x + 10(-\frac{3}{2}) = 18 \)
     - \( 6x - 15 = 18 \)
     - \( 6x = 33 \)
     - \( x = \frac{33}{6} = \frac{11}{2} \)

4. **Interpret the results**:
   - The yield per bundle of upper millet (上禾) is \( x = \frac{11}{2} \) sheng.
   - The yield per bundle of lower millet (下禾) is \( y = -\frac{3}{2} \) sheng.

---

### Code Implementation:


"""


from fractions import Fraction

# Coefficients from the problem
上禾_1 = 6  # Coefficient of upper millet in the first equation
下禾_1 = 10  # Coefficient of lower millet in the first equation
實_1 = 18  # Total yield in the first equation (1 dou 8 sheng = 18 sheng)

上禾_2 = 5  # Coefficient of upper millet in the second equation
下禾_2 = 15  # Coefficient of lower millet in the second equation
實_2 = 5  # Total yield in the second equation (5 sheng)

# Step 1: Align coefficients of 上禾 (upper millet)
上禾_系數 = 上禾_1 * 下禾_2 - 上禾_2 * 下禾_1
下禾_系數 = 下禾_1 * 下禾_2 - 下禾_2 * 下禾_1
實_系數 = 實_1 * 下禾_2 - 實_2 * 下禾_1

# Step 2: Solve for 下禾 (lower millet)
下禾_實 = Fraction(實_系數, 下禾_系數)

# Step 3: Substitute 下禾 back to solve for 上禾 (upper millet)
實_1_代入 = 實_1 - 下禾_1 * 下禾_實
上禾_實 = Fraction(實_1_代入, 上禾_1)

# Results
a = 上禾_實  # Yield per bundle of upper millet
b = 下禾_實  # Yield per bundle of lower millet

print(f"上禾每秉實: {a} 升")
print(f"下禾每秉實: {b} 升")


"""


---

### Final Answer:
- Yield per bundle of upper millet (上禾): \( a = \frac{11}{2} \) sheng.
- Yield per bundle of lower millet (下禾): \( b = -\frac{3}{2} \) sheng.


"""


"""
Code error: Fraction(220, 0)"""
