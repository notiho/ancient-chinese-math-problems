"""
今有令一人、吏五人、從者一十人，食雞一十；令一十人、吏一人、從者五人，食雞八；令五人、吏一十人、從者一人，食雞六。問︰令、吏、從者食雞各幾何？
荅曰：令 a人 食 b雞 ，吏 c人 食 d雞 ，從者 e人 食 f雞 。
"""

"""
This problem involves solving a system of equations to determine how many chickens are consumed per person by the "令" (official), "吏" (clerk), and "從者" (attendant). Let's break it down step by step.

### Problem Setup:
1. **Given:**
   - 1 official, 5 clerks, and 10 attendants eat 10 chickens.
   - 10 officials, 1 clerk, and 5 attendants eat 8 chickens.
   - 5 officials, 10 clerks, and 1 attendant eat 6 chickens.

2. **Unknowns:**
   - Let `a` be the number of chickens consumed by 1 official.
   - Let `b` be the number of chickens consumed by 1 clerk.
   - Let `c` be the number of chickens consumed by 1 attendant.

3. **Equations:**
   - \( 1a + 5b + 10c = 10 \)
   - \( 10a + 1b + 5c = 8 \)
   - \( 5a + 10b + 1c = 6 \)

We will solve this system of equations step by step.

---

### Python Code:


"""


from fractions import Fraction

# Define the equations
# 1a + 5b + 10c = 10
# 10a + 1b + 5c = 8
# 5a + 10b + 1c = 6

# Coefficients of the equations
A1, B1, C1, D1 = 1, 5, 10, 10
A2, B2, C2, D2 = 10, 1, 5, 8
A3, B3, C3, D3 = 5, 10, 1, 6

# Solve for a, b, c using elimination
# Step 1: Eliminate `a` from the second and third equations
factor1 = A2 / A1
factor2 = A3 / A1

B2_new = B2 - factor1 * B1
C2_new = C2 - factor1 * C1
D2_new = D2 - factor1 * D1

B3_new = B3 - factor2 * B1
C3_new = C3 - factor2 * C1
D3_new = D3 - factor2 * D1

# Step 2: Eliminate `b` from the third equation
factor3 = B3_new / B2_new

C3_final = C3_new - factor3 * C2_new
D3_final = D3_new - factor3 * D2_new

# Step 3: Solve for `c`
c = Fraction(D3_final, C3_final)

# Step 4: Solve for `b`
b = Fraction(D2_new - C2_new * c, B2_new)

# Step 5: Solve for `a`
a = Fraction(D1 - B1 * b - C1 * c, A1)

# Results
a_people = 1  # 1 official
b_people = 1  # 1 clerk
c_people = 1  # 1 attendant

print(f"令 {a_people}人 食 {a}雞")
print(f"吏 {b_people}人 食 {b}雞")
print(f"從者 {c_people}人 食 {c}雞")


"""


---

### Explanation of the Solution:
1. We use the method of elimination to solve the system of equations.
2. The fractions library ensures that the results are expressed as exact fractions.
3. The final result gives the number of chickens consumed by each type of person.

---

### Final Answer:
After running the code, the output will be:

- **令** \( a \) 人 食 \( b \) 雞
- **吏** \( c \) 人 食 \( d \) 雞
- **從者** \( e \) 人 食 \( f \) 雞
"""


"""
Code error: both arguments should be Rational instances"""
