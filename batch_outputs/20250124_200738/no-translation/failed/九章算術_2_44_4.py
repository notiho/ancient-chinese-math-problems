"""
今有出錢六百一十，買羽二千一百翭。欲其貴賤率之，問︰各幾何？
反其率術曰：以錢數為法，所率為實，實如法而一。不滿法者反以實減法，法少，實多。二物各以所得多少之數乘法實，即物數。
荅曰：其 a翭 ， b翭 一錢 其 c翭 ， d翭 一錢
"""

"""
To solve this problem, we need to calculate the rates of "貴" (expensive) and "賤" (cheap) for the given money and items. Let's follow the procedure step by step:

---

### Definitions:
- 出錢 (total money): 610
- 羽翭 (total items): 2100翭

---

### Procedure:
1. **以錢數為法**: The total money (610) is the "法" (denominator).
2. **所率為實**: The total items (2100翭) is the "實" (numerator).
3. **實如法而一**: Divide the total items by the total money to find the rate.

---

### Python Code:


"""

#----- content starts here -----

from fractions import Fraction

# 出錢六百一十
錢數 = 610

# 羽二千一百翭
羽翭數 = 2100

# 以錢數為法
法 = 錢數

# 所率為實
實 = 羽翭數

# 實如法而一
每錢翭數 = Fraction(實, 法)

# 分為貴賤兩部分
# 假設貴的部分是 a翭 一錢，賤的部分是 b翭 一錢
# 貴賤比例可以自由設定，這裡假設貴:賤 = 2:3
貴比例 = 2
賤比例 = 3
總比例 = 貴比例 + 賤比例

# 計算貴和賤的翭數
貴翭 = Fraction(貴比例, 總比例) * 羽翭數
賤翭 = Fraction(賤比例, 總比例) * 羽翭數

# 計算貴和賤的每錢翭數
貴每錢翭數 = Fraction(貴翭, 法)
賤每錢翭數 = Fraction(賤翭, 法)

# 結果
a = 貴翭
b = 貴每錢翭數
c = 賤翭
d = 賤每錢翭數
#----- content ends here -----


"""


---

### Explanation of Results:
- `a翭 , b翭 一錢`: The number of expensive items and their rate per money unit.
- `c翭 , d翭 一錢`: The number of cheap items and their rate per money unit.


"""


"""
Variable 'a' has wrong value. Expected: 1140, Actual: 840
Variable 'b' has wrong value. Expected: 3, Actual: 84/61
Variable 'c' has wrong value. Expected: 960, Actual: 1260
Variable 'd' has wrong value. Expected: 4, Actual: 126/61"""
