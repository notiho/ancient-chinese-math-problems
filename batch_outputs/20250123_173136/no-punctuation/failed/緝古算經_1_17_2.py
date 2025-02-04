"""
假令有股弦相乘冪四千七百三十九五分之三句少於弦五十四五分之二問股多少
術曰冪自乘倍少數而一為立冪又少數再自乘半之以減立冪余為實又少數自乘倍之為方法又置少數五之二而一為廉法從開立方除之即句加差即弦弦除冪即股
答曰 a 
"""

"""
This is a complex ancient Chinese mathematical problem involving the Pythagorean theorem and cubic equations. Let's break it down and translate it into Python step by step.

### Problem Explanation:
- There is a right triangle where the product of the leg (股, denoted as `g`) and the hypotenuse (弦, denoted as `x`) equals a given area (冪, denoted as `m`).
- The other leg (句, denoted as `j`) is shorter than the hypotenuse by a given amount (少數, denoted as `s`).
- The goal is to find the length of the leg (股, `g`).

### Procedure:
1. **冪自乘倍少數而一為立冪**  
   Multiply the given area (`m`) by itself, then multiply by twice the given difference (`s`), and add 1. This gives the "立冪" (cubed base).

2. **又少數再自乘半之以減立冪余為實**  
   Square the given difference (`s`), divide it by 2, and subtract it from the cubed base. The result is the "實" (numerator for the solution).

3. **又少數自乘倍之為方法**  
   Square the given difference (`s`), multiply it by 2. This gives the "方法" (denominator for the solution).

4. **又置少數五之二而一為廉法**  
   Multiply the given difference (`s`) by 5, add 2, and add 1. This gives the "廉法" (used for further calculations).

5. **從開立方除之即句加差即弦弦除冪即股**  
   Use the cubed base to find the length of the other leg (`j`), then add the difference (`s`) to find the hypotenuse (`x`). Finally, divide the area (`m`) by the hypotenuse to find the leg (`g`).

### Python Code:

"""


from fractions import Fraction

# 冪四千七百三十九五分之三
m = Fraction(4739, 5)

# 少數五十四五分之二
s = Fraction(54, 5)

# 冪自乘倍少數而一為立冪
立冪 = m * m * (2 * s + 1)

# 又少數再自乘半之以減立冪余為實
實 = 立冪 - (s * s / 2)

# 又少數自乘倍之為方法
方法 = 2 * (s * s)

# 又置少數五之二而一為廉法
廉法 = 5 * s + 2 + 1

# 從開立方除之即句加差即弦弦除冪即股
j = 實 / 方法  # 句 (other leg)
x = j + s      # 弦 (hypotenuse)
g = m / x      # 股 (leg)

# Answer
a = g
print(f"股 (leg) = {a}")


"""


### Explanation of Variables:
- `m`: The given area (冪).
- `s`: The given difference (少數).
- `立冪`: The cubed base calculated from the area and difference.
- `實`: The numerator for the solution.
- `方法`: The denominator for the solution.
- `廉法`: An intermediate value used for further calculations.
- `j`: The other leg (句).
- `x`: The hypotenuse (弦).
- `g`: The leg (股), which is the final answer.

### Final Answer:
The value of `a` will be the length of the leg (股).
"""


"""
Variable 'a' has wrong value. Expected: 68, Actual: 27637848/2538075311"""
