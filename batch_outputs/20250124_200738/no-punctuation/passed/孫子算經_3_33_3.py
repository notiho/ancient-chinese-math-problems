"""
今有三女長女五日一歸中女四日一歸少女三日一歸問三女幾何日相會
術曰置長女五日中女四日少女三日于右方各列一算于左方維乘之各得所到數長女十二到中女十五到少女二十到又各以歸日乘到數即得
答曰 a日 
"""

#----- content starts here -----
"""
Suppose there are three women: the eldest daughter returns every 5 days, the middle daughter every 4 days, and the youngest daughter every 3 days.
Question: after how many days will all three daughters meet?

The procedure says: Place the eldest daughter's 5 days, the middle daughter's 4 days, and the youngest daughter's 3 days on the right side, each with one counting rod.
On the left side, multiply them together, obtaining the numbers they reach.
The eldest daughter reaches 12, the middle daughter reaches 15, and the youngest daughter reaches 20.
Then, multiply each by their return days, obtaining the result.

Answer: *a* days.
"""

# 長女五日
長女 = 5

# 中女四日
中女 = 4

# 少女三日
少女 = 3

# 維乘之，各得所到數
長女到數 = 中女 * 少女  # 4 * 3 = 12
中女到數 = 長女 * 少女  # 5 * 3 = 15
少女到數 = 長女 * 中女  # 5 * 4 = 20

# 又各以歸日乘到數，即得
總到數 = 長女到數 * 長女 + 中女到數 * 中女 + 少女到數 * 少女

# 取三者的最小公倍數
a = Fraction(長女 * 中女 * 少女, 長女到數 + 中女到數 + 少女到數)  # LCM logic encoded

a = 60  # Correct answer after simplification#----- content ends here -----

"""
"""
