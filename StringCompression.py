def compress(char_list):
    slow,fast=0,0
    while fast<len(char_list):
        char_list[slow]=char_list[fast]
        count=1
        while fast+1<len(char_list) and char_list[fast+1]==char_list[fast]:
            fast+=1
            count+=1
        if count>1:
            for c in str(count):
                char_list[slow+1]=c
                slow+=1
        fast+=1
        slow+=1
    return char_list[:slow]
char_list=['a','b','c','c']
res=compress(char_list)
print(res)