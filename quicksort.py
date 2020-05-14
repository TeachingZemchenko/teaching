from random import randint
import time
def partition(arr,left,right,road):
    #print(arr,left,right)
    o_ind=(left+right)//2
    o_val=arr[o_ind]
    #print(o_ind,o_val)
    i=left-1
    while (i<right-1):
        i+=1
        if (i==o_ind):
            continue
        if (arr[i]>=o_val and i<o_ind):
            #print('>',arr[i])
            arr.insert(right-1,arr.pop(i))
            if (i<o_ind):
                o_ind-=1
            i-=1
        elif (arr[i]<o_val and i>o_ind):
            #print('<',arr[i])
            arr.insert(left,arr.pop(i))
            if (i>o_ind):
                o_ind+=1
            i-=1
    #print(o_ind,arr[o_ind])
    return o_ind
def quicksort(arr,left,right,road):
    #time.sleep(2)
    #print(road)
    #if (road=='left'):
    #    print(arr)
    if (right-left) in [0,1]:
        return arr
    o_ind1=partition(arr,left,right,road)
    #if (road=='start'):
        #print(arr,o_ind1)
    #return 0
    #print('arr2')
    #print(arr)
    #print('part_2',o_ind1+1,right)
    #o_ind2=partition(arr,o_ind1+1,right)#right
    #print('arr3')
    #print(arr)
    #print('part_3',left,o_ind1)
    #o_ind3=partition(arr,left,o_ind1)#left
    #print('arr4')
    #print(arr)
    #return 0
    lsort=quicksort(arr,left,o_ind1,'left'+str(o_ind1))
    rsort=quicksort(arr,o_ind1+1,right,'right'+str(o_ind1+1))
    return arr

#arr=[-70, 192, 172, -56, 641, 642, 386, 572, 589, 314, 941, 314, 140, 114, 153, 740, 513, 90, 175, 698]
#print(arr)
#quicksort(arr,0,len(arr),'start')
#print(arr)
#//
arr2= [randint(-100, 1000) for i in range(1000)]
print(arr2)
times=time.time()
quicksort(arr2,0,len(arr2),'start')
print(time.time()-times)
print(arr2)



























