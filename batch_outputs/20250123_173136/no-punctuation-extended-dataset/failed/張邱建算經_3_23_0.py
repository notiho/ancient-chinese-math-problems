"""
今有城周二十里欲三尺安鹿角一枚五重安之問凡用鹿角幾何
術曰置城周里尺數三而一所得五之又置五以三乘之又自相乘以三自乘而一所得四之併上位即得凡數城若圓者置城周里尺數三而一所得五之又併一二三四凡得一十以六乘之倂之得凡數
答曰 a枚 城若圓凡用鹿角 b枚
"""

"""
Suppose there is a city with a circumference of 20 li. It is desired to place deer horns (spikes) every 3 chi, in 5 layers.
Question: how many deer horns are used in total?

The procedure says:
- For a square city: Place the circumference of the city in li, convert it to chi, and divide by 3. Multiply the result by 5. 
  Then place 5, multiply it by 3, and then square it. Also square 3, multiply it by itself, and divide the result by 4. 
  Add this to the previous result to obtain the total number of deer horns.
- For a circular city: Place the circumference of the city in li, convert it to chi, and divide by 3. Multiply the result by 5. 
  Then add 1, 2, 3, and 4, obtaining 10. Multiply this by 6 and add it to the previous result to obtain the total number of deer horns.

Answer: For a square city, *a* deer horns are used. For a circular city, *b* deer horns are used.
"""

# 城周二十里
城周里 = 20

# 1里 = 300步 = 300*5 = 1500尺
里轉尺 = 1500
城周尺 = 城周里 * 里轉尺

# 安鹿角每三尺一枚
鹿角間距 = 3

# 五重安之
層數 = 5

# ---- For a square city ----
# 置城周里尺數三而一所得
鹿角數_基礎 = 城周尺 // 鹿角間距

# 五之
鹿角數_基礎 *= 層數

# 置五以三乘之
五乘三 = 5 * 3

# 自相乘
五乘三平方 = 五乘三 * 五乘三

# 以三自乘而一所得
三平方 = 鹿角間距 * 鹿角間距
三平方除四 = 三平方 // 4

# 併上位即得凡數
a = 鹿角數_基礎 + 五乘三平方 + 三平方除四

# ---- For a circular city ----
# 置城周里尺數三而一所得
鹿角數_基礎_圓 = 城周尺 // 鹿角間距

# 五之
鹿角數_基礎_圓 *= 層數

# 併一二三四凡得一十
一二三四和 = 1 + 2 + 3 + 4

# 以六乘之
一二三四和乘六 = 一二三四和 * 6

# 倂之得凡數
b = 鹿角數_基礎_圓 + 一二三四和乘六
"""
Variable 'a' has wrong value. Expected: 60100, Actual: 50227
Variable 'b' has wrong value. Expected: 60060, Actual: 50060"""
