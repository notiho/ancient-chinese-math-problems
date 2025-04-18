"""
今有凡醬二升飼五人有醬三百二十斛問人㡬何
術曰列三百二十斛每上十之得三萬二千升以五人乘之得一十六萬升以二升除之即得
答曰 a人 
"""

#----- content starts here -----
"""
Suppose there are 2 sheng of sauce to feed 5 people. 
If there are 320 hu of sauce, how many people can be fed?

The procedure says: 
List the 320 hu. Multiply each by 10 to convert to 32,000 sheng. 
Multiply this by 5 people, obtaining 160,000 sheng. 
Divide by 2 sheng, obtaining the number of people.

Answer: *a* people.
"""

# 醬二升
每人醬 = 2

# 飼五人
每五人醬 = 5 * 每人醬

# 醬三百二十斛
醬斛 = 320

# 每上十之，得三萬二千升
醬升 = 10 * 醬斛

# 以五人乘之，得一十六萬升
總醬升 = 5 * 醬升

# 以二升除之，即得
a = 總醬升 // 每人醬#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 80000, Actual: 8000"""
