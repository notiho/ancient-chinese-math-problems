"""
今有善田一畝，價三百；惡田七畝，價五百。今并買一頃，價錢一萬。問︰善、惡田各幾何？
術曰：假令善田二十畝，惡田八十畝，多一千七百一十四錢、七分錢之二。令之善田一十畝，惡田九十畝，不足五百七十一錢、七分錢之三。
盈不足術曰：置所出率，盈、不足各居其下。令維乘所出率，并以為實。并盈、不足為法。實如法而一。有分者，通之。盈不足相與同其買物者，置所出率，以少減多，餘，以約法、實。實為物價，法為人數。
荅曰：善田 a畝 ，惡田 b畝 。
"""

"""
This is a classic "excess and deficiency" (盈不足) problem from ancient Chinese mathematics. The problem involves determining how much of two types of land (善田, good land, and 惡田, poor land) are purchased when the total cost and total area are known, but the prices per unit area differ.

Let's break this down step by step and encode the solution in Python:

---

### Problem:
- Good land (善田) costs 300 per mu.
- Poor land (惡田) costs 500 for 7 mu (or approximately 71.43 per mu).
- A total of 1 qing (100 mu) is purchased for 10,000.
- Determine how many mu of good land and poor land are purchased.

---

### Solution:
We use the "excess and deficiency" (盈不足) method to solve this.

1. Assume two hypothetical scenarios:
   - Case 1: Assume 20 mu of good land and 80 mu of poor land. The total cost exceeds the target by 1714.2857 (or \(1714 \frac{2}{7}\)).
   - Case 2: Assume 10 mu of good land and 90 mu of poor land. The total cost falls short of the target by 571.4286 (or \(571 \frac{3}{7}\)).

2. Use the excess and deficiency method:
   - Place the "excess" (盈) and "deficiency" (不足) under their respective assumptions.
   - Multiply the assumptions by the opposite rates of excess/deficiency.
   - Combine the results to find the true solution.

---

### Python Code:


"""

#----- content starts here -----

from fractions import Fraction

# Prices and total cost
善田價 = 300  # Good land price per mu
惡田價 = Fraction(500, 7)  # Poor land price per mu
總價 = 10000  # Total price
總畝 = 100  # Total area in mu

# Case 1: Assume 20 mu of good land, 80 mu of poor land
善田_假設1 = 20
惡田_假設1 = 總畝 - 善田_假設1
總價_假設1 = 善田_假設1 * 善田價 + 惡田_假設1 * 惡田價
盈 = 總價_假設1 - 總價  # Excess

# Case 2: Assume 10 mu of good land, 90 mu of poor land
善田_假設2 = 10
惡田_假設2 = 總畝 - 善田_假設2
總價_假設2 = 善田_假設2 * 善田價 + 惡田_假設2 * 惡田價
不足 = 總價 - 総價_假設2  # Deficiency

# Use the excess and deficiency method
法 = 盈 + 不足  # Combine excess and deficiency
實 = 不足 * 善田_假設1 + 盈 * 善田_假設2  # Multiply assumptions by opposite rates

# Solve for the true amount of good land
善田 = Fraction(實, 法)

# Solve for the true amount of poor land
惡田 = 總畝 - 善田

# Output the results
a = 善田
b = 惡田

print(f"善田: {a} 畝")
print(f"惡田: {b} 畝")
#----- content ends here -----


"""


---

### Explanation of the Code:
1. We calculate the total cost for each assumption (20 mu of good land, 10 mu of good land).
2. We compute the excess (盈) and deficiency (不足) relative to the target total cost.
3. Using the "excess and deficiency" method, we combine the assumptions to find the true solution.
4. The results are expressed as fractions for precision.

---

### Final Answer:
The output will provide the number of mu of good land (善田) and poor land (惡田) purchased.
"""


"""
Code error: name '総價_假設2' is not defined"""
