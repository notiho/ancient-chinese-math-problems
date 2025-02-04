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
- Then, place 5, multiply it by 3, and also square it. Multiply 3 by itself, and divide the result by 4. Add this to the previous result to obtain the total number.
- For a circular city: Place the circumference of the city in li, convert it to chi, and divide by 3. Multiply the result by 5. Then, add 1, 2, 3, and 4, obtaining 10. Multiply this by 6 and add it to the previous result to obtain the total number.

Answer: *a* spikes for a square city, and *b* spikes for a circular city.
"""

# 城周二十里
城周里 = 20

# 每里等於300步，每步等於5尺
里到尺 = 300 * 5

# 城周里尺數
城周尺 = 城周里 * 里到尺

# 每三尺安鹿角一枚
鹿角間距 = 3

# 五重安之
層數 = 5

# ---- For a square city ----
# 置城周里尺數三而一所得
鹿角數_方 = 城周尺 // 鹿角間距

# 五之
鹿角數_方 *= 層數

# 置五以三乘之
方層數 = 5 * 3

# 自相乘
方層數平方 = 方層數 ** 2

# 以三自乘而一所得四之
三平方 = 3 ** 2
加項_方 = 方層數平方 // (三平方 // 4)

# 併上位即得凡數
a = 鹿角數_方 + 加項_方

# ---- For a circular city ----
# 置城周里尺數三而一所得
鹿角數_圓 = 城周尺 // 鹿角間距

# 五之
鹿角數_圓 *= 層數

# 併一二三四凡得一十
加項_圓 = 1 + 2 + 3 + 4

# 以六乘之
加項_圓 *= 6

# 倂之得凡數
b = 鹿角數_圓 + 加項_圓
"""
Variable 'a' has wrong value. Expected: 60100, Actual: 50112
Variable 'b' has wrong value. Expected: 60060, Actual: 50060"""
