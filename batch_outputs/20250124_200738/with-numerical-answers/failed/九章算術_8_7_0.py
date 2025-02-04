"""
今有賣牛二、羊五，以買十三豕，有餘錢一千。賣牛三、豕三，以買九羊，錢適足。賣羊六、豕八，以買五牛，錢不足六百。問︰牛、羊、豕價各幾何？
術曰：如方程，置牛二、羊五正，豕一十三負，餘錢數正；次牛三正，羊九負，豕三正；次牛五負，羊六正，豕八正，不足錢負。以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：牛價 a(=1200) ，羊價 b(=500) ，豕價 c(=300) 。
"""

#----- content starts here -----
To solve this problem, we will use the ancient Chinese method of solving simultaneous linear equations, as described in the "方程術" (method of solving systems of equations). The problem involves three unknowns: the price of a cow (牛價), the price of a sheep (羊價), and the price of a pig (豕價). These are represented as \(a\), \(b\), and \(c\), respectively.

The problem provides three equations based on the transactions:

1. \(2a + 5b - 13c = 1000\)
2. \(3a - 9b + 3c = 0\)
3. \(-5a + 6b + 8c = -600\)

We will solve these equations step by step using the described method.

---

### Step 1: Represent the equations in matrix form
We represent the equations in a matrix form for clarity:

\[
\begin{bmatrix}
2 & 5 & -13 & 1000 \\
3 & -9 & 3 & 0 \\
-5 & 6 & 8 & -600
\end{bmatrix}
\]

---

### Step 2: Eliminate the first variable (\(a\)) from the second and third rows
We use the first row to eliminate \(a\) from the second and third rows.

#### Eliminate \(a\) from the second row:
Multiply the first row by \(3\) and subtract \(2\) times the second row:
\[
3 \times [2, 5, -13, 1000] - 2 \times [3, -9, 3, 0]
\]
\[
[6, 15, -39, 3000] - [6, -18, 6, 0] = [0, 33, -45, 3000]
\]

#### Eliminate \(a\) from the third row:
Multiply the first row by \(5\) and add it to \(2\) times the third row:
\[
5 \times [2, 5, -13, 1000] + 2 \times [-5, 6, 8, -600]
\]
\[
[10, 25, -65, 5000] + [-10, 12, 16, -1200] = [0, 37, -49, 3800]
\]

The updated matrix is:
\[
\begin{bmatrix}
2 & 5 & -13 & 1000 \\
0 & 33 & -45 & 3000 \\
0 & 37 & -49 & 3800
\end{bmatrix}
\]

---

### Step 3: Eliminate the second variable (\(b\)) from the third row
We use the second row to eliminate \(b\) from the third row.

Multiply the second row by \(37\) and subtract \(33\) times the third row:
\[
37 \times [0, 33, -45, 3000] - 33 \times [0, 37, -49, 3800]
\]
\[
[0, 1221, -1665, 111000] - [0, 1221, -1617, 125400] = [0, 0, -48, -14400]
\]

The updated matrix is:
\[
\begin{bmatrix}
2 & 5 & -13 & 1000 \\
0 & 33 & -45 & 3000 \\
0 & 0 & -48 & -14400
\end{bmatrix}
\]

---

### Step 4: Solve for the variables
#### Solve for \(c\):
From the third row:
\[
-48c = -14400 \implies c = \frac{-14400}{-48} = 300
\]

#### Solve for \(b\):
Substitute \(c = 300\) into the second row:
\[
33b - 45c = 3000 \implies 33b - 45(300) = 3000
\]
\[
33b - 13500 = 3000 \implies 33b = 16500 \implies b = \frac{16500}{33} = 500
\]

#### Solve for \(a\):
Substitute \(b = 500\) and \(c = 300\) into the first row:
\[
2a + 5b - 13c = 1000 \implies 2a + 5(500) - 13(300) = 1000
\]
\[
2a + 2500 - 3900 = 1000 \implies 2a - 1400 = 1000 \implies 2a = 2400 \implies a = \frac{2400}{2} = 1200
\]

---

### Final Answer:
\[
\text{牛價 (price of a cow)} = a = 1200
\]
\[
\text{羊價 (price of a sheep)} = b = 500
\]
\[
\text{豕價 (price of a pig)} = c = 300
\]#----- content ends here -----

"""
Code error: invalid syntax (<string>, line 2)"""
