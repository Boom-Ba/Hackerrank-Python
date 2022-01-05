def uniquenumBST(n):
    if n<=1:
        return 1
    sum=0
    leftNumNodes,rightNumNodes=0,0
    for root in range(1,n+1):
        leftNumNodes =uniquenumBST(root-1)
        rightNumNodes=uniquenumBST(n-root)
        sum+=leftNumNodes*rightNumNodes
    return sum
res=uniquenumBST(3)
print(res)