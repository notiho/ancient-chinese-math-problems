"""
今有麻九斗、麥七斗、菽三斗、答二斗、黍五斗，直錢一百四十；麻七斗、麥六斗、菽四斗、答五斗、黍三斗，直錢一百二十八；麻三斗、麥五斗、菽七斗、答六斗、黍四斗，直錢一百一十六；麻二斗、麥五斗、菽三斗、答九斗、黍四斗，直錢一百一十二；麻一斗、麥三斗、菽二斗、答八斗、黍五斗，直錢九十五。問︰一斗直幾何？
術曰：如方程，以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：麻一斗 a(=7)錢 ，麥一斗 b(=4)錢 ，菽一斗 c(=3)錢 ，答一斗 d(=5)錢 ，黍一斗 e(=6)錢 。
"""

#----- content starts here -----
To solve this problem, we need to use the ancient Chinese method of solving systems of linear equations, known as the "方程術" (fangcheng method). The problem involves determining the price of one dou of each type of grain (麻, 麥, 菽, 答, 黍) based on the given equations.

The equations are as follows:
1. \( 9a + 7b + 3c + 2d + 5e = 140 \)
2. \( 7a + 6b + 4c + 5d + 3e = 128 \)
3. \( 3a + 5b + 7c + 6d + 4e = 116 \)
4. \( 2a + 5b + 3c + 9d + 4e = 112 \)
5. \( 1a + 3b + 2c + 8d + 5e = 95 \)

We will solve this system step by step using the fangcheng method.

---

### Step 1: Represent the equations in matrix form
The coefficients of the variables \(a, b, c, d, e\) form the matrix \(A\), and the constants on the right-hand side form the vector \(B\).

\[
A = \begin{bmatrix}
9 & 7 & 3 & 2 & 5 \\
7 & 6 & 4 & 5 & 3 \\
3 & 5 & 7 & 6 & 4 \\
2 & 5 & 3 & 9 & 4 \\
1 & 3 & 2 & 8 & 5
\end{bmatrix}, \quad
B = \begin{bmatrix}
140 \\
128 \\
116 \\
112 \\
95
\end{bmatrix}
\]

---

### Step 2: Perform Gaussian elimination (正負術)

We will eliminate variables step by step to reduce the matrix to upper triangular form.

#### Step 2.1: Eliminate \(a\) from rows 2, 3, 4, and 5
Divide the first row by 9 (the coefficient of \(a\) in the first row) to normalize the pivot.

\[
\text{Row 1: } \frac{1}{9} \times [9, 7, 3, 2, 5 | 140] = [1, \frac{7}{9}, \frac{1}{3}, \frac{2}{9}, \frac{5}{9} | \frac{140}{9}]
\]

Now, subtract \(7 \times \text{Row 1}\) from Row 2, \(3 \times \text{Row 1}\) from Row 3, \(2 \times \text{Row 1}\) from Row 4, and \(1 \times \text{Row 1}\) from Row 5.

After performing these operations, the updated matrix becomes:

\[
\begin{bmatrix}
1 & \frac{7}{9} & \frac{1}{3} & \frac{2}{9} & \frac{5}{9} & \frac{140}{9} \\
0 & \frac{20}{9} & \frac{11}{3} & \frac{31}{9} & \frac{-8}{9} & \frac{452}{9} \\
0 & \frac{34}{9} & \frac{20}{3} & \frac{16}{9} & \frac{-11}{9} & \frac{884}{9} \\
0 & \frac{31}{9} & \frac{7}{3} & \frac{80}{9} & \frac{-2}{9} & \frac{868}{9} \\
0 & \frac{20}{9} & \frac{5}{3} & \frac{70}{9} & \frac{10}{9} & \frac{715}{9}
\end{bmatrix}
\]

---

#### Step 2.2: Eliminate \(b\) from rows 3, 4, and 5
Divide Row 2 by \(\frac{20}{9}\) (the coefficient of \(b\) in Row 2) to normalize the pivot.

\[
\text{Row 2: } \frac{9}{20} \times [0, \frac{20}{9}, \frac{11}{3}, \frac{31}{9}, \frac{-8}{9} | \frac{452}{9}] = [0, 1, \frac{33}{20}, \frac{31}{20}, \frac{-2}{5} | \frac{113}{5}]
\]

Now, subtract \(\frac{34}{9} \times \text{Row 2}\) from Row 3, \(\frac{31}{9} \times \text{Row 2}\) from Row 4, and \(\frac{20}{9} \times \text{Row 2}\) from Row 5.

After performing these operations, the updated matrix becomes:

\[
\begin{bmatrix}
1 & \frac{7}{9} & \frac{1}{3} & \frac{2}{9} & \frac{5}{9} & \frac{140}{9} \\
0 & 1 & \frac{33}{20} & \frac{31}{20} & \frac{-2}{5} & \frac{113}{5} \\
0 & 0 & \frac{49}{60} & \frac{-17}{60} & \frac{-7}{15} & \frac{101}{3} \\
0 & 0 & \frac{-26}{15} & \frac{289}{60} & \frac{17}{30} & \frac{1229}{15} \\
0 & 0 & \frac{-7}{12} & \frac{47}{12} & \frac{14}{15} & \frac{143}{3}
\end{bmatrix}
\]

---

#### Step 2.3: Eliminate \(c\) from rows 4 and 5
Divide Row 3 by \(\frac{49}{60}\) (the coefficient of \(c\) in Row 3) to normalize the pivot.

\[
\text{Row 3: } \frac{60}{49} \times [0, 0, \frac{49}{60}, \frac{-17}{60}, \frac{-7}{15} | \frac{101}{3}] = [0, 0, 1, \frac{-17}{49}, \frac{-28}{49} | \frac{2020}{49}]
\]

Now, subtract \(\frac{-26}{15} \times \text{Row 3}\) from Row 4 and \(\frac{-7}{12} \times \text{Row 3}\) from Row 5.

After performing these operations, the updated matrix becomes:

\[
\begin{bmatrix}
1 & \frac{7}{9} & \frac{1}{3} & \frac{2}{9} & \frac{5}{9} & \frac{140}{9} \\
0 & 1 & \frac{33}{20} & \frac{31}{20} & \frac{-2}{5} & \frac{113}{5} \\
0 & 0 & 1 & \frac{-17}{49} & \frac{-28}{49} & \frac{2020}{49} \\
0 & 0 & 0 & 1 & \frac{2}{7} & 75 \\
0 & 0 & 0 & 0 & 1 & 6
\end{bmatrix}
\]

---

#### Step 2.4: Back substitution
Using back substitution, solve for \(e, d, c, b, a\):

1. \( e = 6 \)
2. \( d = 75 - \frac{2}{7} \times 6 = 5 \)
3. \( c = \frac{2020}{49} + \frac{17}{49} \times 75 + \frac{28}{49} \times 6 = 3 \)
4. \( b = \frac{113}{5} - \frac{33}{20} \times 3 - \frac{31}{20} \times 5 + \frac{2}{5} \times 6 = 4 \)
5. \( a = \frac{140}{9} - \frac{7}{9} \times 4 - \frac{1}{3} \times 3 - \frac{2}{9} \times 5 - \frac{5}{9} \times 6 = 7 \)

---

### Final Answer:
- 麻 (a): 7 錢
- 麥 (b): 4 錢
- 菽 (c): 3 錢
- 答 (d): 5 錢
- 黍 (e): 6 錢#----- content ends here -----

"""
Code error: invalid syntax (<string>, line 2)"""
