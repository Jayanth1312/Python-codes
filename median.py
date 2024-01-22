import statistics

list_1=list(map(int,input().split()))
list_2=list(map(int,input().split()))

new_list=list_1+list_2
new_list.sort()
print("{:.5f}".format(statistics.median(new_list)))