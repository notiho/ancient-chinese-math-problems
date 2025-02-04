"""
今有租布一萬三千七百九十五端三丈七尺送納洛州計從州到彼别一十八文充水腳又抽一文充積疊並於數内抽給其布準時估端别一百五十文問正及水腳積疊等三色各幾何
術曰置元布數倍丈尺以估一百五十文乗得二百六萬九千三百六十一文為實置一百五十文加水腳一十八文又加積疊一文得一百六十九文為法除實得正布一萬二千二百四十四端不盡一百二十五文進位五因之得六千二百五十以下法除之得三丈六尺九寸不盡者與法俱退位得一百六十九分寸之一百三十九為命分也欲知水腳先置元布數倍丈尺寸以水腳一十八文乗之得二十四萬八千三百二十三文三分二氂為實以法一百六十九除得一千四百六十九端不盡六十二文三分二氂進位五因之得三千一百一十六以下法除之得一丈八尺四寸不盡一百六十九分寸之六十四為命分也欲求積疊置元布數倍丈尺寸訖所得以一文因之得一萬三千七百九十五文七分四氂以法除之得八十一端不盡一百六文七分四氂進位以五因之得五千三百三十七以下法除得三丈一尺五寸不盡者與法俱退位得一百六十九分寸之一百三十五為命分也
答曰正布 a端 水腳 b端 積疊 c端
"""

"""
This is a complex ancient Chinese mathematical problem involving proportional distribution and calculations of cloth, water transportation fees, and stacking fees. Below is the Python implementation of the procedure described in the problem.


"""


from fractions import Fraction

# 元布數 (original cloth count)
元布端 = 13795
元布丈 = 3
元布尺 = 7

# 估價 (price per unit cloth)
估價 = 150

# 水腳 (water transport fee per unit)
水腳 = 18

# 積疊 (stacking fee per unit)
積疊 = 1

# 置元布數倍丈尺
元布總數 = 元布端 * 10 + 元布丈 * 10 + 元布尺

# 正布計算
# 以估價乘元布總數
正布實 = 估價 * 元布總數

# 加水腳和積疊，得法
法 = 估價 + 水腳 + 積疊

# 除實得正布端數
正布端 = 正布實 // 法
正布餘數 = 正布實 % 法

# 餘數進位，計算正布的丈尺
正布進位 = (正布餘數 * 10) // 法
正布丈 = 正布進位 // 10
正布尺 = 正布進位 % 10

# 水腳計算
# 以水腳乘元布總數
水腳實 = 水腳 * 元布總數

# 除以法，得水腳端數
水腳端 = 水腳實 // 法
水腳餘數 = 水腳實 % 法

# 餘數進位，計算水腳的丈尺
水腳進位 = (水腳餘數 * 10) // 法
水腳丈 = 水腳進位 // 10
水腳尺 = 水腳進位 % 10

# 積疊計算
# 以積疊乘元布總數
積疊實 = 積疊 * 元布總數

# 除以法，得積疊端數
積疊端 = 積疊實 // 法
積疊餘數 = 積疊實 % 法

# 餘數進位，計算積疊的丈尺
積疊進位 = (積疊餘數 * 10) // 法
積疊丈 = 積疊進位 // 10
積疊尺 = 積疊進位 % 10

# 答案
a = 正布端
b = 水腳端
c = 積疊端

print(f"正布 {a} 端, 水腳 {b} 端, 積疊 {c} 端")


"""


### Explanation of the Code:
1. **元布數倍丈尺**: The total cloth count is calculated by converting the original units (端, 丈, 尺) into a single unit for easier computation.
2. **正布計算**: The total value of the cloth is calculated by multiplying the total cloth count by the price per unit. The divisor (`法`) is calculated by adding the price, water transport fee, and stacking fee. The division gives the number of cloth units (`端`) for the main cloth, and the remainder is used to calculate the smaller units (`丈`, `尺`).
3. **水腳計算**: The water transport fee is calculated similarly, using the water transport fee per unit instead of the price.
4. **積疊計算**: The stacking fee is calculated similarly, using the stacking fee per unit instead of the price.
5. **Output**: The results are printed as the number of cloth units (`端`) for the main cloth, water transport fee, and stacking fee.

This implementation follows the ancient procedure step by step, ensuring accuracy in the calculations.
"""


"""
Variable 'a' has wrong value. Expected: 8276949/676, Actual: 122473
Variable 'b' has wrong value. Expected: 310327029/211250, Actual: 14696
Variable 'c' has wrong value. Expected: 68450337/845000, Actual: 816"""
