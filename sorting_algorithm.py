def bubble_sort(nums):
    for i in range(len(nums)-1,0,-1):
        for j in range(i):
            if nums[j]>nums[j+1]:
                temp=nums[j]
                nums[j]=nums[j+1]
                nums[j+1]=temp

# nums=[5,3,8,6,7,2]
# bubble_sort(nums)
# print(nums) 

def sel_sorts(nums):
    for i in range(len(nums)):
        minVal=i
        for j in range(i,len(nums)):
            if nums[j]<nums[minVal]:
                minVal=j
        temp=nums[i]
        nums[i]=nums[minVal]
        nums[minVal]=temp

nums=[5,3,8,6,7,2]
# sel_sorts(nums)
# print(nums)

def selection_sort(nums):
    for i in range(len(nums)):
        minVal=i
        for j in range(i,len(nums)):
            if nums[j]<nums[minVal]:
                minVal=j
        temp=nums[i]
        nums[i]=nums[minVal]
        nums[minVal]=temp
# selection_sort(nums)
# print(nums)

a=[2,6,5,1,3,4]
def insertion_sort(a):
    for i in range(1,len(a)): #1-5
        j=i #inner loop that starts at the index of outer loop
        while a[j-1]>a[j] and j>0:
            a[j-1],a[j]=a[j],a[j-1]
            j-=1 #go to the left
            
# insertion_sort(a)
# print(a)

def partition(arr,left,right):
    i=left-1
    pivot=arr[right] #choose right most element as pivot

    #loop through the arr from index left to right-1
    for j in range(left,right):
        if arr[j]<pivot:
            i+=1
            #swap elements if curr_element is less than pivot
            arr[i],arr[j]=arr[j],arr[i]
    #swap the pivot element to its correct position
    arr[i+1],arr[right]=arr[right],arr[i+1]
    return i+1 #return index of the pivot

def quick_sort(arr,left,right):
    if left<right:
        #partition array and get the pivot index
        piv=partition(arr,left,right)

        #recursively apply quick_sort on the left and right parts
        quick_sort(arr,left,piv-1) #sort elemts before pivot
        quick_sort(arr,piv+1,right) #sort elemts after pivot

arr=[3,8,6,0,4,5]
quick_sort(arr,0,len(arr)-1)
# print(arr)

# quick sort using recursion

def quick_sort(a):
    if len(a)<=1:
        return a
    
    pivot=a[len(a)//2]

    left=[x for x in a if x < pivot]
    middle=[x for x in a if x == pivot]
    right=[x for x in a if x > pivot]

    return quick_sort(left) + middle +quick_sort(right)

quick_sort(nums)
# print(nums)


def merge_sort(a):
    #base case
    if len(a)<=1:
        return a
    #divide array into 2 halves
    middle=len(a)//2
    left_half=a[:middle]
    right_half=a[middle:]

    #recursively sort both halves
    left_sorted=merge_sort(left_half)
    right_sorted=merge_sort(right_half)

    #merge 2 sorted halves
    return merge(left_sorted,right_sorted)


def merge(left,right):
    sorted_arr=[]
    i=j=0

    #merge 2 arrays while comparing their elements
    while i<len(left) and j<len(right):
        if left[i] < right[j]:
            sorted_arr.append(left[i])
            i+=1
        else:
            sorted_arr.append(right[j])
            j+=1
    #add remaining elements from the left and right halves
    sorted_arr.extend(left[i:])
    sorted_arr.extend(right[j:])

    return sorted_arr

nums=[2,4,3,3,1,1,1,8,6,7]
# print(merge_sort(nums))

def merge_two_arr(a,b):
    i=j=0
    result=[]

    while i<len(a) and j<len(b):
        if a[i]<b[j]:
            result.append(a[i])
            i+=1
        else:
            result.append(b[j])
            j+=1
    while i<len(a):
        result.append(a[i])
        i+=1
    while j<len(b):
        result.append(b[j])
        j+=1
    return result

x=[33,44,55]
y=[6,7,8]
# print(merge_two_arr(x,y))

