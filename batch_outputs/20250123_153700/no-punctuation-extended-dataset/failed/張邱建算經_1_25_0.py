"""
今有與人錢初一人與三錢次一人與四錢次一人與五錢以次與之轉多一錢與訖還歛聚與均分之人得一百錢問人㡬何
術曰置人得錢數以減初人錢數餘倍之以轉多錢數加之得人數
答曰 a人
"""

"""
Suppose there is a situation where a person gives money to others. 
To the first person, they give 3 qian, to the second person, they give 4 qian, to the third person, they give 5 qian, and so on, increasing the amount given by 1 qian each time.
After giving money to all, they collect the money back and evenly distribute it among the people, such that each person receives 100 qian.
Question: how many people are there?

The procedure says: Place the amount of money each person receives (100 qian).
Subtract the amount given to the first person (3 qian).
Multiply the remainder by the rate of increase in the amount given (1 qian per person).
Add the result to the amount given to the first person (3 qian).
This gives the number of people.

Answer: *a* people.
"""

# 每人得錢數
每人得錢數 = 100

# 初人與三錢
初人錢數 = 3

# 轉多一錢
轉多錢數 = 1

# 以減初人錢數
餘 = 每人得錢數 - 初人錢數

# 餘倍之以轉多錢數
餘倍 = 餘 * 轉多錢數

# 加之得人數
a = 餘倍 + 初人錢數
"""
Variable 'a' has wrong value. Expected: 195, Actual: 100"""
