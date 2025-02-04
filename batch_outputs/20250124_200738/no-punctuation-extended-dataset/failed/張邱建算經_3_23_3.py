"""
今有城周二十里欲三尺安鹿角一枚五重安之問凡用鹿角幾何
術曰置城周里尺數三而一所得五之又置五以三乘之又自相乘以三自乘而一所得四之併上位即得凡數城若圓者置城周里尺數三而一所得五之又併一二三四凡得一十以六乘之倂之得凡數
答曰 a枚 城若圓凡用鹿角 b枚
"""

#----- content starts here -----
"""
Suppose there is a city with a perimeter of 20 li. It is desired to place deer horns (spikes) every 3 chi, in 5 layers.
Question: how many deer horns are used in total?

The procedure says:
1. Place the perimeter of the city in li, convert it to chi, and divide by 3. Multiply the result by 5.
2. Place 5, multiply it by 3, then square it. Also square 3, and divide the first result by the second. Add this to the previous result to obtain the total number of deer horns.
If the city is circular:
1. Place the perimeter of the city in li, convert it to chi, and divide by 3. Multiply the result by 5.
2. Add 1, 2, 3, and 4, obtaining 10. Multiply this by 6, and add it to the previous result to obtain the total number of deer horns.

Answer: *a* deer horns for a square city, and *b* deer horns for a circular city.
"""

# 城周二十里
城周里 = 20

# 1里 = 300步 = 300 * 5 = 1500尺
里轉尺 = 1500
城周尺 = 城周里 * 里轉尺

# 城若方 (square city)
# 三而一
步距 = 3
層數 = 5
第一步 = 城周尺 / 步距

# 所得五之
第一步 = 第一步 * 層數

# 又置五，以三乘之
第二步 = 層數 * 3

# 又自相乘
第二步平方 = 第二步**2

# 以三自乘而一
三平方 = 3**2

# 所得四之
第二步結果 = Fraction(第二步平方, 三平方)

# 併上位
a = 第一步 + 第二步結果

# 城若圓 (circular city)
# 三而一
第一步圓 = 城周尺 / 步距

# 所得五之
第一步圓 = 第一步圓 * 層數

# 又併一二三四，凡得十
圓加數 = 1 + 2 + 3 + 4

# 以六乘之
圓加數 = 圓加數 * 6

# 倂之
b = 第一步圓 + 圓加數#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 60100, Actual: 50025.0
Variable 'b' has wrong value. Expected: 60060, Actual: 50060.0"""
