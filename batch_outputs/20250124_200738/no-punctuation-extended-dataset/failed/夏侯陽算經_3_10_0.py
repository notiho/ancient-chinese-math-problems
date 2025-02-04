"""
今有絹一千二百二十五匹三丈七尺五寸欲送州每匹一十五文充腳竝於身内抽給其絹時估毎匹一貫一百文問正及腳各幾何
術曰置絹數於丈尺已下折半五因以時估一貫一百文乗得一千六百七十八貫五百三十一文二分五氂復置一貫一百文加一十五文為法除得一千五百五匹不盡四百五十六文二分五氂進位四因之得一萬八千二百五十以下法除之得一丈六尺三寸不盡者與法退位倍之得二百二十三分寸之一百五十一欲知腳價者置元絹數丈尺寸折半五因又以腳錢一十五文乗之得二萬二千八百八十九文六氂二毫半以一貫一百一十五文為法除得二十匹不盡五百八十九文六氂二毫半進位四因之得二萬三千五百六十二文半以下法除之得二丈一尺一寸不盡者如前約之得二百二十三分寸之七十二
答曰正 a匹 腳 b匹
"""

"""
This is a complex ancient Chinese problem involving proportional distribution and calculations with fractions. Let's break it down step by step and translate it into Python code.

### Problem Explanation:
We are given:
- 1225 bolts of silk, each 3 zhang, 7 chi, and 5 cun in length.
- Each bolt is valued at 1 guan and 100 wen.
- Each bolt requires 15 wen for transportation costs ("脚").
- The goal is to determine how many bolts are used for the main payment ("正") and how many are used for transportation costs ("脚").

### Procedure:
1. Calculate the total value of the silk based on its market price.
2. Add the transportation cost per bolt to the market price to determine the divisor.
3. Divide the total value by the divisor to find the number of bolts used for the main payment ("正").
4. The remainder is used to calculate the transportation cost bolts ("脚").
5. Perform additional calculations to determine the exact lengths and values.

### Python Code:


"""

#----- content starts here -----

from fractions import Fraction

# Given data
絹數 = 1225  # Total number of bolts of silk
每匹長度 = Fraction(3 * 10 + 7, 10) + Fraction(5, 100)  # Length of each bolt in zhang (3 zhang, 7 chi, 5 cun)
時估每匹 = 1 * 1000 + 100  # Market price per bolt in wen (1 guan = 1000 wen, so 1 guan 100 wen = 1100 wen)
腳錢每匹 = 15  # Transportation cost per bolt in wen

# Step 1: Calculate the total value of the silk
總價值 = 絹數 * 時估每匹  # Total value in wen

# Step 2: Add transportation cost to market price to determine the divisor
法 = 時估每匹 + 腳錢每匹  # Divisor (market price + transportation cost)

# Step 3: Divide total value by the divisor to find the number of bolts for the main payment ("正")
正匹數 = 總價值 // 法  # Integer division to find the number of bolts for the main payment
餘文 = 總價值 % 法  # Remainder in wen

# Step 4: Calculate the number of bolts for transportation costs ("腳")
腳匹數 = 餘文 // 腳錢每匹  # Integer division to find the number of bolts for transportation costs
腳餘文 = 餘文 % 腳錢每匹  # Remainder in wen after calculating transportation costs

# Final Answer
a = 正匹數
b = 腳匹數

print(f"正 {a}匹, 腳 {b}匹")
#----- content ends here -----


"""


### Explanation of the Code:
1. **Input Data**:
   - The total number of bolts (`絹數`) is 1225.
   - The length of each bolt is converted into a fractional value in zhang (`每匹長度`).
   - The market price per bolt (`時估每匹`) is converted into wen (1 guan = 1000 wen).
   - The transportation cost per bolt (`腳錢每匹`) is given in wen.

2. **Step-by-Step Calculation**:
   - The total value of the silk (`總價值`) is calculated by multiplying the number of bolts by the market price per bolt.
   - The divisor (`法`) is the market price plus the transportation cost.
   - The number of bolts used for the main payment (`正匹數`) is calculated using integer division.
   - The remainder (`餘文`) is used to calculate the number of bolts for transportation costs (`腳匹數`).

3. **Output**:
   - The number of bolts used for the main payment (`正`) and transportation costs (`腳`) is printed.

This code follows the ancient procedure step by step, ensuring accuracy and clarity.
"""


"""
Variable 'a' has wrong value. Expected: 1342825/892, Actual: 1208
Variable 'b' has wrong value. Expected: 73245/3568, Actual: 38"""
