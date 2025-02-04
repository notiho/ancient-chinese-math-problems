"""
今有錢六千九百三十，欲令二百一十六人作九分，分之八十一人，人與二分；七十二人，人與三分；六十三人，人與四分。問：三種各得幾何？
術曰：先置八十一人于上，七十二人次之，六十三人在下，頭位以二乘之，得一百六十二，次位以三乘之，得二百一十六，下位以四乘之，得二百五十二，副并三位，得六百三十為法。又置錢六千九百三十為三位頭位，以一百六十二乘之，得一百一十二萬二千六百六十，又以二百一十六乘中位，得一百四十九萬六千八百八十，又以二百五十二乘下位，得一百七十四萬六千三百六十，各為實以法，六百三十各除之，頭位得一千七百八十二，中位得二千三百七十六，下位得二千七百七十二，各以人數除之，即得。
答曰：二分人得錢 a ，三分人得錢 b ，四分人得錢 c 。
"""

"""
This is a classic ancient Chinese math problem involving proportional distribution. Let's break it down and encode it in Python step by step.

### Problem Description:
- There are **6930 coins** to be distributed among **216 people** divided into three groups:
  - **81 people** each get **2 parts**.
  - **72 people** each get **3 parts**.
  - **63 people** each get **4 parts**.
- The goal is to calculate how much money each group gets and how much each person in the group receives.

### Procedure:
1. Multiply the number of people in each group by their respective parts:
   - Group 1: \( 81 \times 2 = 162 \)
   - Group 2: \( 72 \times 3 = 216 \)
   - Group 3: \( 63 \times 4 = 252 \)
2. Add these values to get the total divisor (法): \( 162 + 216 + 252 = 630 \).
3. Multiply the total money (6930) by each group's value (162, 216, 252) to get the "dividend" (實):
   - Group 1: \( 6930 \times 162 \)
   - Group 2: \( 6930 \times 216 \)
   - Group 3: \( 6930 \times 252 \)
4. Divide each dividend by the total divisor (630) to get the total money for each group.
5. Divide the total money for each group by the number of people in that group to get the money per person.

### Python Code:


"""

#----- content starts here -----

from fractions import Fraction

# Total money and group data
total_money = 6930
group_data = [
    {"people": 81, "parts": 2},
    {"people": 72, "parts": 3},
    {"people": 63, "parts": 4},
]

# Step 1: Calculate the total divisor (法)
divisor = sum(group["people"] * group["parts"] for group in group_data)

# Step 2: Calculate the total money for each group
results = []
for group in group_data:
    group_value = group["people"] * group["parts"]
    group_total_money = Fraction(total_money * group_value, divisor)
    money_per_person = Fraction(group_total_money, group["people"])
    results.append({
        "total_money": group_total_money,
        "money_per_person": money_per_person
    })

# Extract results
a = results[0]["total_money"]  # Total money for group 1 (2 parts per person)
b = results[1]["total_money"]  # Total money for group 2 (3 parts per person)
c = results[2]["total_money"]  # Total money for group 3 (4 parts per person)

# Print results
print(f"二分人得錢 {a} ，三分人得錢 {b} ，四分人得錢 {c} 。")
#----- content ends here -----


"""


### Explanation of Results:
- `a`: Total money for the group where each person gets 2 parts.
- `b`: Total money for the group where each person gets 3 parts.
- `c`: Total money for the group where each person gets 4 parts.

This code calculates the proportional distribution of money based on the given rules.
"""


"""
Variable 'a' has wrong value. Expected: 22, Actual: 1782
Variable 'b' has wrong value. Expected: 33, Actual: 2376
Variable 'c' has wrong value. Expected: 44, Actual: 2772"""
