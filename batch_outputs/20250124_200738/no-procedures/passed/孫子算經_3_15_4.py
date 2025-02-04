"""
今有婦人河上蕩桮，津吏問曰：「桮何以多？」婦人曰：「家有客。」津吏曰：「客幾何？」婦人曰：「二人共飯，三人共羹，四人共肉，凡用桮六十五，不知客幾何？」
答曰：「 a人 。」
"""

"""
This is a classic ancient Chinese math problem involving simultaneous equations. Let's solve it step by step.

### Problem Breakdown:
- A woman is washing cups by the river. The ferry officer asks, "Why are there so many cups?"
- The woman replies, "There are guests at home."
- The officer asks, "How many guests?"
- The woman explains:
  - Two people share one bowl of rice.
  - Three people share one bowl of soup.
  - Four people share one plate of meat.
  - In total, 65 cups are used.

We need to find the number of guests (*a* people).

---

### Solution:
Let the number of guests be \( x \). Then:
- The number of bowls of rice used is \( \frac{x}{2} \) (since 2 people share 1 bowl of rice).
- The number of bowls of soup used is \( \frac{x}{3} \) (since 3 people share 1 bowl of soup).
- The number of plates of meat used is \( \frac{x}{4} \) (since 4 people share 1 plate of meat).

The total number of cups used is the sum of all these bowls and plates:
\[
\frac{x}{2} + \frac{x}{3} + \frac{x}{4} = 65
\]

We solve for \( x \).

---

### Python Code:


"""

#----- content starts here -----

from fractions import Fraction

# Total cups used
total_cups = 65

# Solve for x (number of guests)
# (x / 2) + (x / 3) + (x / 4) = 65
# Find the least common denominator (LCD) of 2, 3, and 4, which is 12
# Multiply through by 12 to eliminate fractions:
# 6x + 4x + 3x = 65 * 12
# 13x = 780
# x = 780 / 13

a = Fraction(780, 13)

# Output the result
a
#----- content ends here -----


"""


---

### Explanation of the Solution:
1. Combine the fractions \( \frac{x}{2} + \frac{x}{3} + \frac{x}{4} \) by finding the least common denominator (LCD), which is 12.
   - \( \frac{x}{2} = \frac{6x}{12} \)
   - \( \frac{x}{3} = \frac{4x}{12} \)
   - \( \frac{x}{4} = \frac{3x}{12} \)
   - Adding them gives \( \frac{6x + 4x + 3x}{12} = \frac{13x}{12} \).
2. Set \( \frac{13x}{12} = 65 \).
3. Multiply through by 12: \( 13x = 780 \).
4. Solve for \( x \): \( x = \frac{780}{13} = 60 \).

---

### Final Answer:
The number of guests is:
\[
a = 60 \text{ people.}
\]
"""


"""
"""
