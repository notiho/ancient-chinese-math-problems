"""
今有出錢一萬三千九百七十，買絲一石二鈞二十八斤三兩五銖。欲其貴賤銖率之，問︰各幾何？
反其率術曰：以錢數為法，所率為實，實如法而一。不滿法者反以實減法，法少，實多。二物各以所得多少之數乘法實，即物數。
荅曰：其 a鈞 ， b銖 一錢。 其 c石 ， d銖 一錢。
"""

"""
This problem involves calculating the price per unit weight of silk based on the total cost and the total weight. Let's break it down step by step and translate it into Python code.

### Problem Breakdown:
1. **Given:**
   - Total money spent: 13,970 (in some monetary unit).
   - Total weight of silk: 1 **shi**, 2 **jun**, 28 **jin**, 3 **liang**, 5 **zhu**.

2. **Objective:**
   - Calculate the price per **zhu** (smallest unit of weight).

3. **Procedure:**
   - Convert the total weight into the smallest unit (**zhu**).
   - Divide the total money by the total weight in **zhu** to get the price per **zhu**.
   - Express the price in terms of **shi**, **jun**, **jin**, **liang**, and **zhu**.

---

### Python Code:


"""

#----- content starts here -----

from fractions import Fraction

# Total money spent
total_money = 13970

# Total weight of silk in various units
shi = 1
jun = 2
jin = 28
liang = 3
zhu = 5

# Conversion factors
shi_to_jin = 120  # 1 shi = 120 jin
jun_to_jin = 30   # 1 jun = 30 jin
jin_to_liang = 16 # 1 jin = 16 liang
liang_to_zhu = 24 # 1 liang = 24 zhu

# Convert total weight to zhu (smallest unit)
total_weight_in_zhu = (
    shi * shi_to_jin * jin_to_liang * liang_to_zhu +
    jun * jun_to_jin * jin_to_liang * liang_to_zhu +
    jin * jin_to_liang * liang_to_zhu +
    liang * liang_to_zhu +
    zhu
)

# Calculate the price per zhu
price_per_zhu = Fraction(total_money, total_weight_in_zhu)

# Convert the price per zhu back into shi, jun, jin, liang, and zhu
price_in_zhu = price_per_zhu
price_in_liang = price_in_zhu // liang_to_zhu
remaining_zhu = price_in_zhu % liang_to_zhu

price_in_jin = price_in_liang // jin_to_liang
remaining_liang = price_in_liang % jin_to_liang

price_in_jun = price_in_jin // jun_to_jin
remaining_jin = price_in_jin % jun_to_jin

price_in_shi = price_in_jun // shi_to_jin
remaining_jun = price_in_jun % shi_to_jin

# Final results
a = remaining_jin
b = remaining_zhu
c = price_in_shi
d = price_in_liang

# Output the results
print(f"其 {a} 鈞，{b} 銖 一錢。其 {c} 石，{d} 銖 一錢。")
#----- content ends here -----


"""


---

### Explanation of the Code:
1. **Weight Conversion:**
   - Convert all weight units into the smallest unit (**zhu**) for precise calculations.
   - Use the given conversion factors to calculate the total weight in **zhu**.

2. **Price Calculation:**
   - Divide the total money by the total weight in **zhu** to get the price per **zhu**.

3. **Unit Conversion:**
   - Convert the price per **zhu** back into larger units (**shi**, **jun**, **jin**, **liang**, **zhu**) for a more meaningful representation.

4. **Output:**
   - The results are expressed in terms of **shi**, **jun**, **jin**, **liang**, and **zhu**.

---

### Example Output:
If you run the code with the given inputs, it will calculate the price per **zhu** and express it in the desired format.
"""


"""
Variable 'a' has wrong value. Expected: 3871/2304, Actual: 0
Variable 'b' has wrong value. Expected: 5, Actual: 13970/79949
Variable 'c' has wrong value. Expected: 10099/7680, Actual: 0
Variable 'd' has wrong value. Expected: 6, Actual: 0"""
