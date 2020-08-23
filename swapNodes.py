#!/bin/python3

import os
import sys

#
# Complete the swapNodes function below.
#
sys.setrecursionlimit(1500) 
def swapNodes(indexes, queries):
    #
    # Write your code here.
    #
    class Node:
        def __init__(self,val,level):
            self.val =val 
            self.level =level
            self.left=self.right=None

    def inorder(root):
        if root.left:
            inorder(root.left)
        item.append(root.val)
        if root.right:
            inorder(root.right)

    def swap(tree, ks):
        if tree.left:
            swap(tree.left, ks)
        if tree.right:
            swap (tree.right, ks)
        if tree.level in ks:
            tree.left, tree.right = tree.right, tree.left
        return tree

    def buildTree(indexes):
        from queue import Queue
        q = Queue()
        root =Node(1,1)
        maxLevel =1
        q.put(root)
        for left, right in indexes:
            cur =q.get()
            if left!=-1:
                leftNode = Node(left, cur.level+1)
                cur.left =leftNode
                q.put(leftNode)
            if right!=-1:
                rightNode = Node(right, cur.level+1)
                cur.right =rightNode
                q.put(rightNode)
            maxLevel =cur.level
        return (root,maxLevel)

    tree, maxLevel =buildTree(indexes)
    print(maxLevel)
    res= []
    for k in queries:
        item =[]
        ks =[x for x in range(1, maxLevel+1) if x%k==0 ]
        tree= swap(tree,ks)
        inorder(tree)
        res.append(item)
    return res
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    indexes = []

    for _ in range(n):
        indexes.append(list(map(int, input().rstrip().split())))

    queries_count = int(input())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input())
        queries.append(queries_item)

    result = swapNodes(indexes, queries)

    fptr.write('\n'.join([' '.join(map(str, x)) for x in result]))
    fptr.write('\n')

    fptr.close()

