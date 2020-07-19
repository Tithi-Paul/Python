#range (a,b,c) এর মানে for(int i = a; i<b; i+=c)
def to_celsius(x):
    return (x-32)*5/9

for x in range(0, 101, 20):
    print(x, to_celsius(x))
