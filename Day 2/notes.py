def main():
    for i in range(10):
        print(i)
    # 0 to 10, excluding 10

    for i in range (3,10):
        print(i)
    # starting from 3 to 10

    for i in range (3,10, 2):
   # incrementing up by 2


    #lists, []
    x = [1, 6, 3, 4, 5]
    x[1] = 2
    print(x[3])
    print(x[0:2])
    #print 0 to 2 (exclusive)

    print(x[::2])
    # incrementing by 2
    # the whole list

    #last 2 elements use negative index
    #5 is x[4] but also x[-1]
    print(x[-2::1])
    #last 2 elements
    print()
    
    #import time
    #do something every second
    #what is current time - old time = 45 seconds (every 45 sec)

    #time.ctime --> time to string 







    #sets
    coolnumbers = {3, 10, 2 , 5, 3}
    print(coolnumbers)
    #prints 2, 3, 5, 10
    # no multiples, in order 

main()
