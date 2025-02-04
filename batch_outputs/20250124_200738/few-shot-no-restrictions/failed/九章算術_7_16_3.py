"""
今有善田一畝，價三百；惡田七畝，價五百。今并買一頃，價錢一萬。問︰善、惡田各幾何？
術曰：假令善田二十畝，惡田八十畝，多一千七百一十四錢、七分錢之二。令之善田一十畝，惡田九十畝，不足五百七十一錢、七分錢之三。
盈不足術曰：置所出率，盈、不足各居其下。令維乘所出率，并以為實。并盈、不足為法。實如法而一。有分者，通之。盈不足相與同其買物者，置所出率，以少減多，餘，以約法、實。實為物價，法為人數。
荅曰：善田 a畝 ，惡田 b畝 。
"""

"""
This problem involves solving a system of equations using the "Excess and Deficiency" (盈不足) method, a classical Chinese mathematical technique. Let's break it down step by step and implement it in Python.

### Problem Explanation:
- The price of 1 mu of good (善) land is 300.
- The price of 1 mu of poor (惡) land is 500/7 (since 7 mu of poor land costs 500).
- A total of 1 qing (100 mu) of land is purchased for 10,000.
- We need to determine how many mu of good land and poor land are included in the purchase.

### Steps:
1. Assume two hypothetical scenarios:
   - Scenario 1: 20 mu of good land and 80 mu of poor land. This results in an excess of **1714 2/7** coins.
   - Scenario 2: 10 mu of good land and 90 mu of poor land. This results in a deficit of **571 3/7** coins.
2. Use the "Excess and Deficiency" method to solve for the actual amounts of good and poor land.

---

### Python Implementation:


"""

#----- content starts here -----

from fractions import Fraction

# Prices
善田價 = 300  # Price per mu of good land
惡田價 = Fraction(500, 7)  # Price per mu of poor land

# Total land and total price
總地 = 100  # 1 qing = 100 mu
總價 = 10000

# Hypothetical scenarios
# Scenario 1: 20 mu of good land, 80 mu of poor land
善田_假設1 = 20
惡田_假設1 = 總地 - 善田_假設1
價差_假設1 = Fraction(1714, 1) + Fraction(2, 7)  # Excess

# Scenario 2: 10 mu of good land, 90 mu of poor land
善田_假設2 = 10
惡田_假設2 = 總地 - 善田_假設2
價差_假設2 = -(Fraction(571, 1) + Fraction(3, 7))  # Deficit

# "Excess and Deficiency" method
# Step 1: Calculate the rates (所出率)
率1 = 善田_假設1 * 善田價 + 惡田_假設1 * 惡田價
率2 = 善田_假設2 * 善田價 + 惡田_假設2 * 惡田價

# Step 2: Multiply rates by their respective differences
實1 = 率1 * abs(價差_假設2)
實2 = 率2 * abs(價差_假設1)

# Step 3: Add the results to form the numerator and denominator
法 = abs(價差_假設1) + abs(價差_假設2)
實 = 實1 + 實2

# Step 4: Solve for the amount of good land
善田 = 實 / 法

# Step 5: Solve for the amount of poor land
惡田 = 總地 - 善田

# Output the results
a = 善田
b = 惡田

print(f"善田: {a} 畝")
print(f"惡田: {b} 畝")
#----- content ends here -----


"""


---

### Explanation of the Code:
1. **Prices and Inputs**:
   - The price of good land (`善田價`) is 300 per mu.
   - The price of poor land (`惡田價`) is calculated as 500/7 per mu.
   - The total land (`總地`) is 100 mu, and the total price (`總價`) is 10,000.

2. **Hypothetical Scenarios**:
   - Two scenarios are assumed, with their respective excess or deficit in price.

3. **Excess and Deficiency Method**:
   - The rates (`率1` and `率2`) are calculated based on the hypothetical scenarios.
   - The differences (`實1` and `實2`) are multiplied by the respective excess or deficit.
   - The total (`實`) and divisor (`法`) are calculated.
   - The amount of good land (`善田`) is solved, and the amount of poor land (`惡田`) is derived.

4. **Output**:
   - The results are printed as the number of mu of good and poor land.

---

### Final Answer:
The program will output the values of `a` (善田) and `b` (惡田) in mu.
"""


"""
Variable 'a' has wrong value. Expected: 25/2, Actual: 10000
Variable 'b' has wrong value. Expected: 175/2, Actual: -9900"""
