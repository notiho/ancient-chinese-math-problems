"""
今有醇酒一斗，直錢五十；行酒一斗，直錢一十。今將錢三十，得酒二斗。問︰醇、行酒各得幾何？
術曰：假令醇酒五升，行酒一斗五升，有餘一十。令之醇酒二升，行酒一斗八升，不足二。
盈不足術曰：置所出率，盈、不足各居其下。令維乘所出率，并以為實。并盈、不足為法。實如法而一。有分者，通之。盈不足相與同其買物者，置所出率，以少減多，餘，以約法、實。實為物價，法為人數。荅曰：醇酒 a升 ，行酒 b斗 。
"""

To solve this problem, we will follow the "盈不足術" (Excess and Deficiency Method) step by step:

### Definitions:
- 醇酒 (pure wine): 1斗 = 10升, price = 50錢 per 斗.
- 行酒 (diluted wine): 1斗 = 10升, price = 10錢 per 斗.
- Total money: 30錢.
- Total wine: 2斗 = 20升.

We aim to determine how much of 醇酒 (a升) and 行酒 (b斗) are purchased.

---

### Step 1: Set up the problem
Assume:
- 醇酒 = \( x \) 升.
- 行酒 = \( y \) 升.

From the problem:
1. \( x + y = 20 \) (total wine is 20升).
2. \( 5x + y = 150 \) (total cost is 30錢, where 醇酒 costs 5錢/升 and 行酒 costs 1錢/升).

---

### Step 2: Solve the equations
From \( x + y = 20 \), we get \( y = 20 - x \).

Substitute \( y = 20 - x \) into \( 5x + y = 150 \):
\[
5x + (20 - x) = 150
\]
\[
5x + 20 - x = 150
\]
\[
4x + 20 = 150
\]
\[
4x = 130
\]
\[
x = 32.5
\]

Thus:
- \( x = 32.5 \) 升 (醇酒).
- \( y = 20 - x = 20 - 32.5 = -12.5 \) 升 (行酒).

---

### Step 3: Convert to the correct units
Since \( x \) and \( y \) are in 升:
- \( a = x = 32.5 \) 升 (醇酒).
- \( b = y / 10 = -12.5 / 10 = -1.25 \) 斗 (行酒).

---

### Final Answer:
- 醇酒 \( a = 32.5 \) 升.
- 行酒 \( b = -1.25 \) 斗.


"""
Code error: invalid decimal literal (<string>, line 5)"""
