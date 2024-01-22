string=input()
start=0
end=0
max_len=0
unq_char=set()

while end<len(string):
    if string[end] not in unq_char:
        unq_char.add(string[end])
        max_len=max(max_len,end-start+1)
        end+=1
    else:
        unq_char.remove(string[start])
        start+=1
print(max_len)