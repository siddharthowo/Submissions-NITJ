class Sorting():
    def __init__(self,data):
        self.l=data
        self.len=len(data)

    def bubblesort(self):
        for i in range(self.len):
            for j in range(0,self.len-i-1):
                if self.l[j]>self.l[j+1]:
                    self.l[j],self.l[j+1]=self.l[j+1],self.l[j]

    def insertionsort(self):
        for i in range(1,self.len):
            k=self.l[i]
            j=i-1
            while j>=0 and self.l[j]>k:
                self.l[j+1]=self.l[j]
                j-=1
            self.l[j+1]=k

    def selectionsort(self):
        for i in range(self.len-1):
            min_i=i
            for j in range(i+1,self.len):
                if self.l[j]<self.l[min_i]:
                    min_i=j
            if min_i!= i:
                self.l[i],self.l[min_i] = self.l[min_i],self.l[i]

    def mergesort(self):
        self.merge_sort(0,self.len-1)

    def merge_sort(self,left,right):
        if left<right:
            mid=(left+right)//2
            self.merge_sort(left,mid)
            self.merge_sort(mid+1,right)
            self.merge(left,mid,right)

    def merge(self,left,mid,right):
        temp=[]
        i,j=left,mid+1
        while i<=mid and j<=right:
            if self.l[i]<=self.l[j]:
                temp.append(self.l[i])
                i+=1
            else:
                temp.append(self.l[j])
                j+=1

        while i<=mid:
            temp.append(self.l[i])
            i+=1

        while j<=right:
            temp.append(self.l[j])
            j+=1

        for k in range(len(temp)):
            self.l[left+k]=temp[k]   

    def quicksort(self):
        self.quick_sort(0, self.len - 1)

    def quick_sort(self, low, high):
        if low<high:
            pivot= self.partition(low,high)
            self.quick_sort(low,pivot-1)
            self.quick_sort(pivot+1,high)

    def partition(self, low, high):
        pivot =self.l[high]
        i=low-1
        for j in range(low,high):
            if self.l[j]<=pivot:
                i += 1
                self.l[i],self.l[j]=self.l[j],self.l[i]

        self.l[i+1],self.l[high]=self.l[high],self.l[i+1]
        return i+1

    def heapsort(self):
        n = self.len

        for i in range(n//2-1,-1,-1):
            self.heapify(n,i)

        for i in range(n-1,0,-1):
            self.l[0],self.l[i]=self.l[i],self.l[0]
            self.heapify(i, 0)

    def heapify(self,n,i):
        largest=i
        left=2*i+1
        right=2*i+2

        if left<n and self.l[left]>self.l[largest]:
            largest=left
        if right<n and self.l[right]>self.l[largest]:
            largest=right

        if largest!=i:
            self.l[i],self.l[largest]=self.l[largest],self.l[i]
            self.heapify(n,largest)
                    

x=[5,4,9,1,0,-4,3,2]
arr=Sorting(x)
arr.mergesort()
print(arr.l)


