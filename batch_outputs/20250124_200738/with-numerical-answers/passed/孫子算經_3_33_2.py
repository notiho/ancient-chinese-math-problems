"""
今有三女，長女五日一歸，中女四日一歸，少女三日一歸。問：三女幾何日相會？
術曰：置長女五日，中女四日，少女三日，于右方，各列一算于左方，維乘之，各得所到數。長女十二到，中女十五到，少女二十到，又各以歸日乘到數，即得。
答曰： a(=60)日 。
"""

#----- content starts here -----
"""
Suppose there are three daughters. The eldest daughter returns home every 5 days, the middle daughter every 4 days, and the youngest daughter every 3 days.
Question: after how many days will all three daughters meet at home?

The procedure says: Place the eldest daughter's 5 days, the middle daughter's 4 days, and the youngest daughter's 3 days on the right side.
For each, place one counting rod on the left side.
Cross-multiply them, obtaining the respective "arrival numbers."
The eldest daughter arrives 12 times, the middle daughter 15 times, and the youngest daughter 20 times.
Then, multiply each "arrival number" by the respective return days, obtaining the least common multiple.

Answer: *a*(=60) days.
"""

# 長女五日一歸
長女歸日 = 5

# 中女四日一歸
中女歸日 = 4

# 少女三日一歸
少女歸日 = 3

# 維乘之，各得所到數
長女到數 = 中女歸日 * 少女歸日  # 4 * 3 = 12
中女到數 = 長女歸日 * 少女歸日  # 5 * 3 = 15
少女到數 = 長女歸日 * 中女歸日  # 5 * 4 = 20

# 又各以歸日乘到數，即得
長女乘積 = 長女到數 * 長女歸日  # 12 * 5 = 60
中女乘積 = 中女到數 * 中女歸日  # 15 * 4 = 60
少女乘積 = 少女到數 * 少女歸日  # 20 * 3 = 60

# 最小公倍數
a = 長女乘積  # 60 days#----- content ends here -----

"""
"""
