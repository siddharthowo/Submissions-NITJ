#implementing linear, binary and fibonacci search

class Searching:
    def __init__(self,data):
        self.l=data
        self.length=len(data)

    def display(self):
        print(self.l)

    def linear_search(self,d):
        for idx,i in enumerate(self.l):
            if i==d:
                return 1,idx
        return 0,-1

    def binary_search(self,d):
        low=0
        high=self.length-1
        while(low<=high):
            mid=(low+high)//2
            if self.l[mid]==d:
                return 1,mid
            if self.l[mid]>d:
                high=mid-1
            else:
                low=mid+1
        return 0,-1

    def fibonacci_search(self,d):
        a=0
        b=1
        c=1

        offset=-1

        while(c<self.length):
            a=b
            b=c
            c=a+b

        while(c>1):
            i=min(offset+a,self.length-1)
            if(self.l[i]==d):
                return 1,i
            elif(self.l[i]<d):
                c=b
                b=a
                a=c-b
                offset=i
                print("\noff:",offset,"a b c:",a,b,c)
            else:
                c=a
                b=b-a
                a=c-b
        if(b==1 and self.l[offset+1]==d):
            return 1,offset+1
        return 0,-1

l1=Searching([1,2,3,4,5])
l1.display()
f,i=l1.fibonacci_search(3)
if (f):
    print("Found at index:",i)
else:
    print("Not found")

