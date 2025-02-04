"""
今有絹一千二百二十五匹三丈七尺五寸欲送州每匹一十五文充腳竝於身内抽給其絹時估毎匹一貫一百文問正及腳各幾何
術曰置絹數於丈尺已下折半五因以時估一貫一百文乗得一千六百七十八貫五百三十一文二分五氂復置一貫一百文加一十五文為法除得一千五百五匹不盡四百五十六文二分五氂進位四因之得一萬八千二百五十以下法除之得一丈六尺三寸不盡者與法退位倍之得二百二十三分寸之一百五十一欲知腳價者置元絹數丈尺寸折半五因又以腳錢一十五文乗之得二萬二千八百八十九文六氂二毫半以一貫一百一十五文為法除得二十匹不盡五百八十九文六氂二毫半進位四因之得二萬三千五百六十二文半以下法除之得二丈一尺一寸不盡者如前約之得二百二十三分寸之七十二
答曰正 a匹 腳 b匹
"""

"""
This is a complex ancient Chinese problem involving proportional distribution and calculations with units of currency and cloth. Let's break it down step by step and translate it into Python code.

### Problem Explanation:
We are given:
- 1225 bolts of silk, each 3 zhang, 7 chi, and 5 cun in length.
- Each bolt is valued at 1 guan and 100 wen.
- Additional transportation cost per bolt is 15 wen.
- We need to calculate:
  1. The number of bolts used for the main payment (`正`).
  2. The number of bolts used for the transportation cost (`腳`).

### Procedure:
1. **Calculate the total value of the silk**:
   - Multiply the number of bolts by the value per bolt (1 guan and 100 wen).
2. **Determine the divisor (法)**:
   - Add the transportation cost (15 wen) to the value per bolt.
3. **Calculate the number of bolts for the main payment (`正`)**:
   - Divide the total value of the silk by the divisor.
   - Handle any remainder by converting it into smaller units (wen, fen, li).
4. **Calculate the number of bolts for the transportation cost (`腳`)**:
   - Multiply the original number of bolts by the transportation cost (15 wen).
   - Divide this by the divisor to determine the number of bolts for transportation.

### Python Code:


"""


from fractions import Fraction

# Given data
絹數 = 1225  # Total bolts of silk
每匹價值 = 1 * 1000 + 100  # 1 guan and 100 wen = 1100 wen
運費每匹 = 15  # Transportation cost per bolt in wen

# Step 1: Calculate the total value of the silk
總價值 = 絹數 * 每匹價值  # Total value in wen

# Step 2: Determine the divisor (法)
法 = 每匹價值 + 運費每匹  # Value per bolt + transportation cost

# Step 3: Calculate the number of bolts for the main payment (正)
正匹數 = 總價值 // 法  # Integer division to get the number of bolts
正餘數 = 總價值 % 法  # Remainder in wen

# Convert the remainder into smaller units (if needed)
正餘數進位 = Fraction(正餘數, 法)

# Step 4: Calculate the number of bolts for the transportation cost (腳)
運費總價值 = 絹數 * 運費每匹  # Total transportation cost in wen
腳匹數 = 運費總價值 // 法  # Integer division to get the number of bolts
腳餘數 = 運費總價值 % 法  # Remainder in wen

# Convert the remainder into smaller units (if needed)
腳餘數進位 = Fraction(腳餘數, 法)

# Final results
a = 正匹數
b = 腳匹數

print(f"正 {a} 匹, 腳 {b} 匹")


"""


### Explanation of Results:
- `a` represents the number of bolts used for the main payment (`正`).
- `b` represents the number of bolts used for the transportation cost (`腳`).

This code follows the ancient procedure step by step, ensuring that all calculations are consistent with the original method.
"""


"""
Variable 'a' has wrong value. Expected: 1342825/892, Actual: 1208
Variable 'b' has wrong value. Expected: 73245/3568, Actual: 16"""
