"""
今有三女，長女五日一歸，中女四日一歸，少女三日一歸。問：三女幾何日相會？
術曰：置長女五日，中女四日，少女三日，于右方，各列一算于左方，維乘之，各得所到數。長女十二到，中女十五到，少女二十到，又各以歸日乘到數，即得。
答曰： a日 。
"""

#----- content starts here -----
"""
Suppose there are three daughters. The eldest daughter returns home every 5 days, the middle daughter every 4 days, and the youngest daughter every 3 days.
Question: after how many days will all three daughters meet at home?

The procedure says: Place the eldest daughter's 5 days, the middle daughter's 4 days, and the youngest daughter's 3 days on the right side.
For each, place a counting rod on the left side.
Multiply them together, obtaining the respective "arrival numbers."
The eldest daughter arrives 12 times, the middle daughter 15 times, and the youngest daughter 20 times.
Then, multiply each by their respective return days, obtaining the least common multiple.

Answer: *a* days.
"""

# 長女五日一歸
長女 = 5

# 中女四日一歸
中女 = 4

# 少女三日一歸
少女 = 3

# 求三數的最小公倍數 (Least Common Multiple, LCM)
# 維乘之，各得所到數
到數_長女 = 中女 * 少女  # 4 * 3 = 12
到數_中女 = 長女 * 少女  # 5 * 3 = 15
到數_少女 = 長女 * 中女  # 5 * 4 = 20

# 又各以歸日乘到數，即得
乘積_長女 = 到數_長女 * 長女  # 12 * 5 = 60
乘積_中女 = 到數_中女 * 中女  # 15 * 4 = 60
乘積_少女 = 到數_少女 * 少女  # 20 * 3 = 60

# 最小公倍數為三個乘積的公約數
a = Fraction(乘積_長女, 到數_長女)  # 60 / 12 = 5
#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 60, Actual: 5"""
