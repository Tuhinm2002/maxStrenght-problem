def factorial(num):
    if num==1 or num==0:
        return num
    else:
        return num*factorial(num-1)

def mamx(x):
    b=0
    for a in x:
        n.append(int(a)) #important line for examples like (64,45,4) or (64,8,4)
    for k in n:
        t = factorial(k)
        arr.append(t)
    if len(arr)==1:
        print(arr[0])
    else:
        for ks in range(len(arr)-1):
             b=arr[ks]+arr[ks+1]
    return b
def maxStrenght():
    # s=0
    while True:
        x = int(input("enter a num"))
        x = str(x)
        if (int(x) in arr) or (int(x) in n) or (x in arr1):
            break
        else:
            arr1.append(x)
            mamx(x)



arr=[]
n = []
arr1=[]
fact=[]
i=0
maxStrenght()
print("The maximum strenght",max(arr))






