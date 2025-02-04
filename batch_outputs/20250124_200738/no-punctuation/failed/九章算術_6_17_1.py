"""
今有五人分五錢令上二人所得與下三人等問各得幾何
術曰置錢錐行衰并上二人為九并下三人為六六少於九三以三均加焉副并為法以所分錢乘未并者各自為實實如法得一錢
荅曰甲得 a錢 乙得 b錢 丙得 c錢 丁得 d錢 戊得 e錢 
"""

#----- content starts here -----
"""
Suppose there are 5 people dividing 5 qian (coins). 
The top two people together should receive the same amount as the bottom three people together.
Question: how much does each person receive?

The procedure says: Arrange the qian in a tapered sequence (decreasing order).
Combine the top two people, obtaining 9, and combine the bottom three people, obtaining 6.
The bottom three are less than the top two by 3. Distribute this difference equally among the three.
Add this adjustment to the sequence, and sum them to obtain the divisor.
Multiply the total qian by the unadjusted sequence for each person, obtaining the dividend.
Divide the dividend by the divisor to find the amount of qian each person receives.

Answer: Person A (甲) receives *a* qian, Person B (乙) receives *b* qian, Person C (丙) receives *c* qian, Person D (丁) receives *d* qian, and Person E (戊) receives *e* qian.
"""

# 置錢錐行衰
錢序列 = [5, 4, 3, 2, 1]

# 并上二人為九
上二人 = 錢序列[0] + 錢序列[1]

# 并下三人為六
下三人 = 錢序列[2] + 錢序列[3] + 錢序列[4]

# 六少於九三，以三均加焉
差額 = 上二人 - 下三人
調整 = Fraction(差額, 3)

# 加調整至下三人
錢序列[2] += 調整
錢序列[3] += 調整
錢序列[4] += 調整

# 副并為法
法 = sum(錢序列)

# 以所分錢乘未并者
總錢 = 5
實 = [總錢 * i for i in 錢序列]

# 各自為實，實如法得一錢
a, b, c, d, e = [Fraction(i, 法) for i in 實]#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 4/3, Actual: 25/18
Variable 'b' has wrong value. Expected: 7/6, Actual: 10/9
Variable 'c' has wrong value. Expected: 1, Actual: 10/9
Variable 'e' has wrong value. Expected: 2/3, Actual: 5/9"""
