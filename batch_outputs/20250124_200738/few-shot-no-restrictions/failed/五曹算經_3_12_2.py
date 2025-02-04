"""
今有凡醬二升飼五人，有醬三百二十斛。問：人㡬何？
術曰：列三百二十斛，每上十之得三萬二千升，以五人乘之得一十六萬升，以二升除之即得。
答曰： a人 。
"""

#----- content starts here -----
"""
Suppose there are 2 sheng of sauce to feed 5 people. There are 320 hu of sauce available.
Question: how many people can be fed?

The procedure says: Convert 320 hu into sheng by multiplying by 10 for each hu, obtaining 32,000 sheng.
Multiply this by 5 people, obtaining 160,000 sheng.
Divide this by 2 sheng per person to get the total number of people.

Answer: *a* people.
"""

# 醬二升飼五人
醬每人 = 2  # 每人需要2升

# 醬三百二十斛
醬總量_斛 = 320

# 每斛十升
升每斛 = 10

# 將斛轉換為升
醬總量_升 = 醬總量_斛 * 升每斛

# 以五人乘之
總需求 = 醬總量_升 * 5

# 以二升除之即得
a = 總需求 // 醬每人

a#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 80000, Actual: 8000"""
