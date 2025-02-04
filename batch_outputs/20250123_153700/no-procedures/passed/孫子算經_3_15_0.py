"""
今有婦人河上蕩桮，津吏問曰：「桮何以多？」婦人曰：「家有客。」津吏曰：「客幾何？」婦人曰：「二人共飯，三人共羹，四人共肉，凡用桮六十五，不知客幾何？」
答曰：「 a人 。」
"""

"""
This is a classic ancient Chinese math problem involving simultaneous equations. Let's break it down:

### Problem:
A woman is washing cups by the river. The ferry officer asks, "Why do you have so many cups?" The woman replies, "There are guests at home." The officer asks, "How many guests?" The woman explains:
- Two people share one bowl of rice.
- Three people share one bowl of soup.
- Four people share one bowl of meat.
- In total, 65 cups are used.

The question is: how many guests are there?

---

### Solution:
Let the number of guests be \( x \).  
From the problem:
- For rice: \( \frac{x}{2} \) bowls are needed.
- For soup: \( \frac{x}{3} \) bowls are needed.
- For meat: \( \frac{x}{4} \) bowls are needed.
- Total cups used = \( \frac{x}{2} + \frac{x}{3} + \frac{x}{4} = 65 \).

We solve for \( x \).

---

### Python Code:


"""


from fractions import Fraction

# Total cups used
total_cups = 65

# Solve the equation: x/2 + x/3 + x/4 = 65
# Find the least common denominator (LCD) of 2, 3, and 4, which is 12
lcd = 12

# Rewrite the equation with the LCD:
# (6x + 4x + 3x) / 12 = 65
# 13x / 12 = 65
# Solve for x:
x = Fraction(65 * 12, 13)

# Convert to integer (since the number of guests must be whole)
a = int(x)

# Output the result
a


"""


---

### Explanation:
1. The least common denominator (LCD) of 2, 3, and 4 is 12.
2. Rewrite the equation with the LCD: \( \frac{6x + 4x + 3x}{12} = 65 \).
3. Combine terms: \( \frac{13x}{12} = 65 \).
4. Solve for \( x \): \( x = \frac{65 \times 12}{13} = 60 \).

Thus, the number of guests is **60**.

---

### Answer:
The number of guests is **a = 60**.
"""


"""
"""
