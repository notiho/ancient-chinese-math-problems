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
- For a square city: Place the city's circumference in li, convert it to chi, and divide by 3. Multiply the result by 5.
- Then, place 5, multiply it by 3, and square it. Also square 3, multiply it by itself, and divide by 4. Add this to the previous result to obtain the total number of deer horns.
- For a circular city: Place the city's circumference in li, convert it to chi, and divide by 3. Multiply the result by 5.
- Then, add 1, 2, 3, and 4, obtaining 10. Multiply this by 6 and add it to the previous result to obtain the total number of deer horns.

Answer: For a square city, *a* deer horns are used. For a circular city, *b* deer horns are used.
"""

# 城周二十里
城周里 = 20

# 1 里 = 300 步 = 300 * 5 尺 = 1500 尺
城周尺 = 城周里 * 1500

# Square city calculation:
# 三而一，所得
鹿角間距 = 3
鹿角數 = 城周尺 // 鹿角間距

# 五之
鹿角數 = 鹿角數 * 5

# 置五，以三乘之
五 = 5
三 = 3
五乘三 = 五 * 三

# 又自相乘
五乘三平方 = 五乘三 * 五乘三

# 以三自乘而一，所得
三平方 = 三 * 三
三平方除四 = Fraction(三平方, 4)

# 併上位，即得凡數
a = 鹿角數 + 五乘三平方 + 三平方除四

# Circular city calculation:
# 三而一，所得
鹿角數圓 = 城周尺 // 鹿角間距

# 五之
鹿角數圓 = 鹿角數圓 * 5

# 又併一二三四，凡得一十
併數 = 1 + 2 + 3 + 4

# 以六乘之
併數乘六 = 併數 * 6

# 倂之，得凡數
b = 鹿角數圓 + 併數乘六#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 60100, Actual: 200909/4
Variable 'b' has wrong value. Expected: 60060, Actual: 50060"""
