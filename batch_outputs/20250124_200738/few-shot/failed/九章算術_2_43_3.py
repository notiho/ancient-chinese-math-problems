"""
今有出錢一萬三千九百七十，買絲一石二鈞二十八斤三兩五銖。欲其貴賤銖率之，問︰各幾何？
反其率術曰：以錢數為法，所率為實，實如法而一。不滿法者反以實減法，法少，實多。二物各以所得多少之數乘法實，即物數。
荅曰：其 a鈞 ， b銖 一錢。 其 c石 ， d銖 一錢。
"""

"""
This problem involves calculating the price per unit weight of silk based on the total cost and the total weight. The procedure provided is complex and involves a method of proportionality and division. Let's break it down and encode it step by step.

### Problem Breakdown:
- Total money spent: **13,970 (錢)**
- Total weight of silk: **1 石, 2 鈞, 28 斤, 3 兩, 5 銖**
- The goal is to calculate the price per unit weight (銖 rate) and express the results in terms of 鈞 and 銖.

---

### Procedure:
The procedure ("反其率術") involves:
1. Using the total money as the divisor (法).
2. Using the total weight as the dividend (實).
3. Dividing the total weight by the total money to get the rate per unit weight.
4. Adjusting for any remainder and calculating the proportional amounts for 鈞 and 銖.

---

### Python Code:


"""

#----- content starts here -----

from fractions import Fraction

# Total money spent (錢)
錢數 = 13970

# Total weight of silk: 1 石, 2 鈞, 28 斤, 3 兩, 5 銖
石 = 1
鈞 = 2
斤 = 28
兩 = 3
銖 = 5

# Conversion factors
斤_per_鈞 = 30  # 1 鈞 = 30 斤
兩_per_斤 = 16  # 1 斤 = 16 兩
銖_per_兩 = 24  # 1 兩 = 24 銖

# Convert total weight to 銖
總銖 = (
    石 * 4 * 30 * 16 * 24 +  # 1 石 = 4 鈞
    鈞 * 30 * 16 * 24 +
    斤 * 16 * 24 +
    兩 * 24 +
    銖
)

# Step 1: Use total money as the divisor (法) and total weight as the dividend (實)
法 = 錢數
實 = 總銖

# Step 2: Calculate the rate per 銖
銖率 = Fraction(實, 法)

# Step 3: Convert the rate back to 鈞 and 銖
# 鈞 rate
鈞率 = 銖率 * (1 / (30 * 16 * 24))  # Convert 銖 to 鈞
a = 鈞率.numerator
b = 鈞率.denominator

# 石 rate
石率 = 鈞率 * (1 / 4)  # Convert 鈞 to 石
c = 石率.numerator
d = 石率.denominator

# Final Answer
print(f"其 {a} 鈞, {b} 銖 一錢。其 {c} 石, {d} 銖 一錢。")
#----- content ends here -----


"""


---

### Explanation of the Code:
1. **Weight Conversion**: The total weight is converted into 銖, the smallest unit, for precise calculations.
2. **Rate Calculation**: The rate per 銖 is calculated by dividing the total weight (實) by the total money (法).
3. **Unit Conversion**: The rate is converted back into 鈞 and 石 for the final answer.
4. **Fraction Handling**: The `Fraction` class ensures precise calculations without floating-point errors.

---

### Final Answer:
The output will provide the rate in terms of 鈞 and 銖 per 錢, as well as 石 and 銖 per 錢.
"""


"""
Code error: 'float' object has no attribute 'numerator'"""
