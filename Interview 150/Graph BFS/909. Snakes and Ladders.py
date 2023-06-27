import collections


import collections

class Solution:
    def snakesAndLadders(self, board: list[list[int]]) -> int:
        q = collections.deque()
        coords = {}
        n = len(board)
        pos = 1
        visited = set()

        step = 0
        counter = 1
        # set up board mappings
        for i in range(n-1, -1, -1):
            step += 1
            for j in range(n):
                if step % 2 != 0:
                    coords[counter] = i, j
                else:
                    coords[counter] = i, n-j-1
                counter += 1

        q.append([pos])

        while q:
            # get the first path from the queue
            path = q.popleft()

            # get the last node from the path
            node = path[-1]

            # path found
            if node >= n**2:
                return len(path)-1
            elif node in visited:
                continue
            visited.add(node)

            # enumerate all adjacent nodes, construct a 
            # new path and push it into the queue
            moves = list(range(node + 1, min(node + 6, n**2)+1))
            moveValues = []

            for item in moves:
                x, y = coords.get(item)
                coordValue = board[x][y]
                temp = path.copy()

                if coordValue != -1:
                    temp.append(coordValue)
                    moveValues.append(coordValue)
                    q.append(temp)
                else:
                    temp.append(item)
                    moveValues.append(item)
                    q.append(temp)
            # print('jumps', q)
            # break

        return -1

class Solution2:
    def snakesAndLadders(self, board: list[list[int]]) -> int:
        q = collections.deque()
        coords = {}
        n = len(board)
        pos = 1
        visited = set()

        step = 0
        counter = 1
        # set up board mappings
        # for i in range(n-1, -1, -1):
        #     step += 1
        #     for j in range(n):
        #         if step % 2 != 0:
        #             coords[counter] = i, j
        #         else:
        #             coords[counter] = i, n-j-1
        #         counter += 1

        q.append([(n-1, 0, 1)])

        while q:
            # get the first path from the queue
            path = q.popleft()

            # get the last node from the path
            node = path[-1]

            nodeVal = node[2]

            # path found
            if nodeVal >= n**2:
                return len(path)-1
            elif nodeVal in visited:
                continue
            visited.add(nodeVal)

            # enumerate all adjacent nodes, construct a 
            # new path and push it into the queue
            moves = list(range(1, min(6, n**2)+1))

            for item in moves:
                dy, dx = divmod(item, n)
                level, _ = divmod(item-1, n)
                if level % 2 == 0:
                    y = node[1] + dx
                else:
                    y = n - dx - 1
                x = node[0] - dy
                # x, y = coords.get(item)
                coordValue = board[x][y]
                temp = path.copy()
                print(item, node, x,y,dx,dy, coordValue)

                if coordValue != -1:
                    temp.append((x, y, coordValue))
                    q.append(temp)
                else:
                    temp.append((x, y, item))
                    q.append(temp)
            # print('jumps', q)
            # break

        return -1


a = [[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,15,-1,-1,-1,-1]]
# b = [[1,1,-1],[1,1,1],[-1,1,1]]
# c = [[-1,1,2,-1],[2,13,15,-1],[-1,10,-1,-1],[-1,6,2,8]]
# d = [[-1,-1],[-1,3]]
# e = [[-1,-1,2,-1],[14,2,12,3],[4,9,1,11],[-1,2,1,16]]

tests = [a]

for i in tests:
    a = Solution2().snakesAndLadders(i)
    print(a)  
    print()