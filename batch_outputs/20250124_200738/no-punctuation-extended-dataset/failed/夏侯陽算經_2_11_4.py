"""
今有粟三千八百四十斛欲給馬毎匹五升問給幾何
術曰置粟數再上十之為升以五升除之得馬匹數
答曰給馬 a匹
"""

#----- content starts here -----
"""
Suppose there are 3840 hu of millet. It is desired to distribute it to horses, each horse receiving 5 sheng.
Question: how many horses can be fed?

The procedure says: Place the amount of millet, multiply it by 10 to convert it to sheng.
Divide it by 5 sheng to obtain the number of horses.

Answer: it feeds *a* horses.
"""

# 粟三千八百四十斛
粟數 = 3840

# 再上十之，為升
升數 = 10 * 粟數

# 以五升除之，得馬匹數
a = 升數 // 5  # Use integer division since the number of horses must be whole#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 76800, Actual: 7680"""
