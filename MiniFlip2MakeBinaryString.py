def minFlips(s):
    n = len(s)
    s+=s
    alt1,alt2='',''
    for i in range(len(s)):
        alt1+='0' if i%2 else'1'
        alt2+='1' if i%2 else'0'
    left,right =0 ,0 
    diff1,diff2=0,0
    res=len(s)
    for right in range(len(s)):
        if s[right]!=alt1[right]:
            diff1+=1
        if s[right]!=alt2[right]:
            diff2+=1
        if right-left+1>n:
            if s[left]!=alt1[left]:
                diff1-=1
            if s[left]!=alt2[left]:
                diff2-=1
            left+=1
        if right-left+1==n:
            res=min(res,diff2,diff1)
    return res
s='111000'
res=minFlips(s)
print(res)