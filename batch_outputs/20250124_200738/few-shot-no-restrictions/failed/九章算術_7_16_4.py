"""
今有善田一畝，價三百；惡田七畝，價五百。今并買一頃，價錢一萬。問︰善、惡田各幾何？
術曰：假令善田二十畝，惡田八十畝，多一千七百一十四錢、七分錢之二。令之善田一十畝，惡田九十畝，不足五百七十一錢、七分錢之三。
盈不足術曰：置所出率，盈、不足各居其下。令維乘所出率，并以為實。并盈、不足為法。實如法而一。有分者，通之。盈不足相與同其買物者，置所出率，以少減多，餘，以約法、實。實為物價，法為人數。
荅曰：善田 a畝 ，惡田 b畝 。
"""

"""
This is a classic "excess and deficiency" (盈不足) problem, where we solve for the number of units of two types of land (善田 and 惡田) based on their prices and total cost. Let's break it down and solve it step by step in Python.

---

### Problem Breakdown:
1. **Given:**
   - The price of 1 mu of good land (善田) is 300.
   - The price of 1 mu of poor land (惡田) is \( \frac{500}{7} \) (since 7 mu of poor land costs 500).
   - The total land purchased is 1 qing (100 mu).
   - The total cost is 10,000.

2. **Assumptions:**
   - First assumption: 20 mu of good land and 80 mu of poor land.
     - Total cost = \( 20 \times 300 + 80 \times \frac{500}{7} \).
     - This exceeds the total cost by \( 1714 \frac{2}{7} \).
   - Second assumption: 10 mu of good land and 90 mu of poor land.
     - Total cost = \( 10 \times 300 + 90 \times \frac{500}{7} \).
     - This is short of the total cost by \( 571 \frac{3}{7} \).

3. **Excess and Deficiency Method:**
   - Use the excess and deficiency method to solve for the actual number of mu of good and poor land.

---

### Python Code Implementation:


"""

#----- content starts here -----

from fractions import Fraction

# Prices
善田價 = 300  # Price per mu of good land
惡田價 = Fraction(500, 7)  # Price per mu of poor land

# Total land and total cost
總地 = 100  # 1 qing = 100 mu
總價 = 10000

# Assumptions
# First assumption: 20 mu of good land, 80 mu of poor land
善田_假1 = 20
惡田_假1 = 總地 - 善田_假1
總價_假1 = 善田_假1 * 善田價 + 惡田_假1 * 惡田價
盈 = 總價_假1 - 總價  # Excess: 1714 2/7

# Second assumption: 10 mu of good land, 90 mu of poor land
善田_假2 = 10
惡田_假2 = 總地 - 善田_假2
總價_假2 = 善田_假2 * 善田價 + 惡田_假2 * 惡田價
不足 = 總價 - 総價_假2  # Deficiency: 571 3/7

# Excess and Deficiency Method
盈 = Fraction(1714, 1) + Fraction(2, 7)  # Convert to improper fraction
不足 = Fraction(571, 1) + Fraction(3, 7)  # Convert to improper fraction

# Calculate the actual number of good land (善田)
法 = 盈 + 不足  # Combine excess and deficiency
實 = 善田_假1 * 不足 + 善田_假2 * 盈  # Multiply assumptions by the opposite rates
善田 = 實 / 法  # Actual good land

# Calculate the actual number of poor land (惡田)
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
1. **Prices and Assumptions:**
   - The price per mu of good and poor land is defined.
   - Two assumptions are made for the distribution of land.

2. **Excess and Deficiency:**
   - The excess and deficiency values are calculated based on the assumptions.

3. **Excess and Deficiency Method:**
   - The formula for the method is applied:
     \[
     \text{Actual善田} = \frac{\text{善田假1} \times \text{不足} + \text{善田假2} \times \text{盈}}{\text{盈} + \text{不足}}
     \]
   - The remaining land is assigned to poor land (惡田).

4. **Output:**
   - The results are printed as the number of mu of good and poor land.

---

### Final Answer:
The code will calculate the exact values of \( a \) (善田) and \( b \) (惡田) in mu.
"""


"""
Code error: name '総價_假2' is not defined"""
