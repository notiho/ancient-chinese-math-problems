"""
假令有股弦相乘冪四千七百三十九五分之三句少於弦五十四五分之二問股多少
術曰冪自乘倍少數而一為立冪又少數再自乘半之以減立冪余為實又少數自乘倍之為方法又置少數五之二而一為廉法從開立方除之即句加差即弦弦除冪即股
答曰 a 
"""

"""
This problem involves a classic right triangle relationship where the hypotenuse (弦), the base (句), and the perpendicular (股) are related through the Pythagorean theorem. The problem provides the product of the base and hypotenuse (冪), as well as the difference between the hypotenuse and the base (少數), and asks for the perpendicular (股).

The procedure is as follows:
1. Multiply the given difference (少數) by itself, double it, and add 1 to form the "立冪" (cubing base).
2. Subtract half the square of the difference (少數) from the "立冪" to form the dividend (實).
3. Multiply the square of the difference (少數) by 2 to form the divisor (方法).
4. Divide the dividend (實) by the divisor (方法) to find the base (句).
5. Add the difference (少數) to the base (句) to find the hypotenuse (弦).
6. Divide the product (冪) by the hypotenuse (弦) to find the perpendicular (股).

Now, let's encode this procedure in Python:


"""

#----- content starts here -----

from fractions import Fraction

# 冪四千七百三十九五分之三
冪 = Fraction(4739, 5)

# 少數五十四五分之二
少數 = Fraction(54, 5)

# 冪自乘倍少數而一為立冪
立冪 = 2 * (少數 ** 2) + 1

# 又少數再自乘半之以減立冪余為實
實 = 立冪 - Fraction((少數 ** 2), 2)

# 又少數自乘倍之為方法
方法 = 2 * (少數 ** 2)

# 置少數五之二而一為廉法
廉法 = 5 * 少數 + 2

# 從開立方除之即句
句 = 實 / 方法

# 句加差即弦
弦 = 句 + 少數

# 弦除冪即股
股 = 冪 / 弦

# Answer
a = 股
print(f"股 = {a}")
#----- content ends here -----


"""


This code follows the procedure step by step and calculates the perpendicular (股) as the final result.
"""


"""
Variable 'a' has wrong value. Expected: 68, Actual: 27637848/336923"""
