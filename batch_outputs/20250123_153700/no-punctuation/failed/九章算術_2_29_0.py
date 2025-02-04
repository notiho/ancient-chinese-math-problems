"""
今有麥八斗六升七分升之三欲為小䵂問得幾何
術曰以麥求小䵂三之十而一
荅曰為小䵂 a斗 
"""

"""
Suppose there is 8 dou, 6 sheng, and 7/10 of a sheng of wheat. It is desired to turn it into xiaoqu (small malted grain).
Question: how much does one obtain?

The procedure says: when seeking xiaoqu from wheat, multiply by 3 and divide by 10.

The answer says: it makes *a* dou of xiaoqu.
"""

# 麥八斗六升七分升之三
麥斗 = 8
麥升 = 6
麥分升 = Fraction(7, 10)

# Convert all to 升 (1 斗 = 10 升)
麥 = (麥斗 * 10) + 麥升 + 麥分升

# 以麥求小䵂，三之
小䵂 = 3 * 麥

# 十而一
小䵂 = Fraction(小䵂, 10)

# Convert back to 斗 (1 斗 = 10 升)
a斗 = 小䵂 // 10  # Whole dou
a升 = 小䵂 % 10   # Remaining sheng

a = f"{a斗}斗 {a升}升"
"""
Variable 'a' has wrong value. Expected: 363/140, Actual: 2斗 601/100升"""
