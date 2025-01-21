"""
今有均輸卒：甲縣一千二百人，薄塞；乙縣一千五百五十人，行道一日；丙縣一千二百八十人，行道二日；丁縣九百九十人，行道三日；戊縣一千七百五十人，行道五日。凡五縣，賦輸卒一月一千二百人。欲以遠近、戶率，多少衰出之。問︰縣各幾何？
術曰：令縣卒，各如其居所及行道日數而一，以為衰。甲衰四，乙衰五，丙衰四，丁衰三，戊衰五，副并為法。以人數乘未并者各自為實。實如法而一。有分者，上下輩之。
荅曰：甲縣 a人 。乙縣 b人 。丙縣 c人 。丁縣 d人 。戊縣 e人 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves distributing a total of 1200 soldiers among five counties (甲, 乙, 丙, 丁, 戊) based on their respective weights (衰). The weights are determined by the distance and the number of days traveled.

Here is the Python code:


"""


from fractions import Fraction

# Given data
total_soldiers = 1200  # Total soldiers to be distributed
weights = {
    "甲": 4,  # Weight for 甲
    "乙": 5,  # Weight for 乙
    "丙": 4,  # Weight for 丙
    "丁": 3,  # Weight for 丁
    "戊": 5   # Weight for 戊
}

# Calculate the total weight
total_weight = sum(weights.values())

# Calculate the number of soldiers for each county
a = Fraction(weights["甲"], total_weight) * total_soldiers
b = Fraction(weights["乙"], total_weight) * total_soldiers
c = Fraction(weights["丙"], total_weight) * total_soldiers
d = Fraction(weights["丁"], total_weight) * total_soldiers
e = Fraction(weights["戊"], total_weight) * total_soldiers

# Results
a, b, c, d, e


"""


### Explanation:
1. **Weights (衰):** The weights for each county are given as 4, 5, 4, 3, and 5 for 甲, 乙, 丙, 丁, and 戊 respectively.
2. **Total Weight:** The sum of all weights is calculated.
3. **Distribution:** The number of soldiers for each county is proportional to its weight. This is calculated as `(weight of county / total weight) * total soldiers`.
4. **Fraction Class:** The `Fraction` class is used to ensure precise calculations, especially when the results are not integers.

### Output:
The variables `a`, `b`, `c`, `d`, and `e` will contain the number of soldiers assigned to each county in fractional form.
"""


"""
Variable 'a' has wrong value. Expected: 229, Actual: 1600/7
Variable 'b' has wrong value. Expected: 286, Actual: 2000/7
Variable 'c' has wrong value. Expected: 228, Actual: 1600/7
Variable 'd' has wrong value. Expected: 171, Actual: 1200/7
Variable 'e' has wrong value. Expected: 286, Actual: 2000/7"""
