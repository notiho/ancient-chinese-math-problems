"""
今有孟仲季兄弟三人各持絹不知疋數大兄謂二弟曰我得汝等絹各半得滿七十九疋中弟曰我得兄弟絹各半得滿六十八疋小弟曰我得二兄絹各半得滿五十七疋問兄弟本持絹各幾何
術曰大兄二中弟一小弟一合一百五十八疋大兄一中弟二小弟一合一百三十六疋大兄一中弟一小二合一百一十四疋如方程而求即得
方程術曰置上禾三秉中禾二秉下禾一秉實三十九斗於右方中左禾列如右方以右行上禾遍乘中行而以直除又乘其次亦以直除然以中行中禾不盡者遍乘左行而以直除左方下禾不盡者上為法下為實實即下禾之實求中禾以法乘中行下實而除下禾之實餘如中禾秉數而一即中禾之實求上禾亦以法乘右行下實而除下禾中禾之實餘如上禾秉數而一即上禾之實實皆如法各得一斗
答曰孟 a疋 仲 b疋 季 c疋
"""

#----- content starts here -----
To solve this problem, we will use the method of simultaneous equations as described in the "方程術" (method of solving systems of equations). The problem involves three brothers, Meng, Zhong, and Ji, each holding an unknown number of bolts of silk. The relationships between their holdings are given, and we need to calculate how many bolts each brother originally held.

The equations derived from the problem are:
1. Meng's silk + half of Zhong's silk + half of Ji's silk = 79 bolts.
2. Zhong's silk + half of Meng's silk + half of Ji's silk = 68 bolts.
3. Ji's silk + half of Meng's silk + half of Zhong's silk = 57 bolts.

We will solve these equations step by step using the method described.

---

### Step 1: Represent the equations
Let:
- `孟 = x` (Meng's silk)
- `仲 = y` (Zhong's silk)
- `季 = z` (Ji's silk)

The equations are:
1. \( x + \frac{1}{2}y + \frac{1}{2}z = 79 \)
2. \( y + \frac{1}{2}x + \frac{1}{2}z = 68 \)
3. \( z + \frac{1}{2}x + \frac{1}{2}y = 57 \)

Multiply through by 2 to eliminate fractions:
1. \( 2x + y + z = 158 \)
2. \( 2y + x + z = 136 \)
3. \( 2z + x + y = 114 \)

---

### Step 2: Solve the system of equations
We now solve the system of linear equations:
1. \( 2x + y + z = 158 \)
2. \( x + 2y + z = 136 \)
3. \( x + y + 2z = 114 \)

#### Subtract equations to eliminate variables:
- Subtract equation (2) from equation (1):
  \[
  (2x + y + z) - (x + 2y + z) = 158 - 136
  \]
  \[
  x - y = 22 \tag{4}
  \]

- Subtract equation (3) from equation (2):
  \[
  (x + 2y + z) - (x + y + 2z) = 136 - 114
  \]
  \[
  y - z = 22 \tag{5}
  \]

- Subtract equation (3) from equation (1):
  \[
  (2x + y + z) - (x + y + 2z) = 158 - 114
  \]
  \[
  x - z = 44 \tag{6}
  \]

#### Solve for \(x\), \(y\), and \(z\):
From equation (4): \( x = y + 22 \).

From equation (5): \( y = z + 22 \).

Substitute \( y = z + 22 \) into \( x = y + 22 \):
\[
x = (z + 22) + 22
\]
\[
x = z + 44
\]

Now substitute \( x = z + 44 \) and \( y = z + 22 \) into the first original equation \( 2x + y + z = 158 \):
\[
2(z + 44) + (z + 22) + z = 158
\]
\[
2z + 88 + z + 22 + z = 158
\]
\[
4z + 110 = 158
\]
\[
4z = 48
\]
\[
z = 12
\]

Substitute \( z = 12 \) into \( y = z + 22 \):
\[
y = 12 + 22 = 34
\]

Substitute \( z = 12 \) into \( x = z + 44 \):
\[
x = 12 + 44 = 56
\]

---

### Final Answer:
- Meng (孟) holds \( a = 56 \) bolts of silk.
- Zhong (仲) holds \( b = 34 \) bolts of silk.
- Ji (季) holds \( c = 12 \) bolts of silk.

Answer: \( 孟 = 56 \) 疋, \( 仲 = 34 \) 疋, \( 季 = 12 \) 疋.#----- content ends here -----

"""
Code error: unterminated string literal (detected at line 5) (<string>, line 5)"""
