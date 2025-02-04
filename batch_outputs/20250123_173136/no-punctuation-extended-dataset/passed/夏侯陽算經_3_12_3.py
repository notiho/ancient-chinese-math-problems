"""
今有絹一匹直一貫一百文問丈尺寸各幾何
術曰置錢數以四丈除之得丈價一退得尺價再退得寸價
答曰丈 a文 尺 b文 寸 c文
"""

"""
Suppose there is one bolt of silk worth 1 guan and 100 wen.
Question: how much is the price per zhang, chi, and cun?

The procedure says: Place the total amount of money.
Divide it by 4 zhang to obtain the price per zhang.
Move back one place to obtain the price per chi.
Move back another place to obtain the price per cun.

Answer: the price per zhang is *a* wen, the price per chi is *b* wen, and the price per cun is *c* wen.
"""

# 絹一匹直一貫一百文
總錢數 = 1 * 1000 + 100  # 1貫 = 1000文

# 置錢數以四丈除之，得丈價
丈價 = Fraction(總錢數, 4)

# 退得尺價
尺價 = Fraction(丈價, 10)  # 1丈 = 10尺

# 再退得寸價
寸價 = Fraction(尺價, 10)  # 1尺 = 10寸

a = 丈價
b = 尺價
c = 寸價
"""
"""
