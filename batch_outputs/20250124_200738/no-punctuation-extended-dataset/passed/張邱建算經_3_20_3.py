"""
今有甲乙丙三人共出一千八百錢買車一輛欲與親知乘之為親不取還賣得錢一千五百各以本錢多少分之甲得五百八十三錢三分錢之一乙得五百錢丙得四百一十六錢三分錢之二問本出錢各幾何
術曰置甲乙丙分得之數副併為法以置車錢數乘未併者各自為實實如法得一
答曰甲出錢 a 乙出錢 b 丙出錢 c
"""

#----- content starts here -----
"""
Suppose there are three people, Jia, Yi, and Bing, who together contributed 1800 qian to buy a cart.
They wanted to use it with their relatives and acquaintances. After use, the relatives did not take the cart, and it was sold for 1500 qian.
The money was divided among them based on their contributions:
Jia received 583 and 1/3 qian, Yi received 500 qian, and Bing received 416 and 2/3 qian.
Question: how much did each contribute initially?

The procedure says: Place the amounts Jia, Yi, and Bing received as their shares.
Add these together as the divisor.
Multiply the total cart cost by the amounts not yet added together, each becoming the dividend.
Divide each dividend by the divisor to obtain the contributions.

Answer: Jia contributed *a* qian, Yi contributed *b* qian, and Bing contributed *c* qian.
"""

from fractions import Fraction

# Jia, Yi, and Bing received amounts
甲分得 = Fraction(583, 1) + Fraction(1, 3)
乙分得 = Fraction(500, 1)
丙分得 = Fraction(416, 1) + Fraction(2, 3)

# Combine their shares to form the divisor
法 = 甲分得 + 乙分得 + 丙分得

# Total cart cost
車錢 = 1800

# Calculate contributions
甲實 = 車錢 * 甲分得
乙實 = 車錢 * 乙分得
丙實 = 車錢 * 丙分得

# Divide each by the divisor to get contributions
a = Fraction(甲實, 法)
b = Fraction(乙實, 法)
c = Fraction(丙實, 法)#----- content ends here -----

"""
"""
