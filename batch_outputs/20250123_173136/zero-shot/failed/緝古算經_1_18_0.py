"""
假令有股弦相乘冪七百二十六，句七、十分之七。問：股多少？
術曰：冪自乘，為實。句自乘，為方法，從。開方除之，所得又開方，即股
答曰：股 a 。
"""

"""
To solve this problem, we will translate the ancient Chinese mathematical problem into Python code. Here's the step-by-step breakdown:

1. **Given**:  
   - The product of the leg (股, "a") and the hypotenuse (弦) is the "冪" (power) = 726.  
   - The other leg (句) = \(7 + \frac{7}{10} = \frac{77}{10}\).  

2. **Method**:  
   - Square the "冪" to get the "實" (real value).  
   - Square the "句" to get the "方法" (method value).  
   - Divide the "實" by the "方法" and take the square root to find the leg (股, "a").  

Here is the Python code:


"""


from fractions import Fraction
from math import sqrt

# Given values
mian = 726  # 冪 (product of 股 and 弦)
ju = Fraction(77, 10)  # 句 (other leg)

# Step 1: Square the 冪 to get 實
shi = mian ** 2

# Step 2: Square the 句 to get 方法
fangfa = ju ** 2

# Step 3: Divide 實 by 方法 and take the square root to find 股
a = Fraction(sqrt(shi / fangfa))

# The result is stored in variable 'a'


"""


The variable `a` now contains the value of the unknown 股.
"""


"""
Variable 'a' has wrong value. Expected: 132/5, Actual: 1658691827044937/17592186044416"""
