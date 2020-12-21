import random
list_1 = list(range(1,100))
list_a = random.sample(list_1,k = 20)

def selection_sort(a):
    for j in range(len(a)-1):
        minimum = j 
        for i in range(j+1, len(a)): 
            if(a[i]<a[minimum]):
                minimum = i 
        a[j],a[minimum]=a[minimum],a[j] 
    print("after selection sort:")
    print(a)

print("Given array is")
print(list_a)
selection_sort(list_a)