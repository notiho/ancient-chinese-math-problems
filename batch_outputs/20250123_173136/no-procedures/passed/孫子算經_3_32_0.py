"""
今有出門望見九堤，堤有九木，木有九枝，枝有九巢，巢有九禽，禽有九雛，雛有九毛，毛有九色。問：各幾何？
答曰：木 a枝 ， b 巢， c 禽， d 雛， e 毛， f 色， g 。
"""

"""
This is a classic ancient Chinese math riddle involving exponential growth. Let's break it down step by step and calculate the total quantities for each item.

### Problem Breakdown:
1. There are **9 dikes (堤)**.
2. Each dike has **9 trees (木)**.
3. Each tree has **9 branches (枝)**.
4. Each branch has **9 nests (巢)**.
5. Each nest has **9 birds (禽)**.
6. Each bird has **9 chicks (雛)**.
7. Each chick has **9 feathers (毛)**.
8. Each feather has **9 colors (色)**.

We need to calculate the total quantities for each level.

---

### Python Code:


"""


from fractions import Fraction

# Start with the base number
base = 9

# Calculate each level
堤 = base
木 = 堤 * base
枝 = 木 * base
巢 = 枝 * base
禽 = 巢 * base
雛 = 禽 * base
毛 = 雛 * base
色 = 毛 * base

# Assign results to variables
a = 木
b = 枝
c = 巢
d = 禽
e = 雛
f = 毛
g = 色

# Print results
print(f"木: {a} 枝")
print(f"枝: {b} 巢")
print(f"巢: {c} 禽")
print(f"禽: {d} 雛")
print(f"雛: {e} 毛")
print(f"毛: {f} 色")
print(f"色: {g}")


"""


---

### Explanation of Results:
1. 木 (trees): \( 9 \times 9 = 81 \)
2. 枝 (branches): \( 81 \times 9 = 729 \)
3. 巢 (nests): \( 729 \times 9 = 6,561 \)
4. 禽 (birds): \( 6,561 \times 9 = 59,049 \)
5. 雛 (chicks): \( 59,049 \times 9 = 531,441 \)
6. 毛 (feathers): \( 531,441 \times 9 = 4,782,969 \)
7. 色 (colors): \( 4,782,969 \times 9 = 43,046,721 \)

So the final answers are:
- 木: 81 枝
- 枝: 729 巢
- 巢: 6,561 禽
- 禽: 59,049 雛
- 雛: 531,441 毛
- 毛: 4,782,969 色
- 色: 43,046,721
"""


"""
"""
