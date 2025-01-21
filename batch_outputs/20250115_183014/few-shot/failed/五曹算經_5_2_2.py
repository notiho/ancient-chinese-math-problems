"""
今有七百三十八户，共請絲二十七斤五两。問：户得㡬何？
術曰：列絲二十七斤，以十六两乘之、納五两，得四百三十七两；又以二十四銖乘之，得一萬四百八十八銖；以七百三十八户除之即得。
答曰： a銖 b 絫 c黍 奇 d銖 e黍 。
"""

"""
Suppose there are 738 households collectively requesting 27 jin and 5 liang of silk.
Question: how much does each household receive?

The procedure says: Write down 27 jin of silk, multiply it by 16 liang, and add 5 liang, obtaining 437 liang.
Then multiply it by 24 zhu, obtaining 10,488 zhu.
Divide this by 738 households to get the result.

Answer: *a* zhu, *b* lü, *c* shu, with a remainder of *d* zhu and *e* shu.
"""

# 列絲二十七斤
絲_斤 = 27

# 以十六两乘之、納五两
絲_兩 = (絲_斤 * 16) + 5

# 得四百三十七两
assert 結果_兩 := 437 == 結果_兩


"""
Code error: invalid syntax (<string>, line 20)"""
