"""
今有出錢一萬三千九百七十，買絲一石二鈞二十八斤三兩五銖。欲其貴賤鈞率之，問︰各幾何？
荅曰：其 a斤 ，鈞 b錢 。其 c石 ，鈞 d錢 。
"""

"""
To solve this problem, we need to calculate the price per unit weight (specifically per jin and per jun) based on the total cost and the total weight of the silk.

### Problem Breakdown:
- Total money spent: **13,970 qian**.
- Total weight of silk: **1 shi, 2 jun, 28 jin, 3 liang, 5 zhu**.
- Conversion factors:
  - 1 shi = 4 jun
  - 1 jun = 30 jin
  - 1 jin = 16 liang
  - 1 liang = 24 zhu

We first convert the total weight into a single unit (jin), then calculate the price per jin and per jun.

---

### Python Code:


"""


from fractions import Fraction

# Total money spent
total_money = 13970  # in qian

# Total weight of silk
shi = 1
jun = 2
jin = 28
liang = 3
zhu = 5

# Conversion factors
shi_to_jin = 4 * 30  # 1 shi = 4 jun, 1 jun = 30 jin
liang_to_jin = Fraction(1, 16)  # 1 jin = 16 liang
zhu_to_jin = Fraction(1, 16 * 24)  # 1 liang = 24 zhu

# Convert total weight to jin
total_weight_jin = (
    shi * shi_to_jin +
    jun * 30 +
    jin +
    liang * liang_to_jin +
    zhu * zhu_to_jin
)

# Calculate price per jin
price_per_jin = Fraction(total_money, total_weight_jin)

# Calculate price per jun (1 jun = 30 jin)
price_per_jun = price_per_jin * 30

# Results
a = price_per_jin  # Price per jin in qian
b = price_per_jun  # Price per jun in qian

# Convert price per jun to price per shi (1 shi = 4 jun)
price_per_shi = price_per_jun * 4

c = price_per_shi  # Price per shi in qian
d = price_per_jun  # Price per jun in qian

# Output results
print(f"Price per jin: {a} qian")
print(f"Price per jun: {b} qian")
print(f"Price per shi: {c} qian")
print(f"Price per jun: {d} qian")


"""


---

### Explanation of Variables:
- `total_weight_jin`: Converts the total weight into jin using the given conversion factors.
- `price_per_jin`: Calculates the price per jin by dividing the total money by the total weight in jin.
- `price_per_jun`: Multiplies the price per jin by 30 to get the price per jun.
- `price_per_shi`: Multiplies the price per jun by 4 to get the price per shi.

---

### Final Answer:
- **a**: Price per jin in qian.
- **b**: Price per jun in qian.
- **c**: Price per shi in qian.
- **d**: Price per jun in qian.
"""


"""
Variable 'a' has wrong value. Expected: 979/128, Actual: 5364480/79949
Variable 'b' has wrong value. Expected: 2012, Actual: 160934400/79949
Variable 'c' has wrong value. Expected: 19253/11520, Actual: 643737600/79949
Variable 'd' has wrong value. Expected: 2013, Actual: 160934400/79949"""
