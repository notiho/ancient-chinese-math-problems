"""
今有善田一畝，價三百；惡田七畝，價五百。今并買一頃，價錢一萬。問︰善、惡田各幾何？
術曰：假令善田二十畝，惡田八十畝，多一千七百一十四錢、七分錢之二。令之善田一十畝，惡田九十畝，不足五百七十一錢、七分錢之三。
盈不足術曰：置所出率，盈、不足各居其下。令維乘所出率，并以為實。并盈、不足為法。實如法而一。有分者，通之。盈不足相與同其買物者，置所出率，以少減多，餘，以約法、實。實為物價，法為人數。荅曰：善田 a畝 ，惡田 b畝 。
"""

"""
This is a classic "Excess and Deficit" (盈不足) problem from ancient Chinese mathematics. Let's break it down and translate the procedure into Python code.

### Problem:
You have:
- Good land (善田) priced at 300 per mu.
- Poor land (惡田) priced at 500 per 7 mu.

You want to buy 1 qing (100 mu) of land for 10,000 coins. How much good land and poor land are included?

### Procedure:
1. Assume two scenarios:
   - Scenario 1: 20 mu of good land and 80 mu of poor land. This results in an excess of 1714 2/7 coins.
   - Scenario 2: 10 mu of good land and 90 mu of poor land. This results in a deficit of 571 3/7 coins.
2. Use the "Excess and Deficit" method to solve for the correct distribution of good and poor land.

### Translation into Python Code:


"""


from fractions import Fraction

# Prices and total land
善田價 = 300  # Price per mu of good land
惡田價 = Fraction(500, 7)  # Price per mu of poor land
總畝數 = 100  # Total land in mu
總價 = 10000  # Total price in coins

# Scenario 1: 20 mu of good land, 80 mu of poor land
善田1 = 20
惡田1 = 總畝數 - 善田1
價值1 = 善田1 * 善田價 + 惡田1 * 惡田價
盈 = 價值1 - 總價  # Excess coins

# Scenario 2: 10 mu of good land, 90 mu of poor land
善田2 = 10
惡田2 = 總畝數 - 善田2
價值2 = 善田2 * 善田價 + 惡田2 * 惡田價
不足 = 總價 - 價值2  # Deficit coins

# 盈不足術 calculation
盈 = Fraction(盈)  # Convert to fraction
不足 = Fraction(不足)  # Convert to fraction

# Place the rates (所出率)
所出率1 = 善田1 - 善田2
所出率2 = 惡田2 - 惡田1

# Multiply rates by excess and deficit, then sum
實 = 盈 * 所出率2 + 不足 * 所出率1

# Sum of excess and deficit
法 = 盈 + 不足

# Solve for善田
善田 = 實 / 法

# Solve for惡田
惡田 = 總畝數 - 善田

# Output results
a = 善田
b = 惡田

print(f"善田: {a} 畝, 惡田: {b} 畝")


"""


### Explanation:
1. **Scenario Assumptions**:
   - In the first scenario, we assume 20 mu of good land and calculate the excess coins.
   - In the second scenario, we assume 10 mu of good land and calculate the deficit coins.
2. **Excess and Deficit Method**:
   - Use the differences in land distribution (所出率) and the excess/deficit values to calculate the correct proportions.
3. **Final Calculation**:
   - Solve for the amount of good land (善田) and subtract it from the total to get the amount of poor land (惡田).

### Answer:
The values of `a` (善田) and `b` (惡田) will be printed as the solution in terms of mu.
"""


"""
Variable 'a' has wrong value. Expected: 25/2, Actual: 10
Variable 'b' has wrong value. Expected: 175/2, Actual: 90"""
