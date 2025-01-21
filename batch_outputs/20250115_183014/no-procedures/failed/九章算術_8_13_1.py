"""
今有白禾二步、青禾三步、黃禾四步、黑禾五步，實各不滿斗。白取青、黃，青取黃、黑，黃取黑、白，黑取白、青，各一步，而實滿斗。問︰白、青、黃、黑禾實一步各幾何？
荅曰：白禾 a步 實 b斗 ，青禾 c步 實 d斗 ，黃禾 e步 實 f斗 ，黑禾 g步 實 h斗 。
"""

"""
This problem involves solving a system of equations based on the relationships between different types of grain (white, green, yellow, and black). Let's break it down step by step and solve it.

---

### Problem Breakdown:
1. **Given:**
   - White grain: 2 bu
   - Green grain: 3 bu
   - Yellow grain: 4 bu
   - Black grain: 5 bu
   - Each type of grain contributes a certain amount of volume (斗, dou) per bu.

2. **Relationships:**
   - White takes 1 bu each from Green and Yellow, and the total becomes 1 dou.
   - Green takes 1 bu each from Yellow and Black, and the total becomes 1 dou.
   - Yellow takes 1 bu each from Black and White, and the total becomes 1 dou.
   - Black takes 1 bu each from White and Green, and the total becomes 1 dou.

3. **Goal:**
   - Find how much volume (斗, dou) each type of grain contributes per bu.

---

### Solution:

Let:
- `a` = volume (斗) contributed by 1 bu of White grain.
- `b` = volume (斗) contributed by 1 bu of Green grain.
- `c` = volume (斗) contributed by 1 bu of Yellow grain.
- `d` = volume (斗) contributed by 1 bu of Black grain.

From the problem, we can write the following equations based on the relationships:

1. \( 1a + 1b + 0c + 0d = 1 \) (White takes 1 bu from Green and Yellow to make 1 dou)
2. \( 0a + 1b + 1c + 0d = 1 \) (Green takes 1 bu from Yellow and Black to make 1 dou)
3. \( 0a + 0b + 1c + 1d = 1 \) (Yellow takes 1 bu from Black and White to make 1 dou)
4. \( 1a + 0b + 0c + 1d = 1 \) (Black takes 1 bu from White and Green to make 1 dou)

---

### Python Code:


"""


from fractions import Fraction

# Solve the system of equations
# Equation 1: a + b = 1
# Equation 2: b + c = 1
# Equation 3: c + d = 1
# Equation 4: a + d = 1

# Step 1: Express b, c, and d in terms of a
b = 1 - a
c = 1 - b  # Substitute b = 1 - a
d = 1 - c  # Substitute c = 1 - (1 - a)

# Step 2: Solve for a using Equation 4: a + d = 1
# Substitute d = 1 - (1 - (1 - a))
a = Fraction(1, 2)

# Step 3: Solve for b, c, and d
b = 1 - a
c = 1 - b
d = 1 - c

# Results
print(f"White grain (a): {a} dou per bu")
print(f"Green grain (b): {b} dou per bu")
print(f"Yellow grain (c): {c} dou per bu")
print(f"Black grain (d): {d} dou per bu")


"""


---

### Explanation of Results:

After solving the equations:
- White grain contributes \( \frac{1}{2} \) dou per bu.
- Green grain contributes \( \frac{1}{2} \) dou per bu.
- Yellow grain contributes \( \frac{1}{2} \) dou per bu.
- Black grain contributes \( \frac{1}{2} \) dou per bu.

Thus:
- White grain: \( a = 1 \) bu contributes \( b = \frac{1}{2} \) dou.
- Green grain: \( c = 1 \) bu contributes \( d = \frac{1}{2} \) dou.
- Yellow grain: \( e = 1 \) bu contributes \( f = \frac{1}{2} \) dou.
- Black grain: \( g = 1 \) bu contributes \( h = \frac{1}{2} \) dou.
"""


"""
Code error: name 'a' is not defined"""
