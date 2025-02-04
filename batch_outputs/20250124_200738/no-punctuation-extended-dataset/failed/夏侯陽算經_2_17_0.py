"""
今有租布一萬三千七百九十五端三丈七尺送納洛州計從州到彼别一十八文充水腳又抽一文充積疊並於數内抽給其布準時估端别一百五十文問正及水腳積疊等三色各幾何
術曰置元布數倍丈尺以估一百五十文乗得二百六萬九千三百六十一文為實置一百五十文加水腳一十八文又加積疊一文得一百六十九文為法除實得正布一萬二千二百四十四端不盡一百二十五文進位五因之得六千二百五十以下法除之得三丈六尺九寸不盡者與法俱退位得一百六十九分寸之一百三十九為命分也欲知水腳先置元布數倍丈尺寸以水腳一十八文乗之得二十四萬八千三百二十三文三分二氂為實以法一百六十九除得一千四百六十九端不盡六十二文三分二氂進位五因之得三千一百一十六以下法除之得一丈八尺四寸不盡一百六十九分寸之六十四為命分也欲求積疊置元布數倍丈尺寸訖所得以一文因之得一萬三千七百九十五文七分四氂以法除之得八十一端不盡一百六文七分四氂進位以五因之得五千三百三十七以下法除得三丈一尺五寸不盡者與法俱退位得一百六十九分寸之一百三十五為命分也
答曰正布 a端 水腳 b端 積疊 c端
"""

"""
This is a complex problem involving the calculation of cloth rent, water transport fees, and stacking fees. Let's break it down step by step and encode the procedure into Python.

### Problem Description:
- There are **13,795端 (duan)** of cloth, each measuring **3丈7尺 (zhang and chi)**.
- The cost per duan is **150文 (wen)**.
- Additional fees:
  - **18文** per duan for water transport.
  - **1文** per duan for stacking.
- The goal is to calculate:
  - **a**: The amount of cloth after deducting fees (正布, "correct cloth").
  - **b**: The amount of cloth used for water transport fees (水腳, "water transport").
  - **c**: The amount of cloth used for stacking fees (積疊, "stacking").

---

### Procedure:
1. **正布 (Correct Cloth)**:
   - Multiply the total cloth (in duan and zhang/chi) by the cost per duan (150文).
   - Add the water transport fee (18文) and stacking fee (1文) to get the total fee per duan (169文).
   - Divide the total cost by the total fee per duan to get the correct cloth.

2. **水腳 (Water Transport)**:
   - Multiply the total cloth by the water transport fee (18文).
   - Divide the result by the total fee per duan (169文) to get the water transport cloth.

3. **積疊 (Stacking)**:
   - Multiply the total cloth by the stacking fee (1文).
   - Divide the result by the total fee per duan (169文) to get the stacking cloth.

---

### Python Code:


"""

#----- content starts here -----

from fractions import Fraction

# 元布數 (Original cloth count)
元布端 = 13795  # in duan
元布丈 = 3      # in zhang
元布尺 = 7      # in chi

# Convert the cloth dimensions to a single unit (chi):
# 1 zhang = 10 chi
元布總尺 = 元布端 * (元布丈 * 10 + 元布尺)

# 估價 (Cost per duan)
估價 = 150  # in wen

# 水腳 (Water transport fee per duan)
水腳費 = 18  # in wen

# 積疊 (Stacking fee per duan)
積疊費 = 1  # in wen

# 法 (Total fee per duan)
法 = 估價 + 水腳費 + 積疊費  # 150 + 18 + 1 = 169 wen

# 正布 (Correct Cloth)
正布實 = 元布總尺 * 估價  # Total cost for the cloth
正布端 = 正布實 // 法  # Integer division to get the number of duan
正布餘文 = 正布實 % 法  # Remainder in wen
正布進位 = (正布餘文 * 5) // 法  # Convert remainder to chi
正布尺 = 正布進位 // 10  # Convert chi to zhang and chi
正布寸 = Fraction(正布進位 % 10, 法)  # Remaining fraction in chi

# 水腳 (Water Transport)
水腳實 = 元布總尺 * 水腳費  # Total cost for water transport
水腳端 = 水腳實 // 法  # Integer division to get the number of duan
水腳餘文 = 水腳實 % 法  # Remainder in wen
水腳進位 = (水腳餘文 * 5) // 法  # Convert remainder to chi
水腳尺 = 水腳進位 // 10  # Convert chi to zhang and chi
水腳寸 = Fraction(水腳進位 % 10, 法)  # Remaining fraction in chi

# 積疊 (Stacking)
積疊實 = 元布總尺 * 積疊費  # Total cost for stacking
積疊端 = 積疊實 // 法  # Integer division to get the number of duan
積疊餘文 = 積疊實 % 法  # Remainder in wen
積疊進位 = (積疊餘文 * 5) // 法  # Convert remainder to chi
積疊尺 = 積疊進位 // 10  # Convert chi to zhang and chi
積疊寸 = Fraction(積疊進位 % 10, 法)  # Remaining fraction in chi

# Final Results
a = 正布端  # 正布 in duan
b = 水腳端  # 水腳 in duan
c = 積疊端  # 積疊 in duan

print(f"正布: {a}端")
print(f"水腳: {b}端")
print(f"積疊: {c}端")
#----- content ends here -----


"""


---

### Explanation of Results:
- **正布 (Correct Cloth)**: The amount of cloth left after deducting fees.
- **水腳 (Water Transport)**: The amount of cloth used for water transport fees.
- **積疊 (Stacking)**: The amount of cloth used for stacking fees.

This code follows the procedure described in the problem and calculates the results step by step.
"""


"""
Variable 'a' has wrong value. Expected: 8276949/676, Actual: 453031
Variable 'b' has wrong value. Expected: 310327029/211250, Actual: 54363
Variable 'c' has wrong value. Expected: 68450337/845000, Actual: 3020"""
