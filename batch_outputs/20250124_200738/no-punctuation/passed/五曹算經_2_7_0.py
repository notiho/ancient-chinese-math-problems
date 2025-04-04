"""
今有城周四十八里欲令禦賊每三步置一兵問用兵㡬何
術曰列城周四十八里以三百步乘之得一萬四千四百步以三步除之即得
答曰 a人 
"""

#----- content starts here -----
"""
Suppose there is a city with a perimeter of 48 li. It is desired to defend against invaders by placing one soldier every 3 bu.
Question: how many soldiers are needed?

The procedure says: Arrange the city perimeter of 48 li.
Multiply it by 300 bu (since 1 li = 300 bu), obtaining 14400 bu.
Divide it by 3 bu, and the result is the number of soldiers.

Answer: *a* soldiers.
"""

# 城周四十八里
城周 = 48

# 以三百步乘之
總步數 = 300 * 城周

# 以三步除之
a = 總步數 // 3  # Use integer division since the number of soldiers must be whole#----- content ends here -----

"""
"""
