"""
今有凡醬二升飼五人，有醬三百二十斛。問：人㡬何？
術曰：列三百二十斛，每上十之得三萬二千升，以五人乘之得一十六萬升，以二升除之即得。
答曰： a人 。
"""

#----- content starts here -----
"""
Suppose there are 2 sheng of sauce to feed 5 people. There are 320 hu of sauce available.
Question: how many people can be fed?

The procedure says: Convert 320 hu into sheng by multiplying by 10, obtaining 32,000 sheng.
Multiply this by 5 people, obtaining 160,000 sheng.
Divide by 2 sheng per person to obtain the total number of people.

Answer: *a* people.
"""

# 醬二升飼五人
醬每人 = 2  # 每人需要 2 升
每組人數 = 5  # 每 5 人需要 2 升

# 醬三百二十斛
醬總量_斛 = 320  # 320 斛

# 每斛 10 升
醬總量_升 = 10 * 醬總量_斛  # 將斛轉換為升

# 以五人乘之
總需求_升 = 醬總量_升 * 每組人數

# 以二升除之即得
a = 總需求_升 // 醬每人  # 總人數

a#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 80000, Actual: 8000"""
