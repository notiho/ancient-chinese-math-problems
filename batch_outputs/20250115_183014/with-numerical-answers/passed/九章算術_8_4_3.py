"""
今有上禾六秉，損實一斗八升，當下禾一十秉。下禾十五秉，損實五升，當上禾五秉。問︰上、下禾實一秉各幾何？
術曰：如方程，置上禾六秉正，下禾一十秉負，損實一斗八升正。次置上禾五秉負，下禾一十五秉正，損實五升正。以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。荅曰：上禾 a(=1)秉 實 b(=8)升 ，下禾 c(=1)秉 實 d(=3)升 。
"""

"""
This problem involves solving a system of equations using ancient Chinese mathematical methods, specifically the "fangcheng" (方程) method, which is equivalent to solving linear equations. Here's the step-by-step breakdown and Python implementation:

### Problem Description:
We are given:
1. 6 bundles of upper millet lose 1 dou 8 sheng of grain, which corresponds to 10 bundles of lower millet.
2. 15 bundles of lower millet lose 5 sheng of grain, which corresponds to 5 bundles of upper millet.

We are tasked to find the grain loss per bundle for both upper millet and lower millet.

### Procedure:
The procedure involves setting up a system of linear equations:
1. Place the coefficients for upper millet (上禾), lower millet (下禾), and the total grain loss (損實) into equations.
2. Solve the system using the "fangcheng" method, which involves elimination and substitution.

### Implementation in Python:


"""


from fractions import Fraction

# 上禾六秉正，下禾一十秉負，損實一斗八升正
# Convert 1 dou 8 sheng to sheng (1 dou = 10 sheng)
eq1_upper = 6
eq1_lower = -10
eq1_loss = 10 + 8  # 1 dou 8 sheng = 18 sheng

# 上禾五秉負，下禾一十五秉正，損實五升正
eq2_upper = -5
eq2_lower = 15
eq2_loss = 5  # 5 sheng

# Solve using the fangcheng method
# Step 1: Eliminate one variable (e.g., upper millet)
# Multiply eq1 by 5 and eq2 by 6 to align the coefficients of upper millet
eq1_upper_scaled = eq1_upper * 5
eq1_lower_scaled = eq1_lower * 5
eq1_loss_scaled = eq1_loss * 5

eq2_upper_scaled = eq2_upper * 6
eq2_lower_scaled = eq2_lower * 6
eq2_loss_scaled = eq2_loss * 6

# Add the two equations to eliminate upper millet
combined_lower = eq1_lower_scaled + eq2_lower_scaled
combined_loss = eq1_loss_scaled + eq2_loss_scaled

# Step 2: Solve for lower millet (下禾)
lower_millet_loss_per_bundle = Fraction(combined_loss, combined_lower)

# Step 3: Solve for upper millet (上禾)
# Substitute lower millet's value back into one of the original equations
upper_millet_loss_per_bundle = Fraction(
    eq1_loss - (eq1_lower * lower_millet_loss_per_bundle), eq1_upper
)

# Convert results to dou and sheng
# 1 dou = 10 sheng
a = 1  # Upper millet per bundle
b = upper_millet_loss_per_bundle  # In sheng
c = 1  # Lower millet per bundle
d = lower_millet_loss_per_bundle  # In sheng

# Print results
print(f"上禾每秉實: {b} 升")  # 8 升
print(f"下禾每秉實: {d} 升")  # 3 升


"""


### Explanation of Results:
- **Upper millet (上禾)**: Each bundle loses `8 sheng` of grain.
- **Lower millet (下禾)**: Each bundle loses `3 sheng` of grain.

### Final Answer:
- 上禾 a(=1)秉 實 b(=8)升
- 下禾 c(=1)秉 實 d(=3)升
"""


"""
"""
