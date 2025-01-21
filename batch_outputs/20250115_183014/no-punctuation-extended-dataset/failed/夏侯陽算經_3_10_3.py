"""
今有絹一千二百二十五匹三丈七尺五寸欲送州每匹一十五文充腳竝於身内抽給其絹時估毎匹一貫一百文問正及腳各幾何
術曰置絹數於丈尺已下折半五因以時估一貫一百文乗得一千六百七十八貫五百三十一文二分五氂復置一貫一百文加一十五文為法除得一千五百五匹不盡四百五十六文二分五氂進位四因之得一萬八千二百五十以下法除之得一丈六尺三寸不盡者與法退位倍之得二百二十三分寸之一百五十一欲知腳價者置元絹數丈尺寸折半五因又以腳錢一十五文乗之得二萬二千八百八十九文六氂二毫半以一貫一百一十五文為法除得二十匹不盡五百八十九文六氂二毫半進位四因之得二萬三千五百六十二文半以下法除之得二丈一尺一寸不盡者如前約之得二百二十三分寸之七十二
答曰正 a匹 b丈 腳 c匹 d丈
"""

"""
This is a complex problem involving calculations for distributing silk and determining the exact amount for "正" (main portion) and "腳" (additional portion). Let's break it down step by step and encode the procedure into Python.

### Problem Breakdown:
- **Given**:
  - Total silk: 1225 pieces, each 3丈7尺5寸 (3 zhang, 7 chi, 5 cun).
  - Each piece costs 15文 for transportation.
  - Market value: 1貫100文 per piece.

- **Question**:
  - How many pieces are allocated for the main portion ("正") and how many for the additional portion ("腳")?
  - What is the length of silk in zhang, chi, and cun for each portion?

- **Procedure**:
  - First, calculate the total value of the silk using the market price.
  - Determine the number of pieces allocated for the main portion and the remaining value.
  - Calculate the length of silk for the main portion and the additional portion.
  - Determine the transportation cost for the additional portion and calculate its length.

### Python Code:


"""


from fractions import Fraction

# Given data
絹數 = 1225  # Total silk pieces
每匹長度 = Fraction(3, 1) + Fraction(7, 10) + Fraction(5, 100)  # Length per piece: 3丈7尺5寸
時估每匹 = 1 * 1000 + 100  # Market price per piece: 1貫100文
腳錢每匹 = 15  # Transportation cost per piece

# Step 1: Calculate total value of silk
總價值 = 絹數 * 時估每匹  # Total value in 文

# Step 2: Add transportation cost to market price
法 = 時估每匹 + 腳錢每匹  # Total cost per piece (market price + transportation cost)

# Step 3: Calculate the number of pieces for the main portion ("正")
正匹數 = 總價值 // 法  # Number of pieces for the main portion
剩餘文 = 總價值 % 法  # Remaining value in 文

# Step 4: Calculate the length of silk for the main portion
正總長度 = 正匹數 * 每匹長度  # Total length for the main portion
正丈 = int(正總長度)  # Extract zhang
正尺 = int((正總長度 - 正丈) * 10)  # Extract chi
正寸 = int(((正總長度 - 正丈) * 10 - 正尺) * 10)  # Extract cun

# Step 5: Calculate the number of pieces for the additional portion ("腳")
腳匹數 = 剩餘文 // 腳錢每匹  # Number of pieces for the additional portion
腳剩餘文 = 剩餘文 % 腳錢每匹  # Remaining value in 文 for the additional portion

# Step 6: Calculate the length of silk for the additional portion
腳總長度 = 腳匹數 * 每匹長度  # Total length for the additional portion
腳丈 = int(腳總長度)  # Extract zhang
腳尺 = int((腳總長度 - 腳丈) * 10)  # Extract chi
腳寸 = int(((腳總長度 - 腳丈) * 10 - 腳尺) * 10)  # Extract cun

# Final Answer
a = 正匹數
b = f"{正丈}丈{正尺}尺{正寸}寸"
c = 腳匹數
d = f"{腳丈}丈{腳尺}尺{腳寸}寸"

print(f"正: {a}匹, {b}")
print(f"腳: {c}匹, {d}")


"""


### Explanation of the Code:
1. **Step 1**: Calculate the total value of the silk by multiplying the total number of pieces by the market price per piece.
2. **Step 2**: Add the transportation cost to the market price to get the total cost per piece.
3. **Step 3**: Divide the total value by the total cost per piece to determine the number of pieces for the main portion ("正"). The remainder is the leftover value.
4. **Step 4**: Calculate the total length of silk for the main portion and extract the zhang, chi, and cun.
5. **Step 5**: Use the leftover value to determine the number of pieces for the additional portion ("腳").
6. **Step 6**: Calculate the total length of silk for the additional portion and extract the zhang, chi, and cun.

### Output:
The program will output the number of pieces and the length of silk for both the main portion ("正") and the additional portion ("腳").
"""


"""
Variable 'a' has wrong value. Expected: 1505, Actual: 1208
Variable 'b' has wrong value. Expected: 365/223, Actual: 4530丈0尺0寸
Variable 'c' has wrong value. Expected: 20, Actual: 38
Variable 'd' has wrong value. Expected: 1885/892, Actual: 142丈5尺0寸"""
