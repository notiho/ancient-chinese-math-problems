"""
今有三女長女五日一歸中女四日一歸少女三日一歸問三女幾何日相會
術曰置長女五日中女四日少女三日于右方各列一算于左方維乘之各得所到數長女十二到中女十五到少女二十到又各以歸日乘到數即得
答曰 a日 
"""

#----- content starts here -----
"""
Suppose there are three women: the eldest returns every 5 days, the middle one every 4 days, and the youngest every 3 days.
Question: after how many days will all three meet?

The procedure says: Place the eldest's 5 days, the middle's 4 days, and the youngest's 3 days on the right side, each with one counting rod.
On the left side, multiply them together, obtaining the respective arrival numbers.
The eldest arrives 12 times, the middle 15 times, and the youngest 20 times.
Then, multiply each by their respective return days, obtaining the least common multiple.

Answer: *a* days.
"""

# 長女五日
長女 = 5

# 中女四日
中女 = 4

# 少女三日
少女 = 3

# 維乘之各得所到數
長女到數 = 中女 * 少女  # 4 * 3 = 12
中女到數 = 長女 * 少女  # 5 * 3 = 15
少女到數 = 長女 * 中女  # 5 * 4 = 20

# 又各以歸日乘到數即得
長女歸 = 長女到數 * 長女  # 12 * 5 = 60
中女歸 = 中女到數 * 中女  # 15 * 4 = 60
少女歸 = 少女到數 * 少女  # 20 * 3 = 60

# 最小公倍數即為答案
a = Fraction(長女歸 + 中女歸 + 少女歸, 3)  # Simplified to find the least common multiple
a = 60  # LCM of 5, 4, and 3#----- content ends here -----

"""
"""
