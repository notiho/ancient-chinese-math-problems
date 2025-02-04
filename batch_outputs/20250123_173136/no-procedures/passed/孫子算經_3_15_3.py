"""
今有婦人河上蕩桮，津吏問曰：「桮何以多？」婦人曰：「家有客。」津吏曰：「客幾何？」婦人曰：「二人共飯，三人共羹，四人共肉，凡用桮六十五，不知客幾何？」
答曰：「 a人 。」
"""

"""
This is a classic ancient Chinese math problem. Let's break it down:

The problem states that:
- 2 people share 1 bowl of rice.
- 3 people share 1 bowl of soup.
- 4 people share 1 bowl of meat.
- A total of 65 bowls (桮) were used.

The question is: how many guests (people) are there?

To solve this, we need to find the number of people \( a \) such that the total number of bowls used matches 65.

---

### Solution in Python:


"""


from fractions import Fraction

# Total bowls used
total_bowls = 65

# Let the number of guests be 'a'
# Each guest uses:
# - 1/2 bowl of rice
# - 1/3 bowl of soup
# - 1/4 bowl of meat

# Total bowls used per guest:
bowls_per_guest = Fraction(1, 2) + Fraction(1, 3) + Fraction(1, 4)

# Solve for the number of guests (a):
a = total_bowls / bowls_per_guest

# Print the result
print(f"The number of guests is: {a} people.")


"""


---

### Explanation:
1. Each guest uses:
   - \( \frac{1}{2} \) bowl of rice,
   - \( \frac{1}{3} \) bowl of soup,
   - \( \frac{1}{4} \) bowl of meat.
   Adding these fractions gives the total bowls used per guest:
   \[
   \text{Bowls per guest} = \frac{1}{2} + \frac{1}{3} + \frac{1}{4} = \frac{13}{12}
   \]

2. The total number of bowls used is 65. To find the number of guests \( a \), divide the total bowls by the bowls used per guest:
   \[
   a = \frac{65}{\frac{13}{12}} = 65 \times \frac{12}{13} = 60
   \]

---

### Final Answer:
The number of guests is **60 people**.
"""


"""
"""
