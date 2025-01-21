"""
今有上禾三秉，中禾二秉，下禾一秉，實三十九斗；上禾二秉，中禾三秉，下禾一秉，實三十四斗；上禾一秉，中禾二秉，下禾三秉，實二十六斗。問︰上、中、下禾實一秉各幾何？
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：上禾 a秉 ， b斗 ，中禾 c秉 ， d斗 ，下禾 e秉 ， f斗 。
"""

"""
This problem involves solving a system of linear equations to determine the yield of one sheaf of upper, middle, and lower grain. The procedure described is essentially a method for solving simultaneous equations using elimination and substitution. Below is the Python implementation of the procedure:


"""


from fractions import Fraction

# 上禾三秉，中禾二秉，下禾一秉，實三十九斗
eq1 = [3, 2, 1, 39]

# 上禾二秉，中禾三秉，下禾一秉，實三十四斗
eq2 = [2, 3, 1, 34]

# 上禾一秉，中禾二秉，下禾三秉，實二十六斗
eq3 = [1, 2, 3, 26]

# Step 1: Eliminate the first variable (上禾) from eq2 and eq3 using eq1
# Multiply eq1 by 2 and subtract from eq2
multiplier_eq1_eq2 = Fraction(eq2[0], eq1[0])
eq2 = [eq2[i] - multiplier_eq1_eq2 * eq1[i] for i in range(4)]

# Multiply eq1 by 1 and subtract from eq3
multiplier_eq1_eq3 = Fraction(eq3[0], eq1[0])
eq3 = [eq3[i] - multiplier_eq1_eq3 * eq1[i] for i in range(4)]

# Step 2: Eliminate the second variable (中禾) from eq3 using eq2
# Multiply eq2 by the appropriate factor and subtract from eq3
multiplier_eq2_eq3 = Fraction(eq3[1], eq2[1])
eq3 = [eq3[i] - multiplier_eq2_eq3 * eq2[i] for i in range(4)]

# Step 3: Solve for 下禾 (the third variable)
下禾 = Fraction(eq3[3], eq3[2])

# Step 4: Solve for 中禾 (the second variable) using eq2
中禾 = Fraction(eq2[3] - eq2[2] * 下禾, eq2[1])

# Step 5: Solve for 上禾 (the first variable) using eq1
上禾 = Fraction(eq1[3] - eq1[2] * 下禾 - eq1[1] * 中禾, eq1[0])

# Convert results to sheaves and dou
a, b = divmod(上禾.numerator, 上禾.denominator)
c, d = divmod(中禾.numerator, 中禾.denominator)
e, f = divmod(下禾.numerator, 下禾.denominator)

# Output the results
print(f"上禾 {a}秉 ， {b}/{上禾.denominator}斗 ，中禾 {c}秉 ， {d}/{中禾.denominator}斗 ，下禾 {e}秉 ， {f}/{下禾.denominator}斗 。")


"""


### Explanation of the Code:
1. **Input Equations**: The three equations are represented as lists, where the first three elements are the coefficients of the variables (上禾, 中禾, 下禾), and the fourth element is the total yield in dou.
2. **Elimination**: The first variable (上禾) is eliminated from the second and third equations using the first equation. Then, the second variable (中禾) is eliminated from the third equation using the modified second equation.
3. **Back Substitution**: After elimination, the third variable (下禾) is solved directly. Then, the second variable (中禾) is solved using the modified second equation, and finally, the first variable (上禾) is solved using the original first equation.
4. **Conversion to Sheaves and Dou**: The results are converted into integer sheaves and fractional dou for the final answer.

### Final Answer:
The output will display the yield of one sheaf of upper, middle, and lower grain in terms of integer sheaves and fractional dou.
"""


"""
Variable 'a' has wrong value. Expected: 1, Actual: 9
Variable 'b' has wrong value. Expected: 37/4, Actual: 1
Variable 'c' has wrong value. Expected: 1, Actual: 4
Variable 'd' has wrong value. Expected: 17/4, Actual: 1
Variable 'e' has wrong value. Expected: 1, Actual: 2
Variable 'f' has wrong value. Expected: 11/4, Actual: 3"""
