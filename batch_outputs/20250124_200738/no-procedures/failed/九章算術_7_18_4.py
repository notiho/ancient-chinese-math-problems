"""
今有良馬與駑馬發長安至齊。齊去長安三千里。良馬初日行一百九十三里，日增十三里。駑馬初日行九十七里，日減半里。良馬先至齊，復還迎駑馬。問︰幾何日相逢及各行幾何？
荅曰： a日 而相逢。良馬行 b里 。駑馬行 c里 。
"""

"""
This is a classic problem involving arithmetic progressions for both the good horse (良馬) and the slow horse (駑馬). Let's solve it step by step.

---

### Problem:
- The distance between Chang'an and Qi is 3000 li.
- The good horse (良馬) starts by traveling 193 li on the first day, and increases its daily travel by 13 li each day.
- The slow horse (駑馬) starts by traveling 97 li on the first day, and decreases its daily travel by 0.5 li each day.
- The good horse reaches Qi first, then returns to meet the slow horse.
- Question: After how many days do they meet? How far has each horse traveled?

---

### Solution in Python:


"""

#----- content starts here -----

from fractions import Fraction

# Initial conditions
distance = 3000  # Total distance in li

# 良馬 (good horse)
良馬初日 = 193  # First day's travel in li
良馬日增 = 13    # Daily increase in li

# 駑馬 (slow horse)
駑馬初日 = 97    # First day's travel in li
駑馬日減 = Fraction(1, 2)  # Daily decrease in li

# Variables to track progress
良馬距離 = 0  # Distance traveled by the good horse
駑馬距離 = 0  # Distance traveled by the slow horse
日數 = 0      # Number of days

# Step 1: Calculate when the good horse reaches Qi
while 良馬距離 < distance:
    日數 += 1
    良馬距離 += 良馬初日 + (日數 - 1) * 良馬日增

良馬到齊日數 = 日數  # Days it takes for the good horse to reach Qi
良馬到齊距離 = 良馬距離  # Distance traveled by the good horse to reach Qi

# Step 2: The good horse returns to meet the slow horse
日數 = 0  # Reset day counter
良馬距離 = 0  # Reset good horse's distance
駑馬距離 = 0  # Reset slow horse's distance

while True:
    日數 += 1
    
    # Update distances for both horses
    良馬距離 += 良馬初日 + (日數 - 1) * 良馬日增
    駑馬距離 += max(0, 駑馬初日 - (日數 - 1) * 駑馬日減)  # Slow horse cannot travel negative distances
    
    # Check if the good horse meets the slow horse
    if 良馬距離 - (2 * distance - 駑馬距離) >= 0:
        break

# Step 3: Calculate total distances traveled
良馬總距離 = 良馬距離
駑馬總距離 = 駑馬距離

# Step 4: Output results
a = 日數  # Days until they meet
b = 良馬總距離  # Total distance traveled by the good horse
c = 駑馬總距離  # Total distance traveled by the slow horse

a, b, c
#----- content ends here -----


"""


---

### Explanation:
1. **良馬到齊日數**: First, calculate how many days it takes for the good horse to reach Qi using the arithmetic progression formula.
2. **良馬返回迎駑馬**: After reaching Qi, the good horse starts returning to meet the slow horse. Both horses' distances are updated daily until they meet.
3. **相逢日數**: The day they meet is recorded, along with the total distances traveled by each horse.

---

### Final Answer:
- **a**: The number of days until they meet.
- **b**: The total distance traveled by the good horse.
- **c**: The total distance traveled by the slow horse.
"""


"""
Variable 'a' has wrong value. Expected: 3000/191, Actual: 16
Variable 'b' has wrong value. Expected: 866040/191, Actual: 4648
Variable 'c' has wrong value. Expected: 279960/191, Actual: 1492"""
