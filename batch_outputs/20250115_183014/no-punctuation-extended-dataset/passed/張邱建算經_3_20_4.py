"""
今有甲乙丙三人共出一千八百錢買車一輛欲與親知乘之為親不取還賣得錢一千五百各以本錢多少分之甲得五百八十三錢三分錢之一乙得五百錢丙得四百一十六錢三分錢之二問本出錢各幾何
術曰置甲乙丙分得之數副併為法以置車錢數乘未併者各自為實實如法得一
答曰甲出錢 a 乙出錢 b 丙出錢 c
"""

"""
Suppose three people, Jia, Yi, and Bing, together contributed 1800 qian to buy a cart. 
They wanted to share it with relatives and acquaintances, but the relatives did not take it. 
After selling the cart, they received 1500 qian. 
The money was divided based on their contributions: 
Jia received 583 1/3 qian, Yi received 500 qian, and Bing received 416 2/3 qian. 
Question: how much money did each person originally contribute?

The procedure says: Place the amounts Jia, Yi, and Bing received as their shares in a line. 
Add these together as the divisor. 
Multiply the cart's total cost by the amounts not yet added together, with each becoming its own dividend. 
Divide each dividend by the divisor to obtain the original contributions.

Answer: Jia contributed *a* qian, Yi contributed *b* qian, and Bing contributed *c* qian.
"""

from fractions import Fraction

# 甲乙丙分得之數
甲分得 = Fraction(583, 1) + Fraction(1, 3)
乙分得 = Fraction(500, 1)
丙分得 = Fraction(416, 1) + Fraction(2, 3)

# 副併為法
法 = 甲分得 + 乙分得 + 丙分得

# 置車錢數
車錢 = 1800

# 以置車錢數乘未併者，各自為實
甲實 = 車錢 * 甲分得
乙實 = 車錢 * 乙分得
丙實 = 車錢 * 丙分得

# 實如法得一
a = Fraction(甲實, 法)
b = Fraction(乙實, 法)
c = Fraction(丙實, 法)
"""
"""
