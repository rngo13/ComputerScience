import random
r = random.randrange (0,10)
# the zerio is inclusive and the 10 is exclusive
# 0<= result < 10
print(r)


p= random.random()
if p < .25:
    print("success")
else:
    print("fail!")
print(p)