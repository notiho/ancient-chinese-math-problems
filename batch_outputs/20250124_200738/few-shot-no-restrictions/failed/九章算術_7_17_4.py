"""
今有黃金九枚，白銀一十一枚，稱之重適等。交易其一，金輕十三兩。問︰金、銀一枚各重幾何？
術曰：假令黃金三斤，白銀二斤、一十一分斤之五，不足四十九，於右行。令之黃金二斤，白銀一斤、一十一分斤之七，多一十五於左行。以分母各乘其行內之數，以盈不足維乘所出率，并以為實。并盈不足為法。實如法，得黃金重。分母乘法以除，得銀重。約之得分也。
荅曰：金重 a斤 ，銀重 b斤 。
"""

"""
This is a classic problem involving proportional weights of gold and silver, where their weights are balanced, and the problem seeks to determine the weight of one piece of gold and one piece of silver. Let's translate the procedure into Python code step by step.

---

### Problem Breakdown:
- There are **9 pieces of gold** and **11 pieces of silver**, and their total weights are equal.
- If one gold piece is traded for one silver piece, the gold becomes lighter by **13 liang**.
- We are tasked to find the weight of **one piece of gold** and **one piece of silver**.

---

### Procedure:
1. Assume hypothetical weights for gold and silver:
   - Let gold weigh `3 jin` per piece.
   - Let silver weigh `2 jin + 5/11 jin` per piece.
2. Check the balance:
   - If the total weight of gold is less than the total weight of silver, adjust the weights.
   - If the total weight of gold is more than the total weight of silver, adjust the weights.
3. Use the given proportions and relationships to calculate the exact weights.

---

Here is the Python implementation:


"""

#----- content starts here -----

from fractions import Fraction

# Initial data
金枚數 = 9  # Number of gold pieces
銀枚數 = 11  # Number of silver pieces
金輕 = 13  # Gold becomes lighter by 13 liang when traded

# Step 1: Assume initial weights
# 假令黃金三斤，白銀二斤、一十一分斤之五
金假重 = Fraction(3)  # 3 jin
銀假重 = Fraction(2) + Fraction(5, 11)  # 2 jin + 5/11 jin

# Calculate the total weights for the initial assumption
金總重 = 金枚數 * 金假重
銀總重 = 銀枚數 * 銀假重

# Step 2: Adjust weights based on the imbalance
# 假令黃金二斤，白銀一斤、一十一分斤之七
金調整重 = Fraction(2)  # 2 jin
銀調整重 = Fraction(1) + Fraction(7, 11)  # 1 jin + 7/11 jin

# Calculate the total weights for the adjusted assumption
金調整總重 = 金枚數 * 金調整重
銀調整總重 = 銀枚數 * 銀調整重

# Step 3: Calculate the difference (盈不足)
盈 = 銀總重 - 金總重  # Excess in the first assumption
不足 = 金調整總重 - 銀調整總重  # Deficit in the second assumption

# Step 4: Calculate the final weights
# 分母各乘其行內之數，以盈不足維乘所出率，并以為實
金重實 = 銀假重 * 不足 + 銀調整重 * 盈
銀重實 = 金假重 * 不足 + 金調整重 * 盈

# 并盈不足为法
法 = 盈 + 不足

# 实如法，得黄金重
金重 = 金重實 / 法

# 分母乘法以除，得银重
銀重 = 銀重實 / 法

# Simplify the results
a = 金重
b = 銀重

# Output the results
print(f"金重: {a} 斤")
print(f"銀重: {b} 斤")
#----- content ends here -----


"""


---

### Explanation of the Code:
1. **Initial Assumptions**:
   - Start with hypothetical weights for gold and silver.
   - Calculate the total weights for both metals under these assumptions.

2. **Adjustments**:
   - Use a second set of hypothetical weights to calculate the imbalance (盈 and 不足).

3. **Final Calculation**:
   - Use the proportions of the imbalance to calculate the exact weights of gold and silver.

---

### Answer:
The program will output the weights of one piece of gold (`a`) and one piece of silver (`b`) in jin.
"""


"""
Code error: Fraction(0, 0)"""
