"""
今有出錢一萬三千九百七十，買絲一石二鈞二十八斤三兩五銖。欲其貴賤石率之，問︰各幾何？
其率術曰：各置所買石、鈞、斤、兩以為法，以所率乘錢數為實，實如法而一。不滿法者反以實減法，法賤實貴。
荅曰：其 a鈞 ，石 b錢 。其 c石 ，石 d錢 。
"""

"""
This problem involves calculating the price per unit weight of silk based on the total cost and the total weight. The weight is given in a traditional Chinese system of units: 石 (shi), 鈞 (jun), 斤 (jin), 兩 (liang), and 銖 (zhu). The goal is to determine the price per 石 (shi) and 鈞 (jun).

---

### Problem Breakdown:
- **Total money spent**: 13,970 (錢)
- **Total weight of silk**: 1 石, 2 鈞, 28 斤, 3 兩, 5 銖
- **Question**: What is the price per 石 (shi) and per 鈞 (jun)?

---

### Conversion Factors:
1 石 = 4 鈞  
1 鈞 = 30 斤  
1 斤 = 16 兩  
1 兩 = 24 銖  

---

### Procedure:
1. Convert the total weight into 銖 (zhu), the smallest unit.
2. Calculate the total price per 銖.
3. Convert the price per 銖 back into the price per 鈞 and per 石.

---

### Python Code:


"""

#----- content starts here -----

from fractions import Fraction

# Total money spent
total_money = 13970  # 錢

# Total weight: 1 石, 2 鈞, 28 斤, 3 兩, 5 銖
shi = 1
jun = 2
jin = 28
liang = 3
zhu = 5

# Conversion factors
shi_to_jun = 4
jun_to_jin = 30
jin_to_liang = 16
liang_to_zhu = 24

# Step 1: Convert total weight into 銖
total_zhu = (
    shi * shi_to_jun * jun_to_jin * jin_to_liang * liang_to_zhu +
    jun * jun_to_jin * jin_to_liang * liang_to_zhu +
    jin * jin_to_liang * liang_to_zhu +
    liang * liang_to_zhu +
    zhu
)

# Step 2: Calculate the price per 銖
price_per_zhu = Fraction(total_money, total_zhu)

# Step 3: Convert price per 銖 to price per 鈞 and 石
# Price per 鈞
zhu_per_jun = jun_to_jin * jin_to_liang * liang_to_zhu
price_per_jun = price_per_zhu * zhu_per_jun

# Price per 石
zhu_per_shi = shi_to_jun * zhu_per_jun
price_per_shi = price_per_zhu * zhu_per_shi

# Results
a = price_per_jun  # Price per 鈞
b = price_per_shi  # Price per 石

# Output
print(f"其 {a} 鈞 ，石 {b} 錢 。")
#----- content ends here -----


"""


---

### Explanation of the Code:
1. **Weight Conversion**: The total weight is converted into the smallest unit, 銖, using the provided conversion factors.
2. **Price per 銖**: The total money is divided by the total weight in 銖 to get the price per 銖.
3. **Price per 鈞 and 石**: The price per 鈖 is scaled up to calculate the price per 鈞 and 石 using the conversion factors.

---

### Example Output:
If you run the code, it will calculate the price per 鈞 and 石 based on the given inputs. The results will be expressed as fractions for precision.
"""


"""
Variable 'a' has wrong value. Expected: 979/960, Actual: 160934400/79949
Variable 'b' has wrong value. Expected: 8051, Actual: 643737600/79949
Missing variable in output: 'c'
Missing variable in output: 'd'"""
