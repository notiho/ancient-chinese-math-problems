"""
今有婦人河上蕩桮，津吏問曰：「桮何以多？」婦人曰：「家有客。」津吏曰：「客幾何？」婦人曰：「二人共飯，三人共羹，四人共肉，凡用桮六十五，不知客幾何？」
答曰：「 a人 。」
"""

"""
This problem is a classic ancient Chinese math puzzle. Let's break it down:

The problem involves determining the number of guests based on the following conditions:
- 2 people share 1 bowl of rice.
- 3 people share 1 bowl of soup.
- 4 people share 1 bowl of meat.
- In total, 65 bowls are used.

We need to find the number of guests, denoted as `a`.

---

### Solution in Python:


"""

#----- content starts here -----

from fractions import Fraction

# Total number of bowls used
total_bowls = 65

# Let the number of guests be 'a'
# Each guest contributes:
# - 1/2 bowl of rice
# - 1/3 bowl of soup
# - 1/4 bowl of meat
# The total number of bowls used is:
# a * (1/2 + 1/3 + 1/4) = total_bowls

# Calculate the combined fraction of bowls per guest
bowls_per_guest = Fraction(1, 2) + Fraction(1, 3) + Fraction(1, 4)

# Solve for the number of guests
a = total_bowls / bowls_per_guest

# Output the result
a = int(a)  # The number of guests must be an integer
print(f"The number of guests is: {a} people.")
#----- content ends here -----


"""


---

### Explanation:
1. Each guest contributes:
   - \( \frac{1}{2} \) bowl of rice,
   - \( \frac{1}{3} \) bowl of soup,
   - \( \frac{1}{4} \) bowl of meat.
2. The total contribution per guest is:
   \[
   \text{Bowls per guest} = \frac{1}{2} + \frac{1}{3} + \frac{1}{4} = \frac{13}{12}
   \]
3. The total number of bowls is 65, so:
   \[
   a \times \frac{13}{12} = 65
   \]
   Solving for \( a \):
   \[
   a = 65 \div \frac{13}{12} = 65 \times \frac{12}{13} = 60
   \]
4. Therefore, there are **60 guests**.

---

### Final Answer:
**a = 60 people**.
"""


"""
"""
