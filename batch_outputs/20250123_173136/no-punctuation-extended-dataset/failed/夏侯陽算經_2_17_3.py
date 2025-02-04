"""
今有租布一萬三千七百九十五端三丈七尺送納洛州計從州到彼别一十八文充水腳又抽一文充積疊並於數内抽給其布準時估端别一百五十文問正及水腳積疊等三色各幾何
術曰置元布數倍丈尺以估一百五十文乗得二百六萬九千三百六十一文為實置一百五十文加水腳一十八文又加積疊一文得一百六十九文為法除實得正布一萬二千二百四十四端不盡一百二十五文進位五因之得六千二百五十以下法除之得三丈六尺九寸不盡者與法俱退位得一百六十九分寸之一百三十九為命分也欲知水腳先置元布數倍丈尺寸以水腳一十八文乗之得二十四萬八千三百二十三文三分二氂為實以法一百六十九除得一千四百六十九端不盡六十二文三分二氂進位五因之得三千一百一十六以下法除之得一丈八尺四寸不盡一百六十九分寸之六十四為命分也欲求積疊置元布數倍丈尺寸訖所得以一文因之得一萬三千七百九十五文七分四氂以法除之得八十一端不盡一百六文七分四氂進位以五因之得五千三百三十七以下法除得三丈一尺五寸不盡者與法俱退位得一百六十九分寸之一百三十五為命分也
答曰正布 a端 水腳 b端 積疊 c端
"""

"""
This is a complex ancient Chinese math problem involving proportional distribution of cloth rents, water transport fees, and stacking fees. Below is the Python implementation of the procedure ("術") described in the problem.


"""


from fractions import Fraction

# 元布數 (original cloth count in duan, zhang, chi)
元布端數 = 13795
元布丈數 = 3
元布尺數 = 7

# 估價 (price per duan)
估價 = 150

# 水腳 (water transport fee per duan)
水腳 = 18

# 積疊 (stacking fee per duan)
積疊 = 1

# 將元布數轉換為總丈尺數 (convert original cloth count to total zhang and chi)
總布數 = 元布端數 * 10 + 元布丈數 * 10 + 元布尺數

# 正布計算
# 置元布數倍丈尺以估一百五十文乘得實
正布實 = 總布數 * 估價

# 置估價加水腳又加積疊為法
正布法 = 估價 + 水腳 + 積疊

# 除實得正布端數
正布端數 = 正布實 // 正布法
正布餘文 = 正布實 % 正布法

# 餘文進位五因之
正布進位 = (正布餘文 * 10) // 正布法

# 餘文以下法除之得丈尺
正布丈尺 = (正布餘文 * 10) % 正布法

# 水腳計算
水腳實 =元

"""

"""


"""
Code error: name '元' is not defined"""
