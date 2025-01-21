"""
今有上禾三秉，中禾二秉，下禾一秉，實三十九斗；上禾二秉，中禾三秉，下禾一秉，實三十四斗；上禾一秉，中禾二秉，下禾三秉，實二十六斗。問︰上、中、下禾實一秉各幾何？
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：上禾 a(=1)秉 ， b(=37/4)斗 ，中禾 c(=1)秉 ， d(=17/4)斗 ，下禾 e(=1)秉 ， f(=11/4)斗 。
"""

"""
This problem involves solving a system of linear equations to determine the yield of one bundle of upper, middle, and lower grain. The ancient Chinese method described is equivalent to solving the system using elimination and substitution. Below is the Python implementation of the procedure:


"""


from fractions import Fraction

# 上禾三秉，中禾二秉，下禾一秉，實三十九斗
# 上禾二秉，中禾三秉，下禾一秉，實三十四斗
# 上禾一秉，中禾二秉，下禾三秉，實二十六斗

# Coefficients of the equations
上禾系數 = [3, 2, 1]
中禾系數 = [2, 3, 2]
下禾系數 = [1, 1, 3]
實 = [39, 34, 26]

# Step 1: Eliminate the first variable (上禾) from the second and third equations
# Multiply the first equation by 2 and subtract from the second equation
中禾系數[1] = 中禾系數[1] * 上禾系數[0] - 中禾系數[0] * 上禾系數[1]
下禾系數[1] = 下禾系數[1] * 上禾系數[0] - 下禾系數[0] * 上禾系數[1]
實[1] = 實[1] * 上禾系數[0] - 實[0] * 上禾系數[1]

# Multiply the first equation by 1 and subtract from the third equation
中禾系數[2] = 中禾系數[2] * 上禾系數[0] - 中禾系數[0] * 上禾系數[2]
下禾系數[2] = 下禾系數[2] * 上禾系數[0] - 下禾系數[0] * 上禾系數[2]
實[2] = 實[2] * 上禾系數[0] - 實[0] * 上禾系數[2]

# Step 2: Eliminate the second variable (中禾) from the third equation
# Multiply the second equation by the new 中禾系數[2] and subtract from the third equation
下禾系數[2] = 下禾系數[2] * 中禾系數[1] - 下禾系數[1] * 中禾系數[2]
實[2] = 實[2] * 中禾系數[1] - 實[1] * 中禾系數[2]

# Step 3: Solve for 下禾
下禾實 = Fraction(實[2], 下禾系數[2])

# Step 4: Solve for 中禾
中禾實 = Fraction(實[1] - 下禾系數[1] * 下禾實, 中禾系數[1])

# Step 5: Solve for 上禾
上禾實 = Fraction(實[0] - 中禾系數[0] * 中禾實 - 下禾系數[0] * 下禾實, 上禾系數[0])

# Results
a = 1  # 上禾秉數
b = 上禾實  # 上禾實
c = 1  # 中禾秉數
d = 中禾實  # 中禾實
e = 1  # 下禾秉數
f = 下禾實  # 下禾實

# Output
print(f"上禾 {a}秉 ， {b}斗 ，中禾 {c}秉 ， {d}斗 ，下禾 {e}秉 ， {f}斗 。")


"""


### Explanation of the Results:
- The procedure follows the elimination method to reduce the system of equations step by step.
- The final results are:
  - 上禾 (upper grain): 1 bundle yields `37/4` dou.
  - 中禾 (middle grain): 1 bundle yields `17/4` dou.
  - 下禾 (lower grain): 1 bundle yields `11/4` dou.
"""


"""
"""
