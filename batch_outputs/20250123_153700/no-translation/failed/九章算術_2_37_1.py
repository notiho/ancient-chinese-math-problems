"""
今有出錢五百七十六，買竹七十八箇。欲其大小率之，問︰各幾何？
其率術曰：各置所買石、鈞、斤、兩以為法，以所率乘錢數為實，實如法而一。不滿法者反以實減法，法賤實貴。
荅曰：其 a箇 ，箇 b錢 。其 c箇 ，箇 d錢 。
"""

"""
This problem involves dividing 576 coins among 78 bamboo pieces, with the goal of determining the number of bamboo pieces of different sizes (likely large and small) and their respective costs. Let's solve it step by step according to the procedure provided.


"""


# 出錢五百七十六
錢數 = 576

# 買竹七十八箇
竹數 = 78

# 假設大小竹的比例為大竹 2 錢，小竹 1 錢 (根據題意的大小率)
大竹率 = 2
小竹率 = 1

# 各置所買石、鈞、斤、兩以為法
法 = 大竹率 + 小竹率

# 以所率乘錢數為實
大竹實 = 錢數 * 大竹率
小竹實 = 錢數 * 小竹率

# 實如法而一
大竹數 = 大竹實 // 法
小竹數 = 小竹實 // 法

# 不滿法者反以實減法，法賤實貴
剩餘錢 = 錢數 - (大竹數 * 大竹率 + 小竹數 * 小竹率)

# 調整數量以滿足剩餘錢
if 剩餘錢 > 0:
    小竹數 += 剩餘錢 // 小竹率

# 結果
a = 大竹數
b = 大竹率
c = 小竹數
d = 小竹率


"""


### Explanation:
1. The "法" is the sum of the rates for large and small bamboo pieces.
2. The total money is divided proportionally based on the rates.
3. Any remaining money is adjusted by increasing the count of smaller bamboo pieces, as they are cheaper.

This gives the number of large and small bamboo pieces (`a` and `c`) and their respective costs per piece (`b` and `d`).
"""


"""
Variable 'a' has wrong value. Expected: 48, Actual: 384
Variable 'b' has wrong value. Expected: 7, Actual: 2
Variable 'c' has wrong value. Expected: 30, Actual: 192
Variable 'd' has wrong value. Expected: 8, Actual: 1"""
