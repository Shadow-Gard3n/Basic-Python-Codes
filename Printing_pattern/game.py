def main(): 

    a = input("What do you want for your pattern: ")
    z = int(input("Select the number 1 for trianglular pattern, 2 for rectangular pattern and 3 for diamond pattern: "))
    if z ==2 or z == 1:
        n = int(input("How many lines of pattern do you want the pattern: "))
    if z == 3:
        n = int(input("How many lines of pattern do you want the pattern(❗❗Please enter only odd number as it is diamond❗❗): "))
        if n%2 == 0:
            print(" ❌❌Wrong input,please try again❌❌ ")
            
            main()
        else:
            pass

    m = n
    if z == 1:
        for b in range(1,n*2,2):
            print(" "*int((n-b/2-1/2)),a*b)

    elif z == 2 and n>=4:
        print(a*n)
        d=1
        for d in range(2,n):
            print(a," "*(n-4),a)
            d +=1
        print(a*n)
    elif z == 2 and n == 3:
        print(a*n)
        print(a, a)
        print(a*n)
    elif z == 2 and n == 2:
        print(a*n)
        print(a*n)
    elif z == 2 and n == 1:
        print(a)
        
    
    
    elif z == 3:
        for f in range(1,n+1,2):
            print(" "*int((n-f)/2),a*f)
        while n>=1:
            n = n-2
            print(" "*int((m-n)/2),n*a)
main()
t = input("Press 1 if you want to retry and 2 if you want to end this: ")
if t == '1':
    main()
elif t == '2':
    exit()
else:
    print("❗❗Wrong choice so ending the program❗❗")
    exit()


        

    
    
    

