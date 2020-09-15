rooms = [[2147483647, -1, 0, 2147483647],
[2147483647,2147483647,2147483647,-1],
[2147483647,-1,2147483647,-1],
[0,-1,2147483647,2147483647]
]

def bfs(rooms):
  sol =rooms.copy()
  if not sol:
    return sol
  n, m =len(sol),len(sol[0])
  front =[(r,c) for r in range(n) for c in range(m) if sol[r][c]==0]
  print(front)
  dr, dc=[1,0,-1,0],[0,1,0,-1]
  distance =0 
  while front:
    next =[]
    for r, c in front: 
      for i in range(4):
        nr,nc= r+dr[i], c+dc[i] #index
        print(nr,nc)
        if 0<=nr<n and 0<=nc<m and sol[nr][nc]== 2147483647:
          sol[nr][nc]=distance + 1
          next.append((nr,nc))
    front= next
    distance+=1

  return sol

print(bfs(rooms))
