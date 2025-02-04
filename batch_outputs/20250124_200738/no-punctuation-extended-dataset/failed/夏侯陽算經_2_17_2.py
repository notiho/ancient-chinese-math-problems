"""
今有租布一萬三千七百九十五端三丈七尺送納洛州計從州到彼别一十八文充水腳又抽一文充積疊並於數内抽給其布準時估端别一百五十文問正及水腳積疊等三色各幾何
術曰置元布數倍丈尺以估一百五十文乗得二百六萬九千三百六十一文為實置一百五十文加水腳一十八文又加積疊一文得一百六十九文為法除實得正布一萬二千二百四十四端不盡一百二十五文進位五因之得六千二百五十以下法除之得三丈六尺九寸不盡者與法俱退位得一百六十九分寸之一百三十九為命分也欲知水腳先置元布數倍丈尺寸以水腳一十八文乗之得二十四萬八千三百二十三文三分二氂為實以法一百六十九除得一千四百六十九端不盡六十二文三分二氂進位五因之得三千一百一十六以下法除之得一丈八尺四寸不盡一百六十九分寸之六十四為命分也欲求積疊置元布數倍丈尺寸訖所得以一文因之得一萬三千七百九十五文七分四氂以法除之得八十一端不盡一百六文七分四氂進位以五因之得五千三百三十七以下法除得三丈一尺五寸不盡者與法俱退位得一百六十九分寸之一百三十五為命分也
答曰正布 a端 水腳 b端 積疊 c端
"""

"""
This is a complex problem involving multiple calculations for determining the distribution of cloth rent into three categories: the actual cloth rent (正布), the water transport fee (水腳), and the stacking fee (積疊). Let's translate the procedure into Python step by step.


"""

#----- content starts here -----

from fractions import Fraction

# 元布數 (original cloth rent): 13,795端 3丈 7尺
元布端數 = 13795
元布丈 = 3
元布尺 = 7

# Convert the original cloth rent into a single unit (尺)
元布總尺 = 元布端數 * 30 + 元布丈 * 10 + 元布尺

# 估端別一百五十文 (price per unit of cloth): 150文
估價 = 150

# 水腳 (water transport fee per unit): 18文
水腳 = 18

# 積疊 (stacking fee per unit): 1文
積疊 = 1

# 正布計算 (Actual cloth rent calculation)
# 置元布數倍丈尺以估一百五十文乘得為實
正布實 = 元布總尺 * 估價

# 置一百五十文加水腳一十八文又加積疊一文得為法
正布法 = 估價 + 水腳 + 積疊

# 除實得正布端數
正布端數 = 正布實 // 正布法

# 不盡部分
正布餘文 = 正布實 % 正布法

# 進位五因之
正布進位 = (正布餘文 * 5) // 正布法

# 得正布的丈尺
正布總尺 = 正布進位
正布丈 = 正布總尺 // 10
正布尺 = 正布總尺 % 10

# 水腳計算 (Water transport fee calculation)
# 置元布數倍丈尺以水腳一十八文乘之得為實
水腳實 = 元布總尺 * 水腳

# 以法除之得水腳端數
水腳端數 = 水腳實 // 正布法

# 不盡部分
水腳餘文 = 水腳實 % 正布法

# 進位五因之
水腳進位 = (水腳餘文 * 5) // 正布法

# 得水腳的丈尺
水腳總尺 = 水腳進位
水腳丈 = 水腳總尺 // 10
水腳尺 = 水腳總尺 % 10

# 積疊計算 (Stacking fee calculation)
# 置元布數倍丈尺以積疊一文乘之得為實
積疊實 = 元布總尺 * 積疊

# 以法除之得積疊端數
積疊端數 = 積疊實 // 正布法

# 不盡部分
積疊餘文 = 積疊實 % 正布法

# 進位五因之
積疊進位 = (積疊餘文 * 5) // 正布法

# 得積疊的丈尺
積疊總尺 = 積疊進位
積疊丈 = 積疊總尺 // 10
積疊尺 = 積疊總尺 % 10

# 答案
a = 正布端數
b = 水腳端數
c = 積疊端數

print(f"正布: {a}端, 水腳: {b}端, 積疊: {c}端")
#----- content ends here -----


"""


### Explanation:
1. **正布 (Actual cloth rent)**:
   - Multiply the total cloth rent (in 尺) by the price per unit (150文).
   - Add the water transport fee (18文) and stacking fee (1文) to get the divisor.
   - Divide the total value by the divisor to get the number of 正布端數.

2. **水腳 (Water transport fee)**:
   - Multiply the total cloth rent (in 尺) by the water transport fee (18文).
   - Divide by the same divisor to get the number of 水腳端數.

3. **積疊 (Stacking fee)**:
   - Multiply the total cloth rent (in 尺) by the stacking fee (1文).
   - Divide by the same divisor to get the number of 積疊端數.

4. **進位 and 不盡部分**:
   - Handle the remainder (不盡部分) by multiplying it by 5 and dividing by the divisor to calculate the additional fraction.

This code calculates the exact distribution of 正布, 水腳, and 積疊 based on the given procedure.
"""


"""
Variable 'a' has wrong value. Expected: 8276949/676, Actual: 367355
Variable 'b' has wrong value. Expected: 310327029/211250, Actual: 44082
Variable 'c' has wrong value. Expected: 68450337/845000, Actual: 2449"""
