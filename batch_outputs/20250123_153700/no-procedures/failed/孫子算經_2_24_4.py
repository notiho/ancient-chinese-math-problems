"""
今有甲乙丙三人持錢，甲語乙丙：各將公等所持錢半以益我錢成九十。乙復語甲丙：各將公等所持錢，半以益我，錢成七十。丙復語甲乙：各將公等所持錢，半以益我，錢成五十六。問：三人元持錢各若干？
答曰：甲 a ，乙 b ，丙 c 。
"""

This problem involves solving a system of equations based on the statements made by three individuals, where each person receives half of the money held by the other two and their total money becomes a specific amount. Let's break it down and solve it step by step.

### Problem:
- **Person A (甲)** says: "If each of you (乙 and 丙) gives me half of your money, I will have 90."
- **Person B (乙)** says: "If each of you (甲 and 丙) gives me half of your money, I will have 70."
- **Person C (丙)** says: "If each of you (甲 and 乙) gives me half of your money, I will have 56."

We need to find how much money each person originally had: \( a \) (甲), \( b \) (乙), and \( c \) (丙).

---

### Solution:
Let \( a \), \( b \), and \( c \) represent the original amounts of money held by 甲, 乙, and 丙, respectively.

From the problem, we can write the following equations:

1. \( a + \frac{b}{2} + \frac{c}{2} = 90 \)
2. \( b + \frac{a}{2} + \frac{c}{2} = 70 \)
3. \( c + \frac{a}{2} + \frac{b}{2} = 56 \)

Rewriting these equations to eliminate fractions:

1. \( 2a + b + c = 180 \)
2. \( 2b + a + c = 140 \)
3. \( 2c + a + b = 112 \)

Now we solve this system of linear equations.

---

### Step 1: Add all three equations together
\[
(2a + b + c) + (2b + a + c) + (2c + a + b) = 180 + 140 + 112
\]
\[
4a + 4b + 4c = 432
\]
\[
a + b + c = 108 \tag{4}
\]

---

### Step 2: Solve for individual variables
From equation (4), substitute \( c = 108 - a - b \) into the first two equations.

#### Substitute into the first equation:
\[
2a + b + (108 - a - b) = 180
\]
\[
2a + b + 108 - a - b = 180
\]
\[
a = 72 \tag{5}
\]

#### Substitute \( a = 72 \) into the second equation:
\[
2b + 72 + (108 - 72 - b) = 140
\]
\[
2b + 72 + 108 - 72 - b = 140
\]
\[
b = 40 \tag{6}
\]

#### Substitute \( a = 72 \) and \( b = 40 \) into equation (4):
\[
c = 108 - 72 - 40
\]
\[
c = 36 \tag{7}
\]

---

### Final Answer:
\[
\text{甲 (a)} = 72, \quad \text{乙 (b)} = 40, \quad \text{丙 (c)} = 36
\]
"""
Code error: unterminated string literal (detected at line 2) (<string>, line 2)"""
