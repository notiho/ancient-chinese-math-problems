"""
今有婦人河上蕩桮，津吏問曰：「桮何以多？」婦人曰：「家有客。」津吏曰：「客幾何？」婦人曰：「二人共飯，三人共羹，四人共肉，凡用桮六十五，不知客幾何？」
答曰：「 a人 。」
"""

"""
This is a classic ancient Chinese math problem involving solving a system of equations. Let's break it down and solve it step by step.

---

### Problem Breakdown:
- A woman is washing cups by the river.
- The ferry official asks her why there are so many cups.
- She replies that there are guests at her house.
- She explains:
  - 2 people share 1 bowl of rice.
  - 3 people share 1 bowl of soup.
  - 4 people share 1 bowl of meat.
- In total, 65 cups are used.
- The question is: how many guests are there?

---

### Solution:
Let the number of guests be \( x \).  
The total number of cups used is the sum of the cups for rice, soup, and meat.

1. **Rice cups**:  
   Since 2 people share 1 bowl of rice, the number of bowls of rice is \( \frac{x}{2} \).  
   Each bowl uses 1 cup, so the number of cups for rice is \( \frac{x}{2} \).

2. **Soup cups**:  
   Since 3 people share 1 bowl of soup, the number of bowls of soup is \( \frac{x}{3} \).  
   Each bowl uses 1 cup, so the number of cups for soup is \( \frac{x}{3} \).

3. **Meat cups**:  
   Since 4 people share 1 bowl of meat, the number of bowls of meat is \( \frac{x}{4} \).  
   Each bowl uses 1 cup, so the number of cups for meat is \( \frac{x}{4} \).

4. **Total cups**:  
   The total number of cups is given as 65.  
   So, we have the equation:  
   \[
   \frac{x}{2} + \frac{x}{3} + \frac{x}{4} = 65
   \]

---

### Solve for \( x \):
To solve this equation, find a common denominator for the fractions.  
The denominators are 2, 3, and 4. The least common multiple (LCM) is 12.

Multiply through by 12 to eliminate the fractions:
\[
12 \cdot \frac{x}{2} + 12 \cdot \frac{x}{3} + 12 \cdot \frac{x}{4} = 12 \cdot 65
\]

Simplify each term:
\[
6x + 4x + 3x = 780
\]

Combine like terms:
\[
13x = 780
\]

Solve for \( x \):
\[
x = \frac{780}{13} = 60
\]

---

### Final Answer:
The number of guests is \( a = 60 \).

---

### Python Code:

"""


from fractions import Fraction

# Total cups used
total_cups = 65

# Solve for x using the equation (x/2 + x/3 + x/4 = 65)
# Multiply through by the LCM of 2, 3, and 4, which is 12
numerator = 12 * total_cups
denominator = 6 + 4 + 3

# Number of guests
a = Fraction(numerator, denominator)

print(f"The number of guests is {a} people.")


"""


Output:
```
The number of guests is 60 people.
```
"""


"""
"""
