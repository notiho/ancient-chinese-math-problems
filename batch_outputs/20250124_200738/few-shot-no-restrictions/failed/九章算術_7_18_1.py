"""
今有良馬與駑馬發長安至齊。齊去長安三千里。良馬初日行一百九十三里，日增十三里。駑馬初日行九十七里，日減半里。良馬先至齊，復還迎駑馬。問︰幾何日相逢及各行幾何？
術曰：假令十五日，不足三百三十七里半。令之十六日，多一百四十里。以盈、不足維乘假令之數，并而為實。并盈不足為法。實如法而一，得日數。不盡者，以等數除之而命分。
荅曰： a日 而相逢。良馬行 b里 。駑馬行 c里 。
"""

"""
This is a classic ancient Chinese math problem involving arithmetic progressions for both the good horse (良馬) and the bad horse (駑馬). The problem involves calculating when the two horses meet and how far each has traveled. Let's solve it step by step using Python.

---

### Problem Breakdown:
1. **Distance from Chang'an to Qi**: 3000 li.
2. **Good horse (良馬)**:
   - Initial daily distance: 193 li.
   - Daily increment: 13 li.
3. **Bad horse (駑馬)**:
   - Initial daily distance: 97 li.
   - Daily decrement: 0.5 li.
4. The good horse reaches Qi first, returns to meet the bad horse, and they meet at some point.

We need to calculate:
- The number of days (*a*) until they meet.
- The total distance traveled by the good horse (*b*).
- The total distance traveled by the bad horse (*c*).

---

### Solution in Python:


"""

#----- content starts here -----

from fractions import Fraction

# Constants
total_distance = 3000  # Distance from Chang'an to Qi in li

# 良馬 (Good horse)
good_initial = 193  # Initial daily distance in li
good_increment = 13  # Daily increment in li

# 駑馬 (Bad horse)
bad_initial = 97  # Initial daily distance in li
bad_decrement = Fraction(1, 2)  # Daily decrement in li

# Step 1: Define the distance traveled by each horse after n days
def good_horse_distance(n):
    """Calculate the total distance traveled by the good horse in n days."""
    return n * good_initial + (n * (n - 1) // 2) * good_increment

def bad_horse_distance(n):
    """Calculate the total distance traveled by the bad horse in n days."""
    return n * bad_initial - (n * (n - 1) // 2) * bad_decrement

# Step 2: Find the day when the good horse meets the bad horse
# The good horse reaches Qi, returns, and meets the bad horse
def find_meeting_day():
    for n in range(1, 1000):  # Arbitrary large range to ensure convergence
        good_to_qi = good_horse_distance(n)  # Distance to Qi
        if good_to_qi >= total_distance:
            # The good horse reaches Qi on day n
            distance_past_qi = good_to_qi - total_distance
            for m in range(1, n):  # Days spent returning to meet the bad horse
                bad_distance = bad_horse_distance(n + m)
                good_return_distance = distance_past_qi + good_horse_distance(m)
                if good_return_distance >= bad_distance:
                    return n + m, good_return_distance, bad_distance

# Step 3: Calculate results
meeting_day, good_total_distance, bad_total_distance = find_meeting_day()

# Output results
a = meeting_day
b = good_total_distance
c = bad_total_distance

print(f"相逢日數: {a}日")
print(f"良馬行: {b}里")
print(f"駑馬行: {c}里")
#----- content ends here -----


"""


---

### Explanation of the Code:
1. **Distance Formulas**:
   - The good horse's distance is calculated using the arithmetic progression formula:  
     \( \text{distance} = n \cdot \text{initial} + \frac{n \cdot (n-1)}{2} \cdot \text{increment} \)
   - The bad horse's distance is similarly calculated, but with a decrement.

2. **Meeting Condition**:
   - The good horse reaches Qi, returns, and meets the bad horse. The meeting day is determined by iterating over possible days and checking when the distances match.

3. **Output**:
   - The number of days until they meet (*a*).
   - The total distance traveled by the good horse (*b*).
   - The total distance traveled by the bad horse (*c*).

---

### Example Output:
If you run the code, it will calculate the exact day they meet and the distances traveled by each horse. The results will be in terms of days and li.
"""


"""
Variable 'a' has wrong value. Expected: 3000/191, Actual: 19
Variable 'b' has wrong value. Expected: 866040/191, Actual: 1798
Variable 'c' has wrong value. Expected: 279960/191, Actual: 3515/2"""
