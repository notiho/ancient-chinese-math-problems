"""
今有出錢五百七十六，買竹七十八箇。欲其大小率之，問︰各幾何？
其率術曰：各置所買石、鈞、斤、兩以為法，以所率乘錢數為實，實如法而一。不滿法者反以實減法，法賤實貴。
荅曰：其 a箇 ，箇 b錢 。其 c箇 ，箇 d錢 。
"""

"""
This problem involves dividing 576 coins among 78 bamboo items, with the goal of determining the price per bamboo item based on their size or quality. The problem suggests there are two types of bamboo items (e.g., large and small) and provides a method to calculate their respective quantities and prices.

Here is the solution encoded in Python:


"""

#----- content starts here -----

from fractions import Fraction

# 出錢五百七十六
總錢數 = 576

# 買竹七十八箇
總竹數 = 78

# 假設大竹和小竹的價格比例為 2:1
大竹價格比例 = 2
小竹價格比例 = 1

# 計算總比例
總比例 = 大竹價格比例 + 小竹價格比例

# 計算每單位比例的竹數
每單位竹數 = 總竹數 / 總比例

# 計算大竹和小竹的數量
大竹數 = 每單位竹數 * 大竹價格比例
小竹數 = 每單位竹數 * 小竹價格比例

# 計算每箇竹的價格
每箇大竹價格 = 總錢數 / (大竹數 * 大竹價格比例 + 小竹數 * 小竹價格比例) * 大竹價格比例
每箇小竹價格 = 總錢數 / (大竹數 * 大竹價格比例 + 小竹數 * 小竹價格比例) * 小竹價格比例

# 輸出結果
a = 大竹數
b = 每箇大竹價格
c = 小竹數
d = 每箇小竹價格

print(f"其 {a} 箇，箇 {b} 錢。其 {c} 箇，箇 {d} 錢。")
#----- content ends here -----


"""


### Explanation of the Code:
1. **Input Values**:
   - `總錢數` is the total money spent (576 coins).
   - `總竹數` is the total number of bamboo items purchased (78 items).
   - The price ratio between large and small bamboo items is assumed to be 2:1.

2. **Proportional Distribution**:
   - The total ratio is calculated as the sum of the price ratios for large and small bamboo items.
   - The number of bamboo items for each type is calculated based on the total ratio.

3. **Price Calculation**:
   - The price per bamboo item is calculated proportionally based on the total money and the price ratio.

4. **Output**:
   - The number of large bamboo items (`a`) and their price per item (`b`).
   - The number of small bamboo items (`c`) and their price per item (`d`).

This approach follows the proportional distribution method described in the problem. Let me know if you need further clarification or adjustments!
"""


"""
Variable 'a' has wrong value. Expected: 48, Actual: 52.0
Variable 'b' has wrong value. Expected: 7, Actual: 8.861538461538462
Variable 'c' has wrong value. Expected: 30, Actual: 26.0
Variable 'd' has wrong value. Expected: 8, Actual: 4.430769230769231"""
