"""
今有器中米，不知其數，前人取半，中人三分取一，後人四分取一，餘米一斗五升。問：米幾何？
術曰：置餘米一斗五升，以六乘之，得九斗；以二除之，得四斗五升；以四乘之，得一斛八斗；以三除之，即得。
答曰： a斗 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. Here's the solution:


"""


from fractions import Fraction

# Given the remaining rice is 1斗5升, convert it to a single unit (升)
# 1斗 = 10升, so 1斗5升 = 15升
remaining_rice = 15  # in 升

# Step 1: Multiply the remaining rice by 6
step1 = remaining_rice * 6  # in 升

# Step 2: Divide the result by 2
step2 = Fraction(step1, 2)  # in 升

# Step 3: Multiply the result by 4
step3 = step2 * 4  # in 升

# Step 4: Divide the result by 3
total_rice_in_sheng = Fraction(step3, 3)  # in 升

# Convert the total rice back to 斗 (1斗 = 10升)
a = total_rice_in_sheng / 10  # in 斗

# Final answer
a  # in 斗


"""


The variable `a` will hold the total amount of rice in 斗.
"""


"""
"""
