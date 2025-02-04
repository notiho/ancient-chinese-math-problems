"""
今有良馬與駑馬發長安至齊。齊去長安三千里。良馬初日行一百九十三里，日增十三里。駑馬初日行九十七里，日減半里。良馬先至齊，復還迎駑馬。問︰幾何日相逢及各行幾何？
術曰：假令十五日，不足三百三十七里半。令之十六日，多一百四十里。以盈、不足維乘假令之數，并而為實。并盈不足為法。實如法而一，得日數。不盡者，以等數除之而命分。
荅曰： a日 而相逢。良馬行 b里 。駑馬行 c里 。
"""

"""
This is a classic ancient Chinese math problem involving arithmetic progressions. Let's break it down step by step and encode the solution in Python.

### Problem Explanation:
- The distance between Chang'an and Qi is 3000 li.
- The **good horse (良馬)** starts by traveling 193 li on the first day and increases its daily distance by 13 li each day.
- The **inferior horse (駑馬)** starts by traveling 97 li on the first day and decreases its daily distance by 0.5 li each day.
- The good horse reaches Qi first, then turns back to meet the inferior horse.
- We are tasked to find:
  1. The number of days (*a*) it takes for the two horses to meet.
  2. The total distance traveled by the good horse (*b*).
  3. The total distance traveled by the inferior horse (*c*).

---

### Solution Procedure:
1. **Good Horse's Distance**:
   The good horse travels according to an arithmetic progression:
   - First day: 193 li
   - Second day: 193 + 13 li
   - Third day: 193 + 2 × 13 li, and so on.

   The distance traveled by the good horse on the *n*-th day is:
   \[
   d_{\text{good}}(n) = 193 + 13(n - 1)
   \]
   The total distance traveled in *n* days is the sum of the arithmetic progression:
   \[
   S_{\text{good}}(n) = \frac{n}{2} \times \left(2 \times 193 + (n - 1) \times 13\right)
   \]

2. **Inferior Horse's Distance**:
   The inferior horse also follows an arithmetic progression:
   - First day: 97 li
   - Second day: 97 - 0.5 li
   - Third day: 97 - 2 × 0.5 li, and so on.

   The distance traveled by the inferior horse on the *n*-th day is:
   \[
   d_{\text{inferior}}(n) = 97 - 0.5(n - 1)
   \]
   The total distance traveled in *n* days is the sum of the arithmetic progression:
   \[
   S_{\text{inferior}}(n) = \frac{n}{2} \times \left(2 \times 97 - (n - 1) \times 0.5\right)
   \]

3. **Meeting Point**:
   - The good horse travels to Qi (3000 li), then turns back to meet the inferior horse.
   - Let *n* be the number of days it takes for the two horses to meet.
   - The total distance traveled by the good horse in *n* days must equal the total distance traveled by the inferior horse in *n* days plus the 3000 li round trip.

---

### Python Code Implementation:


"""

#----- content starts here -----

from fractions import Fraction

# Constants
distance_to_qi = 3000  # Distance from Chang'an to Qi in li
good_horse_initial = 193  # Initial daily distance for the good horse
good_horse_increment = 13  # Daily increment for the good horse
inferior_horse_initial = 97  # Initial daily distance for the inferior horse
inferior_horse_decrement = 0.5  # Daily decrement for the inferior horse

# Function to calculate total distance traveled by the good horse in n days
def good_horse_distance(n):
    return n / 2 * (2 * good_horse_initial + (n - 1) * good_horse_increment)

# Function to calculate total distance traveled by the inferior horse in n days
def inferior_horse_distance(n):
    return n / 2 * (2 * inferior_horse_initial - (n - 1) * inferior_horse_decrement)

# Find the number of days it takes for the two horses to meet
n = 1
while True:
    good_horse_total = good_horse_distance(n)
    inferior_horse_total = inferior_horse_distance(n)
    if good_horse_total >= distance_to_qi + inferior_horse_total:
        break
    n += 1

# Calculate the total distances traveled
good_horse_total_distance = good_horse_distance(n)
inferior_horse_total_distance = inferior_horse_distance(n)

# Results
a = n  # Number of days
b = good_horse_total_distance  # Total distance traveled by the good horse
c = inferior_horse_total_distance  # Total distance traveled by the inferior horse

# Output the results
print(f"相逢日數: {a}日")
print(f"良馬行: {b}里")
print(f"駑馬行: {c}里")
#----- content ends here -----


"""


---

### Explanation of the Code:
1. We define functions to calculate the total distance traveled by the good horse and the inferior horse in *n* days using the formulas for the sum of an arithmetic progression.
2. We use a `while` loop to find the smallest *n* such that the total distance traveled by the good horse (including the round trip to Qi) is greater than or equal to the total distance traveled by the inferior horse plus the 3000 li.
3. Once the condition is met, we calculate the total distances traveled by both horses and output the results.

---

### Final Answer:
- *a*: The number of days it takes for the two horses to meet.
- *b*: The total distance traveled by the good horse.
- *c*: The total distance traveled by the inferior horse.
"""


"""
Variable 'a' has wrong value. Expected: 3000/191, Actual: 16
Variable 'b' has wrong value. Expected: 866040/191, Actual: 4648.0
Variable 'c' has wrong value. Expected: 279960/191, Actual: 1492.0"""
