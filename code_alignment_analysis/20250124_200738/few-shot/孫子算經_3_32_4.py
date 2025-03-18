"""
今有出門望見九堤，堤有九木，木有九枝，枝有九巢，巢有九禽，禽有九雛，雛有九毛，毛有九色。問：各幾何？
術曰：置九堤以九乘之，得木之數；又以九乘之，得枝之數；又以九乘之，得巢之數；又以九乘之，得禽之數；又以九乘之，得雛之數；又以九乘之，得毛之數；又以九乘之，得色之數。
答曰：木 a枝 ， b 巢， c 禽， d 雛， e 毛， f 色， g 。
"""

#----- content starts here -----
"""
Suppose one goes out and sees 9 dikes. Each dike has 9 trees, each tree has 9 branches, each branch has 9 nests, each nest has 9 birds, each bird has 9 chicks, each chick has 9 feathers, and each feather has 9 colors.
Question: how many of each are there?

The procedure says: Place the 9 dikes and multiply by 9, obtaining the number of trees.
Then multiply by 9 again, obtaining the number of branches.
Then multiply by 9 again, obtaining the number of nests.
Then multiply by 9 again, obtaining the number of birds.
Then multiply by 9 again, obtaining the number of chicks.
Then multiply by 9 again, obtaining the number of feathers.
Then multiply by 9 again, obtaining the number of colors.

Answer: *a* trees, *b* branches, *c* nests, *d* birds, *e* chicks, *f* feathers, *g* colors.
"""
#NO_ERR

# 置九堤
堤 = 9

# 以九乘之，得木之數
木 = 堤 * 9

# 又以九乘之，得枝之數
枝 = 木 * 9

# 又以九乘之，得巢之數
巢 = 枝 * 9

# 又以九乘之，得禽之數
禽 = 巢 * 9

# 又以九乘之，得雛之數
雛 = 禽 * 9

# 又以九乘之，得毛之數
毛 = 雛 * 9

# 又以九乘之，得色之數
色 = 毛 * 9

# Assign results
a = 木
b = 枝
c = 巢
d = 禽
e = 雛
f = 毛
g = 色#----- content ends here -----

"""
"""
