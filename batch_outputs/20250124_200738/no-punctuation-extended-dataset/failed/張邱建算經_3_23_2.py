"""
今有城周二十里欲三尺安鹿角一枚五重安之問凡用鹿角幾何
術曰置城周里尺數三而一所得五之又置五以三乘之又自相乘以三自乘而一所得四之併上位即得凡數城若圓者置城周里尺數三而一所得五之又併一二三四凡得一十以六乘之倂之得凡數
答曰 a枚 城若圓凡用鹿角 b枚
"""

#----- content starts here -----
"""
Suppose there is a city with a circumference of 20 li. It is desired to place deer horns (spikes) every 3 chi, in 5 layers.
Question: how many deer horns are used in total?

The procedure says:
1. Place the circumference of the city in li, convert it to chi, and divide by 3. Multiply the result by 5.
2. Then place 5, multiply it by 3, and then square it. Also square 3, and divide the result by 4. Add this to the previous result to get the total number of deer horns.
3. If the city is circular, place the circumference of the city in li, convert it to chi, and divide by 3. Multiply the result by 5. Add 1, 2, 3, and 4 to get 10, multiply by 6, and add this to the previous result to get the total number of deer horns.

Answer: *a* deer horns for a square city, and *b* deer horns for a circular city.
"""

# 城周二十里
城周里 = 20

# 1里 = 300步 = 300尺
里到尺 = 300
城周尺 = 城周里 * 里到尺

# 三尺安鹿角一枚
鹿角間距 = 3

# 五重安之
層數 = 5

# 城若方形
# 置城周里尺數三而一所得
方形基數 = Fraction(城周尺, 鹿角間距)

# 五之
方形鹿角數 = 方形基數 * 層數

# 又置五以三乘之
五乘三 = 5 * 3

# 又自相乘
五乘三平方 = 五乘三 ** 2

# 以三自乘而一所得
三平方 = 鹿角間距 ** 2
三平方四分之一 = Fraction(三平方, 4)

# 四之併上位即得凡數
方形總數 = 方形鹿角數 + Fraction(五乘三平方, 三平方四分之一)

a = 方形總數

# 城若圓形
# 置城周里尺數三而一所得
圓形基數 = Fraction(城周尺, 鹿角間距)

# 五之
圓形鹿角數 = 圓形基數 * 層數

# 又併一二三四凡得一十
圓形附加數 = 1 + 2 + 3 + 4

# 以六乘之
圓形附加數六倍 = 圓形附加數 * 6

# 倂之得凡數
圓形總數 = 圓形鹿角數 + 圓形附加數六倍

b = 圓形總數#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 60100, Actual: 10100
Variable 'b' has wrong value. Expected: 60060, Actual: 10060"""
