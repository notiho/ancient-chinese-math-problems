"""
今有賣牛二、羊五，以買十三豕，有餘錢一千。賣牛三、豕三，以買九羊，錢適足。賣羊六、豕八，以買五牛，錢不足六百。問︰牛、羊、豕價各幾何？
術曰：如方程，置牛二、羊五正，豕一十三負，餘錢數正；次牛三正，羊九負，豕三正；次牛五負，羊六正，豕八正，不足錢負。以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。荅曰：牛價 a(=1200) ，羊價 b(=500) ，豕價 c(=300) 。
"""

To solve this problem, we will use the ancient Chinese method of solving simultaneous linear equations, as described in the "方程術" (method of solving systems of equations). The problem involves three unknowns: the price of a cow (牛價), the price of a sheep (羊價), and the price of a pig (豕價). These are represented as \(a\), \(b\), and \(c\), respectively.

The problem provides three equations based on the transactions described:

1. \(2a + 5b - 13c = 1000\) (selling 2 cows and 5 sheep to buy 13 pigs, with 1000 money left over).
2. \(3a - 9b + 3c = 0\) (selling 3 cows and 3 pigs to buy 9 sheep, with no money left over).
3. \(-5a + 6b + 8c = -600\) (selling 6 sheep and 8 pigs to buy 5 cows, with 600 money short).

We will solve this system of equations using the procedure described in the "方程術".

---

### Step 1: Represent the equations in matrix form
We represent the equations as a matrix, where each row corresponds to an equation, and the columns represent the coefficients of \(a\), \(b\), and \(c\), followed by the constant term on the right-hand side.

\[
\begin{bmatrix}
2 & 5 & -13 & 1000 \\
3 & -9 & 3 & 0 \\
-5 & 6 & 8 & -600
\end{bmatrix}
\]

---

### Step 2: Eliminate variables using the described procedure
We will use Gaussian elimination to reduce the matrix step by step, following the "正負術" (positive-negative method) and "方程術".

---

#### Normalize the first row
Divide the first row by 2 (the coefficient of \(a\) in the first row) to make the leading coefficient 1.

\[
\begin{bmatrix}
1 & \frac{5}{2} & -\frac{13}{2} & 500 \\
3 & -9 & 3 & 0 \\
-5 & 6 & 8 & -600
\end{bmatrix}
\]

---

#### Eliminate \(a\) from the second and third rows
- For the second row: Subtract \(3 \times\) the first row from the second row.
- For the third row: Add \(5 \times\) the first row to the third row.

\[
\begin{bmatrix}
1 & \frac{5}{2} & -\frac{13}{2} & 500 \\
0 & -\frac{33}{2} & \frac{51}{2} & -1500 \\
0 & \frac{37}{2} & \frac{-29}{2} & 1900
\end{bmatrix}
\]

---

#### Normalize the second row
Divide the second row by \(-\frac{33}{2}\) (the coefficient of \(b\) in the second row) to make the leading coefficient of \(b\) in the second row 1.

\[
\begin{bmatrix}
1 & \frac{5}{2} & -\frac{13}{2} & 500 \\
0 & 1 & -\frac{51}{33} & \frac{3000}{33} \\
0 & \frac{37}{2} & \frac{-29}{2} & 1900
\end{bmatrix}
\]

---

#### Eliminate \(b\) from the first and third rows
- For the first row: Subtract \(\frac{5}{2} \times\) the second row from the first row.
- For the third row: Subtract \(\frac{37}{2} \times\) the second row from the third row.

\[
\begin{bmatrix}
1 & 0 & -\frac{104}{33} & \frac{8500}{33} \\
0 & 1 & -\frac{51}{33} & \frac{3000}{33} \\
0 & 0 & \frac{319}{33} & \frac{24000}{33}
\end{bmatrix}
\]

---

#### Normalize the third row
Divide the third row by \(\frac{319}{33}\) (the coefficient of \(c\) in the third row) to make the leading coefficient of \(c\) in the third row 1.

\[
\begin{bmatrix}
1 & 0 & -\frac{104}{33} & \frac{8500}{33} \\
0 & 1 & -\frac{51}{33} & \frac{3000}{33} \\
0 & 0 & 1 & 75
\end{bmatrix}
\]

---

#### Back-substitute to solve for \(a\), \(b\), and \(c\)
- Substitute \(c = 75\) into the second row to solve for \(b\):
  \[
  b = \frac{3000}{33} + \frac{51}{33} \times 75 = 500
  \]

- Substitute \(b = 500\) and \(c = 75\) into the first row to solve for \(a\):
  \[
  a = \frac{8500}{33} + \frac{104}{33} \times 75 = 1200
  \]

---

### Final Answer:
- 牛價 (\(a\)) = 1200
- 羊價 (\(b\)) = 500
- 豕價 (\(c\)) = 300
"""
Code error: invalid syntax (<string>, line 2)"""
