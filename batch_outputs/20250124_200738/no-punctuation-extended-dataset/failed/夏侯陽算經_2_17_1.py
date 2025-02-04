"""
今有租布一萬三千七百九十五端三丈七尺送納洛州計從州到彼别一十八文充水腳又抽一文充積疊並於數内抽給其布準時估端别一百五十文問正及水腳積疊等三色各幾何
術曰置元布數倍丈尺以估一百五十文乗得二百六萬九千三百六十一文為實置一百五十文加水腳一十八文又加積疊一文得一百六十九文為法除實得正布一萬二千二百四十四端不盡一百二十五文進位五因之得六千二百五十以下法除之得三丈六尺九寸不盡者與法俱退位得一百六十九分寸之一百三十九為命分也欲知水腳先置元布數倍丈尺寸以水腳一十八文乗之得二十四萬八千三百二十三文三分二氂為實以法一百六十九除得一千四百六十九端不盡六十二文三分二氂進位五因之得三千一百一十六以下法除之得一丈八尺四寸不盡一百六十九分寸之六十四為命分也欲求積疊置元布數倍丈尺寸訖所得以一文因之得一萬三千七百九十五文七分四氂以法除之得八十一端不盡一百六文七分四氂進位以五因之得五千三百三十七以下法除得三丈一尺五寸不盡者與法俱退位得一百六十九分寸之一百三十五為命分也
答曰正布 a端 水腳 b端 積疊 c端
"""

"""
This is a complex ancient Chinese math problem involving proportional calculations for distributing cloth rents, including deductions for transport costs ("water fees") and stacking fees. Below is the Python implementation of the procedure:


"""

#----- content starts here -----

from fractions import Fraction

# 元布數 (original cloth amount)
元布端 = 13795  # in duan
元布丈 = 3      # in zhang
元布尺 = 7      # in chi

# 估端別一百五十文 (price per duan)
估價 = 150

# 水腳一十八文 (water fee per duan)
水腳 = 18

# 積疊一文 (stacking fee per duan)
積疊 = 1

# 置元布數倍丈尺 (convert original cloth to total units in chi)
元布總尺 = 元布端 * 10 + 元布丈 * 10 + 元布尺  # 1 duan = 10 chi, 1 zhang = 10 chi

# 正布計算 (calculating the main cloth amount)
# 以估價乘元布總尺
正布實 = 元布總尺 * 估價

# 加水腳與積疊，得法
法 = 估價 + 水腳 + 積疊

# 除實得正布端數
正布端 = 正布實 // 法
正布餘文 = 正布實 % 法

# 餘文進位，計算剩餘的布長
正布進位 = (正布餘文 * 10) // 法
正布剩餘尺 = (正布餘文 * 10) % 法

# 水腳計算 (calculating water fees)
水腳實 = 元布總尺 * 水腳
水腳端 = 水腳實 // 法
水腳餘文 = 水腳實 % 法

# 餘文進位，計算剩餘的布長
水腳進位 = (水腳餘文 * 10) // 法
水腳剩餘尺 = (水腳餘文 * 10) % 法

# 積疊計算 (calculating stacking fees)
積疊實 = 元布總尺 * 積疊
積疊端 = 積疊實 // 法
積疊餘文 = 積疊實 % 法

# 餘文進位，計算剩餘的布長
積疊進位 = (積疊餘文 * 10) // 法
積疊剩餘尺 = (積疊餘文 * 10) % 法

# 答案
a = 正布端
b = 水腳端
c = 積疊端

print(f"正布: {a}端, 水腳: {b}端, 積疊: {c}端")
#----- content ends here -----


"""


### Explanation of the Code:
1. **元布數倍丈尺**: The original cloth amount is converted into total chi (尺) for calculations. Each duan (端) is 10 chi, and each zhang (丈) is also 10 chi.
2. **正布計算**: The main cloth amount is calculated by multiplying the total chi by the price per duan (估價). The total cost is divided by the divisor (法), which includes the price, water fee, and stacking fee.
3. **水腳計算**: The water fee is calculated similarly by multiplying the total chi by the water fee per duan and dividing by the divisor.
4. **積疊計算**: The stacking fee is calculated in the same way as the water fee.
5. **進位與剩餘**: Any remainder from the division is converted into smaller units (e.g., chi or fractions of chi) for precision.

### Final Answer:
The values of `a`, `b`, and `c` represent the amounts of cloth allocated for the main cloth, water fees, and stacking fees, respectively.
"""


"""
Variable 'a' has wrong value. Expected: 8276949/676, Actual: 122473
Variable 'b' has wrong value. Expected: 310327029/211250, Actual: 14696
Variable 'c' has wrong value. Expected: 68450337/845000, Actual: 816"""
