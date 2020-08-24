from queue import Queue

n = int(input())
grid = []
for i in range(0, n):
    grid.append(list(input().strip()))

a,b,c,d = [int(x) for x in input().strip().split(' ')]

queue = Queue()
queue.put(dict(row=a, column=b, steps=0))

visited = [[False for x in range(n) ] for x in range(n)]
res = 0

while queue.qsize() > 0:
    p = queue.get()
    visited[p['row']][p['column']] = True

    if p['row'] == c and p['column'] == d:
        res = p['steps']
        break

    steps = p['steps']+1

    i = p['row']+1

    while i < n and grid[i][p['column']] == '.':
        if not visited[i][p['column']]:
            queue.put(dict(row=i, column=p['column'], steps=steps))
            visited[i][p['column']] = True
        i+=1

    i = p['row']-1
    while i>=0 and grid[i][p['column']] == '.':
        if not visited[i][p['column']]:
            queue.put(dict(row=i, column=p['column'], steps=steps))
            visited[i][p['column']] = True
        i-=1

    j = p['column']+1
    while j<n and grid[p['row']][j] == '.':
        if not visited[p['row']][j]:
            queue.put(dict(row=p['row'], column=j, steps=steps))
            visited[p['row']][j] = True
        j+=1

    j = p['column']-1
    while j>=0 and grid[p['row']][j] == '.':
        if not visited[p['row']][j]:
            queue.put(dict(row=p['row'], column=j, steps=steps))
            visited[p['row']][j] = True
        j-=1

print (res)