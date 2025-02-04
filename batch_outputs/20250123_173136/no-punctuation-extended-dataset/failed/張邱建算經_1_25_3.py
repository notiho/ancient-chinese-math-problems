"""
今有與人錢初一人與三錢次一人與四錢次一人與五錢以次與之轉多一錢與訖還歛聚與均分之人得一百錢問人㡬何
術曰置人得錢數以減初人錢數餘倍之以轉多錢數加之得人數
答曰 a人
"""

"""
Suppose there is a situation where a person gives money to others. 
Initially, the first person is given 3 qian, the next person is given 4 qian, the next person is given 5 qian, and so on, with each subsequent person receiving 1 qian more than the previous one.
After distributing the money, the total amount is collected back and evenly divided among the people, with each person receiving 100 qian.
Question: how many people are there?

The procedure says: Place the amount of money each person receives.
Subtract the amount given to the first person.
Multiply the remainder by the amount by which the money increases for each subsequent person.
Add the result to the initial amount, obtaining the number of people.

Answer: there are *a* people.
"""

# 每人得一百錢
每人得錢 = 100

# 初一人與三錢
初人錢數 = 3

# 轉多一錢
轉多錢數 = 1

# 置人得錢數，以減初人錢數
餘 = 每人得錢 - 初人錢數

# 餘倍之以轉多錢數
餘倍 = 餘 / 轉多錢數

# 加之得人數
a = 餘倍 + 1
"""
Variable 'a' has wrong value. Expected: 195, Actual: 98.0"""
