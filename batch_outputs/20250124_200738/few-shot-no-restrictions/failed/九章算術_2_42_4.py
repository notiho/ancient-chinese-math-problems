"""
今有出錢一萬三千九百七十，買絲一石二鈞二十八斤三兩五銖。欲其貴賤兩率之，問︰各幾何？
其率術曰：各置所買石、鈞、斤、兩以為法，以所率乘錢數為實，實如法而一。不滿法者反以實減法，法賤實貴。
荅曰：其 a石 ，兩 b錢 。其 c鈞 ，兩 d錢 。
"""

"""
This problem involves calculating the price per unit weight (stone, jun, etc.) for a given amount of money and silk. Let's break it down step by step and translate it into Python code.

### Problem Breakdown:
- **Money spent:** 13,970 (in some monetary unit).
- **Silk purchased:** 1 stone, 2 jun, 28 jin, 3 liang, and 5 zhu.
- **Goal:** Calculate the price per unit weight for each weight category (stone, jun, etc.).

### Procedure:
1. Convert the total weight into a single unit for easier calculations.
   - 1 stone = 4 jun
   - 1 jun = 30 jin
   - 1 jin = 16 liang
   - 1 liang = 24 zhu
2. Calculate the total weight in the smallest unit (zhu).
3. Calculate the price per unit weight for each category by dividing the total money by the total weight in that category.
4. If there is a remainder (not divisible), adjust according to the rules provided.

### Python Code:


"""

#----- content starts here -----

from fractions import Fraction

# Total money spent
total_money = 13970

# Silk weight: 1 stone, 2 jun, 28 jin, 3 liang, 5 zhu
stone = 1
jun = 2
jin = 28
liang = 3
zhu = 5

# Conversion factors
jun_per_stone = 4
jin_per_jun = 30
liang_per_jin = 16
zhu_per_liang = 24

# Convert everything to zhu (smallest unit)
total_zhu = (
    stone * jun_per_stone * jin_per_jun * liang_per_jin * zhu_per_liang +
    jun * jin_per_jun * liang_per_jin * zhu_per_liang +
    jin * liang_per_jin * zhu_per_liang +
    liang * zhu_per_liang +
    zhu
)

# Calculate price per zhu
price_per_zhu = Fraction(total_money, total_zhu)

# Convert price per zhu to other units
price_per_liang = price_per_zhu * zhu_per_liang
price_per_jin = price_per_liang * liang_per_jin
price_per_jun = price_per_jin * jin_per_jun
price_per_stone = price_per_jun * jun_per_stone

# Results
a = price_per_stone  # Price per stone
b = price_per_liang  # Price per liang
c = price_per_jun    # Price per jun
d = price_per_jin    # Price per jin

# Output the results
print(f"Price per stone: {a} money")
print(f"Price per liang: {b} money")
print(f"Price per jun: {c} money")
print(f"Price per jin: {d} money")
#----- content ends here -----


"""


### Explanation of the Code:
1. **Conversion to Zhu:** All weights are converted to the smallest unit (zhu) for accurate calculations.
2. **Price per Zhu:** The total money is divided by the total weight in zhu to get the price per zhu.
3. **Conversion Back:** The price per zhu is multiplied by the conversion factors to get the price per larger unit (liang, jin, jun, stone).
4. **Fraction Class:** The `Fraction` class is used to ensure precise calculations without floating-point errors.

### Example Output:
If you run the code, it will calculate the price per stone, jun, jin, and liang based on the given input.
"""


"""
Variable 'a' has wrong value. Expected: 12893/9216, Actual: 643737600/79949
Variable 'b' has wrong value. Expected: 4, Actual: 335280/79949
Variable 'c' has wrong value. Expected: 3871/2880, Actual: 160934400/79949
Variable 'd' has wrong value. Expected: 5, Actual: 5364480/79949"""
