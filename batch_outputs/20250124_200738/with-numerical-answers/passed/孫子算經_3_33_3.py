"""
今有三女，長女五日一歸，中女四日一歸，少女三日一歸。問：三女幾何日相會？
術曰：置長女五日，中女四日，少女三日，于右方，各列一算于左方，維乘之，各得所到數。長女十二到，中女十五到，少女二十到，又各以歸日乘到數，即得。
答曰： a(=60)日 。
"""

#----- content starts here -----
"""
Suppose there are three daughters. The eldest daughter returns every 5 days, the middle daughter every 4 days, and the youngest daughter every 3 days.
Question: after how many days will the three daughters meet?

The procedure says: Place the eldest daughter's 5 days, the middle daughter's 4 days, and the youngest daughter's 3 days on the right side.
For each, place a single counting rod on the left side.
Multiply them crosswise, obtaining their respective "arrival numbers."
The eldest daughter arrives 12 times, the middle daughter 15 times, and the youngest daughter 20 times.
Then, multiply each by the number of days it takes them to return, obtaining the result.

Answer: *a*(=60) days.
"""

# 長女五日
長女歸日 = 5

# 中女四日
中女歸日 = 4

# 少女三日
少女歸日 = 3

# 維乘之，各得所到數
長女到數 = 中女歸日 * 少女歸日  # 4 * 3 = 12
中女到數 = 長女歸日 * 少女歸日  # 5 * 3 = 15
少女到數 = 長女歸日 * 中女歸日  # 5 * 4 = 20

# 又各以歸日乘到數，即得
長女結果 = 長女歸日 * 長女到數  # 5 * 12 = 60
中女結果 = 中女歸日 * 中女到數  # 4 * 15 = 60
少女結果 = 少女歸日 * 少女到數  # 3 * 20 = 60

# 最小公倍數即為答案
a = 長女結果  # 60 days#----- content ends here -----

"""
"""
