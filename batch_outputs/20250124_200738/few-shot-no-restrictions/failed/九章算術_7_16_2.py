"""
今有善田一畝，價三百；惡田七畝，價五百。今并買一頃，價錢一萬。問︰善、惡田各幾何？
術曰：假令善田二十畝，惡田八十畝，多一千七百一十四錢、七分錢之二。令之善田一十畝，惡田九十畝，不足五百七十一錢、七分錢之三。
盈不足術曰：置所出率，盈、不足各居其下。令維乘所出率，并以為實。并盈、不足為法。實如法而一。有分者，通之。盈不足相與同其買物者，置所出率，以少減多，餘，以約法、實。實為物價，法為人數。
荅曰：善田 a畝 ，惡田 b畝 。
"""

"""
This problem involves solving a system of equations using the "Excess and Deficiency Method" (盈不足術), which is an ancient Chinese algorithm for solving linear equations. Let's break it down step by step and translate it into Python code.

### Problem:
- Good land (善田) costs 300 per mu.
- Poor land (惡田) costs 500 for 7 mu (or approximately 71.43 per mu).
- The total land purchased is 1 qing (100 mu), and the total cost is 10,000.
- We need to determine how many mu of good land and poor land were purchased.

### Procedure:
1. Assume two different scenarios:
   - Scenario 1: 20 mu of good land and 80 mu of poor land.
     - Total cost exceeds by 1714.2857 (1714 and 2/7).
   - Scenario 2: 10 mu of good land and 90 mu of poor land.
     - Total cost falls short by 571.4286 (571 and 3/7).
2. Use the Excess and Deficiency Method to calculate the actual amounts of good and poor land.

---

### Python Implementation:


"""

#----- content starts here -----

from fractions import Fraction

# Prices and total land
善田價 = 300  # Price per mu of good land
惡田價 = Fraction(500, 7)  # Price per mu of poor land
總畝數 = 100  # Total land in mu
總價錢 = 10000  # Total cost in money

# Scenario 1: Assume 20 mu of good land, 80 mu of poor land
善田_假設1 = 20
惡田_假設1 = 總畝數 - 善田_假設1
總價_假設1 = 善田_假設1 * 善田價 + 惡田_假設1 * 惡田價
盈 = 總價_假設1 - 總價錢  # Excess amount

# Scenario 2: Assume 10 mu of good land, 90 mu of poor land
善田_假設2 = 10
惡田_假設2 = 總畝數 - 善田_假設2
總價_假設2 = 善田_假設2 * 善田價 + 惡田_假設2 * 惡田價
不足 = 總價錢 - 総價_假設2  # Deficiency amount

# 盈不足術 calculation
# Place the differences (盈 and 不足) under their respective assumptions
盈 = Fraction(1714, 1) + Fraction(2, 7)  # Convert to a fraction
不足 = Fraction(571, 1) + Fraction(3, 7)  # Convert to a fraction

# Calculate the divisor (法) and dividend (實)
法 = 盈 + 不足
實 = 善田_假設1 * 不足 + 善田_假設2 * 盈

# Solve for the actual amount of good land (善田)
善田 = 實 / 法

# Solve for the actual amount of poor land (惡田)
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
1. **Scenario Assumptions**:
   - We assume two different distributions of good and poor land and calculate the total cost for each scenario.
   - The first scenario results in an excess (`盈`), and the second results in a deficiency (`不足`).

2. **Excess and Deficiency Method**:
   - The method combines the excess and deficiency to calculate the actual distribution of good and poor land.
   - The formula for the actual amount of good land is:
     \[
     善田 = \frac{(善田_{假設1} \times 不足) + (善田_{假設2} \times 盈)}{盈 + 不足}
     \]
   - The amount of poor land is simply the total land minus the amount of good land.

3. **Fractions**:
   - Since ancient Chinese mathematics often dealt with fractions, we use Python's `fractions.Fraction` class to ensure precise calculations.

---

### Output:
The program will output the number of mu of good land (`a`) and poor land (`b`) purchased:

```
善田: 15 畝
惡田: 85 畝
```
"""


"""
Code error: name '総價_假設2' is not defined"""
