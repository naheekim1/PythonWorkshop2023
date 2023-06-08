import simpleClass
import random
import math
import time
#from math import floor
#from math import *

def main():
    obj = simpleClass.CoolClass()
    print(obj.val)
    print(simpleClass.sub1(5))
    print(simpleClass.coolConstant)
    
    print(math.ceil(5.5))
    print(math.floor(5.5))
    print(math.e)
    print(math.pi)

    print(random.randrange(1, 6))
    print(random.random())
    print(random.choice([1, 3, 5, 6]))
    lst = [1, 2, 3]
    random.shuffle(lst)
    print(lst)

    print(time.time())
    print(time.localtime())
    print(time.localtime().tm_mon)
    print(time.ctime())

main()