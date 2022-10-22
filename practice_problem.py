def isPrime(n):
    flag=True
    for i in range(2,n):
        if n%i==0:
            flag=False
            break
    return flag

def nearestprime(n):
    i=1
    while(True):
        m=n+i
        if isPrime(m):
            print(f"The nearset prime is {m}")
            break
        k=n-i
        if isPrime(k):
            print(f"The nearset prime is {k}")
            break
        i+=1
        
#nearestprime(11)  

def profit(arr):     
    l,r=0,1
    maxp=0
    while r<len(arr):
        #print(arr[l],arr[r])
        if arr[l]<arr[r]:
            profit=arr[r]-arr[l]
            maxp=max(maxp,profit)
        else:
            l=r
        r+=1
    return maxp
        
#print(profit([7,1,5,3,6,4]))     

#check if a given number is fibbonaci
def IsFibbonaci(n):
    pass
print(IsFibbonaci(4))   
    
    
    



        
        

