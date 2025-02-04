"""
今有五百六十五户，户責絲一斤十一两八銖。問：計絲㡬何？
術曰：列一斤通作十六两，納十一两得二十七两；以二十四銖乘之、納八銖，得六百五十六銖；以乘户五百六十五，得三十七萬六百四十銖；以二十四銖除之，得一萬五千四百四十三两奇八銖；又以十六两除之，得九百六十五斤奇三两；以三十斤除之，得三十二鈞奇五斤；又以四鈞除之即得。
答曰： a石 。
"""

#----- content starts here -----
"""
Suppose there are 565 households, and each household owes 1 jin, 11 liang, and 8 zhu of silk.
Question: how much silk is owed in total?

The procedure says:
- Convert 1 jin into 16 liang, then add 11 liang to get 27 liang.
- Multiply 27 liang by 24 zhu per liang, then add 8 zhu to get 656 zhu.
- Multiply 656 zhu by the 565 households to get 370,640 zhu.
- Divide 370,640 zhu by 24 zhu per liang to get 15,443 liang and 8 zhu.
- Divide 15,443 liang by 16 liang per jin to get 965 jin and 3 liang.
- Divide 965 jin by 30 jin per jun to get 32 jun and 5 jin.
- Divide 32 jun by 4 jun per shi to get the total number of shi.

Answer: *a* shi.
"""

from fractions import Fraction

# 戶數
戶數 = 565

# 每戶責絲：1斤11两8銖
斤 = 1
两 = 11
銖 = 8

# 1斤 = 16两，將1斤11两轉換為两
總两 = 斤 * 16 + 两  # 1斤 = 16两
總两 = 總两  # 27两

# 1两 = 24銖，將27两8銖轉換為銖
總銖 = 總两 * 24 + 銖  # 1两 = 24銖
總銖 = 總銖  # 656銖

# 總銖乘以戶數
總銖_所有戶 = 總銖 * 戶數  # 370,640銖

# 以24銖除之，轉換為两
總两_所有戶 = 總銖_所有戶 // 24  # 商為两數
剩餘銖 = 總銖_所有戶 % 24  # 餘數為銖數

# 以16两除之，轉換為斤
總斤_所有戶 = 總两_所有戶 // 16  # 商為斤數
剩餘两 = 總两_所有戶 % 16  # 餘數為两數

# 以30斤除之，轉換為鈞
總鈞_所有戶 = 總斤_所有戶 // 30  # 商為鈞數
剩餘斤 = 總斤_所有戶 % 30  # 餘數為斤數

# 以4鈞除之，轉換為石
總石_所有戶 = 總鈞_所有戶 // 4  # 商為石數
剩餘鈞 = 總鈞_所有戶 % 4  # 餘數為鈞數

# 答案
a = 總石_所有戶
print(f"答曰：{a}石。")#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 4633/576, Actual: 8"""
