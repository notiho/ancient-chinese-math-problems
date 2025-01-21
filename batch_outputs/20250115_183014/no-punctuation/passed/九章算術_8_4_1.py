"""
今有上禾六秉損實一斗八升當下禾一十秉下禾十五秉損實五升當上禾五秉問上下禾實一秉各幾何
術曰如方程置上禾六秉正下禾一十秉負損實一斗八升正次置上禾五秉負下禾一十五秉正損實五升正以正負術入之
方程術曰置上禾三秉中禾二秉下禾一秉實三十九斗於右方中左禾列如右方以右行上禾遍乘中行而以直除又乘其次亦以直除然以中行中禾不盡者遍乘左行而以直除左方下禾不盡者上為法下為實實即下禾之實求中禾以法乘中行下實而除下禾之實餘如中禾秉數而一即中禾之實求上禾亦以法乘右行下實而除下禾中禾之實餘如上禾秉數而一即上禾之實實皆如法各得一斗荅曰上禾 a秉 實 b升 下禾 c秉 實 d升 
"""

"""
This problem involves solving a system of equations using ancient Chinese methods, specifically the "fangcheng" (方程) procedure. The goal is to determine the yield per bundle of "upper millet" (上禾) and "lower millet" (下禾) based on the given relationships. Below is the translation of the procedure into Python code:


"""


from fractions import Fraction

# Problem setup
# 上禾六秉正，下禾一十秉負，損實一斗八升正
eq1_upper_millet = 6
eq1_lower_millet = -10
eq1_loss = Fraction(1, 1) + Fraction(8, 10)  # 1斗8升 converted to a fraction

# 上禾五秉負，下禾一十五秉正，損實五升正
eq2_upper_millet = -5
eq2_lower_millet = 15
eq2_loss = Fraction(5, 10)  # 5升 converted to a fraction

# Fangcheng procedure
# Step 1: Eliminate one variable (e.g., lower millet) using the equations
# Multiply the first equation by 15 (from eq2_lower_millet)
# Multiply the second equation by 10 (from eq1_lower_millet)
factor1 = 15
factor2 = 10

new_eq1_upper_millet = eq1_upper_millet * factor1
new_eq1_loss = eq1_loss * factor1

new_eq2_upper_millet = eq2_upper_millet * factor2
new_eq2_loss = eq2_loss * factor2

# Add the two equations to eliminate lower millet
final_upper_millet = new_eq1_upper_millet + new_eq2_upper_millet
final_loss = new_eq1_loss + new_eq2_loss

# Step 2: Solve for the yield of upper millet (per bundle)
upper_millet_yield = final_loss / final_upper_millet

# Step 3: Substitute the yield of upper millet back into one of the original equations to solve for lower millet
lower_millet_yield = (eq1_loss - eq1_upper_millet * upper_millet_yield) / eq1_lower_millet

# Convert results to dou and sheng
a = 1  # Upper millet bundles
b = upper_millet_yield * 10  # Convert to sheng (1 dou = 10 sheng)
c = 1  # Lower millet bundles
d = lower_millet_yield * 10  # Convert to sheng (1 dou = 10 sheng)

# Output the results
print(f"上禾 {a} 秉, 實 {b} 升")
print(f"下禾 {c} 秉, 實 {d} 升")


"""


### Explanation of the Code:
1. **Problem Setup**: The equations are set up based on the problem statement. The losses are converted into fractions for precise calculations.
2. **Fangcheng Procedure**: The system of equations is solved step by step:
   - The first step eliminates one variable (lower millet) by multiplying the equations by appropriate factors and adding them.
   - The second step solves for the yield of upper millet per bundle.
   - The third step substitutes the yield of upper millet back into one of the original equations to solve for the yield of lower millet per bundle.
3. **Conversion to Dou and Sheng**: The results are converted into the appropriate units (dou and sheng) for the final answer.

### Final Answer:
The results are printed in the format:
- 上禾 (upper millet): `a` bundles, `b` sheng per bundle
- 下禾 (lower millet): `c` bundles, `d` sheng per bundle
"""


"""
"""
