"""
假令有粟三千七十二石欲作方倉一圓窖一令徑與方等方於窖深二尺少於倉高三尺盛各滿中而粟適盡問方徑高深各多少
術曰三十五乘粟二十五而一為率多自乘以並多少乘之以乘一十四如二十五而一所得以減率余為實並多少以乘多倍之乘一十四如二十五而一多自乘加之為方法又並多少以乘一十四如二十五而一加多加之為廉法從開立方除之即窖深各加差即方徑高
答曰方徑各 a丈 高 b丈 深 c丈 
"""

"""
This is a complex ancient Chinese mathematical problem involving the calculation of dimensions for a square granary and a circular pit, given a specific volume of grain. Below is the translation of the problem into Python code, following the procedure ("術") step by step.


"""

#----- content starts here -----

"""
Suppose there are 3072 shi of millet, and it is desired to construct one square granary and one circular pit.
Let the diameter of the circular pit be equal to the side of the square granary.
The depth of the circular pit is 2 chi less than the height of the granary, and the height of the granary is 3 chi more than the depth of the pit.
Both are filled to capacity, and the millet is exactly used up.
Question: What are the side length (or diameter), height, and depth?

The procedure says:
1. Multiply 35 by the millet and divide by 25 to get the initial rate.
2. Multiply the rate by itself (square it), and add the product of the millet and 14, divided by 25.
3. Subtract the rate from the result to get the "real" value.
4. Multiply the millet by 14, divide by 25, and add this to the rate to get the "edge" value.
5. Take the cube root of the result to get the depth of the pit.
6. Add the differences (2 chi and 3 chi) to get the side length (or diameter) and height.

Answer: The side length (or diameter) is *a* zhang, the height is *b* zhang, and the depth is *c* zhang.
"""

from fractions import Fraction

# 粟三千七十二石
粟 = 3072

# Step 1: 三十五乘粟，二十五而一為率
率 = Fraction(35 * 粟, 25)

# Step 2: 多自乘以並，多少乘之，以乘一十四如二十五而一
多自乘 = 率 * 率
多少乘之 = Fraction(14 * 粟, 25)
所得 = 多自乘 + 多少乘之

# Step 3: 所得以減率，余為實
實 = 所得 - 率

# Step 4: 並多少以乘，多倍之，乘一十四如二十五而一
廉法 = Fraction(14 * 粟, 25) + 率

# Step 5: 開立方 (cube root of 實)
# Since Python does not have a built-in cube root function, we use **(1/3).
窖深 = 實 ** Fraction(1, 3)

# Step 6: 窖深各加差，即方徑高
方徑 = 窖深 + Fraction(2, 10)  # Adding 2 chi (2/10 zhang)
高 = 窖深 + Fraction(3, 10)  # Adding 3 chi (3/10 zhang)

# Final results
a = 方徑
b = 高
c = 窖深

# Outputs
print(f"方徑各 {a} 丈, 高 {b} 丈, 深 {c} 丈")
#----- content ends here -----


"""


### Explanation of Variables:
1. `粟`: The total volume of millet in shi.
2. `率`: The initial rate calculated from the millet.
3. `實`: The "real" value used to calculate the depth.
4. `廉法`: The "edge" value used to calculate the dimensions.
5. `窖深`: The depth of the circular pit.
6. `方徑`: The side length of the square granary (or the diameter of the circular pit).
7. `高`: The height of the square granary.

This code follows the ancient procedure step by step and uses the `Fraction` class to ensure precise calculations, as required.
"""


"""
Variable 'a' has wrong value. Expected: 8/5, Actual: 264.6514589377163
Variable 'b' has wrong value. Expected: 19/10, Actual: 264.75145893771634
Variable 'c' has wrong value. Expected: 7/5, Actual: 264.4514589377163"""
