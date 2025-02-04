"""
今有邑方十里，各中開門。甲乙俱從邑中央而出。乙東出；甲南出，出門不知步數，邪向東北磨邑，適與乙會。率甲行五，乙行三。問︰甲、乙行各幾何？
術曰：令五自乘，三亦自乘，并而半之，為邪行率。邪行率減於五自乘者，餘，為南行率。以三乘五，為乙東行率。置邑方半之，以南行率乘之，如東行率而一，即得出南門步數。以增邑方半，即南行。置南行步求弦者，以邪行率乘之，求東者以東行率乘之，各自為實。實如南行率得一步。
荅曰：甲出南門 a步 ，邪東北行 b步 ，及乙。乙東行 c步 。
"""

"""
This is a classic ancient Chinese math problem involving geometry and proportional reasoning. Let's break it down step by step and encode it in Python.

### Problem Description:
- A square city has sides of 10 li (里), and gates are located at the middle of each side.
- Two people, A (甲) and B (乙), start at the center of the city.
  - B exits through the east gate.
  - A exits through the south gate, but instead of continuing straight, A moves diagonally northeast along the city boundary and meets B.
- The walking rates are:
  - A walks 5 steps for every 3 steps B walks.
- Question: How far does A walk south to exit the south gate, how far does A walk diagonally northeast, and how far does B walk east?

### Procedure:
1. Compute the diagonal walking rate (邪行率) using the Pythagorean theorem.
2. Use the diagonal rate to find the southward walking rate (南行率).
3. Use the walking rates to calculate the distances walked by A and B.

### Python Code:


"""

#----- content starts here -----

from fractions import Fraction
import math

# Given data
邑方 = 10  # Side length of the square city in li
甲速 = 5    # A's walking rate
乙速 = 3    # B's walking rate

# Step 1: Compute the diagonal walking rate (邪行率)
甲速平方 = 甲速 ** 2
乙速平方 =乙速**#----- content ends here -----


"""

"""


"""
Code error: invalid syntax (<string>, line 13)"""
