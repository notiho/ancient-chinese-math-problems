"""
今有人當稟粟二斛。倉無粟，欲與米一、菽二，以當所稟粟。問︰各幾何？
術曰：置米一、菽二求為粟之數。并之得三、九分之八，以為法。亦置米一、菽二，而以粟二斛乘之，各自為實。實如法得一斛。
荅曰：米 a斗 。菽 b斛 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves finding the equivalent amounts of 米 (rice) and 菽 (beans) that correspond to 2 斛 (a unit of volume) of 粟 (millet). Here's the solution:


"""


from fractions import Fraction

# Given values
粟 = 2  # in 斛
米_ratio = Fraction(1, 1)  # 米 is 1 unit
菽_ratio = Fraction(2, 1)  # 菽 is 2 units

# Total ratio (米 + 菽)
total_ratio = 米_ratio + 菽_ratio  # 1 + 2 = 3

# 米 and 菽 contributions to 粟
米_contribution = 粟 * (米_ratio / total_ratio)
菽_contribution = 粟 * (菽_ratio / total_ratio)

# Assign the results to variables
a = 米_contribution  # 米 in 斗
b = 菽_contribution  # 菽 in 斛

# Results
a, b


"""


### Explanation:
1. The problem states that 米 (rice) contributes 1 part and 菽 (beans) contributes 2 parts to the total equivalent of 粟 (millet).
2. The total ratio is the sum of the 米 and 菽 parts, which is 3.
3. To find the contribution of 米 and 菽 to the total 粟, we calculate their respective proportions:
   - 米 contributes \( \frac{1}{3} \) of the total 粟.
   - 菽 contributes \( \frac{2}{3} \) of the total 粟.
4. Since 粟 is given as 2 斛, we multiply these proportions by 2 to find the actual amounts.

### Final Answer:
- \( a = \frac{2}{3} \) 斗 (米)
- \( b = \frac{4}{3} \) 斛 (菽)
"""


"""
Variable 'a' has wrong value. Expected: 36/7, Actual: 2/3
Variable 'b' has wrong value. Expected: 36/35, Actual: 4/3"""
