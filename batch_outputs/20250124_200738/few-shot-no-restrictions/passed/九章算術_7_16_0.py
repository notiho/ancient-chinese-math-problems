"""
今有善田一畝，價三百；惡田七畝，價五百。今并買一頃，價錢一萬。問︰善、惡田各幾何？
術曰：假令善田二十畝，惡田八十畝，多一千七百一十四錢、七分錢之二。令之善田一十畝，惡田九十畝，不足五百七十一錢、七分錢之三。
盈不足術曰：置所出率，盈、不足各居其下。令維乘所出率，并以為實。并盈、不足為法。實如法而一。有分者，通之。盈不足相與同其買物者，置所出率，以少減多，餘，以約法、實。實為物價，法為人數。
荅曰：善田 a畝 ，惡田 b畝 。
"""

"""
This is a classic "Excess and Deficiency" (盈不足) problem from ancient Chinese mathematics. Let's break it down and solve it step by step using Python.

### Problem:
- The price of 1 mu of good land (善田) is 300 coins.
- The price of 1 mu of poor land (惡田) is 500/7 coins (since 7 mu of poor land costs 500 coins).
- A total of 1 qing (100 mu) of land is purchased for 10,000 coins.
- Question: How many mu of good land and poor land are purchased?

### Procedure:
1. Assume two scenarios:
   - In the first scenario, assume 20 mu of good land and 80 mu of poor land. The total cost exceeds 10,000 coins by 1714 2/7 coins.
   - In the second scenario, assume 10 mu of good land and 90 mu of poor land. The total cost falls short of 10,000 coins by 571 3/7 coins.
2. Use the "Excess and Deficiency" method to solve for the actual number of mu of good and poor land.

---

### Python Code:


"""

#----- content starts here -----

from fractions import Fraction

# Prices
善田價 = 300  # Price per mu of good land
惡田價 = Fraction(500, 7)  # Price per mu of poor land

# Total land and total price
總畝數 = 100  # 1 qing = 100 mu
總價 = 10000  # Total price in coins

# Assumptions and their results
# First assumption: 20 mu of good land, 80 mu of poor land
善田_假設1 = 20
惡田_假設1 = 總畝數 - 善田_假設1
總價_假設1 = 善田_假設1 * 善田價 + 惡田_假設1 * 惡田價
盈 = 總價_假設1 - 總價  # Excess: 1714 2/7 coins
盈 = Fraction(1714) + Fraction(2, 7)

# Second assumption: 10 mu of good land, 90 mu of poor land
善田_假設2 = 10
惡田_假設2 = 總畝數 - 善田_假設2
總價_假設2 = 善田_假設2 * 善田價 + 惡田_假設2 * 惡田價
不足 = 總價 - 總價_假設2  # Deficiency: 571 3/7 coins
不足 = Fraction(571) + Fraction(3, 7)

# Excess and Deficiency method
# 盈不足術: (盈 * 假設2 - 不足 * 假設1) / (盈 - 不足)
善田 = (盈 * 善田_假設2 + 不足 * 善田_假設1) / (盈 + 不足)
惡田 = 總畝數 - 善田

# Output the results
a = 善田
b = 惡田

print(f"善田: {a} 畝")
print(f"惡田: {b} 畝")
#----- content ends here -----


"""


---

### Explanation of the Code:
1. **Prices and Assumptions**:
   - The price per mu of good land and poor land is defined.
   - Two assumptions are made about the distribution of good and poor land.

2. **Calculate Excess and Deficiency**:
   - For each assumption, calculate the total price and determine whether it exceeds or falls short of the target price (10,000 coins).

3. **Apply the Excess and Deficiency Method**:
   - Use the formula from the "Excess and Deficiency" method to calculate the actual number of mu of good land and poor land.

4. **Output**:
   - The results are printed as the number of mu of good land (`a`) and poor land (`b`).

---

### Answer:
The program will calculate and output the values of `a` (善田, good land) and `b` (惡田, poor land) in mu.
"""


"""
"""
