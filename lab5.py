import random
import time
num_list= [random.randint(1,100000) for i in range(100000)]

'''顺序检索
时间复杂度：O(n)
优点：数据存储可以无序，插入元素可以直接加在表尾
缺点：检索时间长
'''
def direct_search(key):
    for i in range(len(num_list)):
        if(num_list[i] == key):
            print(i)

'''二分检索
时间复杂度：O(log(n))
优点：比较次数少，检索速度快
缺点：需要按照关键码排序，不易更新
'''
def binarySearch(key):
    low,high = 0,len(num_list)-1
    while(low<=high):
        mid = (low+high)//2
        if num_list[mid]==key:
            print("找到目标，索引号是:",mid)
            break
        else:
            if num_list[mid]<key:
                low,high =mid+1,high
            else:
                low,high =low,mid-1
    else:
        print("未找到")

start1 = time.time()
for i in range(100):
    direct_search(random.randint(1,100000))
end1  = time.time()
num_list.sort()
start2 = time.time()
for i in range(100):
    binarySearch(random.randint(1,100000))
end2  = time.time()
print("\n在长度为100000，取值为1~100000的序列中：")
print("100次直接检索用时",end1-start1,"秒")
print("100次二分法检索用时",end2-start2,"秒")