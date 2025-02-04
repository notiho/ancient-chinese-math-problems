"""
今有甲乙丙三人共出一千八百錢買車一輛欲與親知乘之為親不取還賣得錢一千五百各以本錢多少分之甲得五百八十三錢三分錢之一乙得五百錢丙得四百一十六錢三分錢之二問本出錢各幾何
術曰置甲乙丙分得之數副併為法以置車錢數乘未併者各自為實實如法得一
答曰甲出錢 a 乙出錢 b 丙出錢 c
"""

#----- content starts here -----
"""
Suppose there are three people, Jia, Yi, and Bing, who together contributed 1800 qian to buy a cart. 
They intended to use it with their acquaintances, but the acquaintances did not contribute. 
Later, they sold the cart for 1500 qian and divided the money according to their contributions:
Jia received 583 1/3 qian, Yi received 500 qian, and Bing received 416 2/3 qian.
Question: how much did each contribute initially?

The procedure says: Place the amounts Jia, Yi, and Bing received as their shares in a line.
Add these together to form the divisor.
Multiply the total cart cost by the amounts not yet added together, each becoming its own dividend.
Divide each dividend by the divisor to obtain the contributions.

Answer: Jia contributed *a* qian, Yi contributed *b* qian, and Bing contributed *c* qian.
"""

from fractions import Fraction

# Jia, Yi, and Bing's shares
甲分得 = Fraction(1750, 3)  # 583 1/3 qian
乙分得 = 500  # 500 qian
丙分得 = Fraction(1250, 3)  # 416 2/3 qian

# Combine their shares to form the divisor (法)
法 = 甲分得 + 乙分得 + 丙分得

# Total cart cost
車錢 = 1800

# Multiply the total cart cost by the individual shares to form the dividends (實)
甲實 = 車錢 * 甲分得
乙實 = 車錢 * 乙分得
丙實 = 車錢 * 丙分得

# Divide each dividend by the divisor to obtain the contributions
a = Fraction(甲實, 法)
b = Fraction(乙實, 法)
c = Fraction(丙實, 法)#----- content ends here -----

"""
"""
