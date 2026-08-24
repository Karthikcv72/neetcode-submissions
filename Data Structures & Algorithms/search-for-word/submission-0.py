class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS=len(board)
        COLS=len(board[0])
        path=set()
        def backtracking(r,c,i):
            if i==len(word):
                return True
            directions=[[1,0],[-1,0],[0,1],[0,-1]]
            path.add((r,c))
            for dr,dc in directions:
                nr,nc=r+dr,c+dc
                if nr<0 or nr>=ROWS or nc<0 or nc>=COLS or (nr,nc) in path or board[nr][nc]!=word[i]:
                    continue
                if backtracking(nr,nc,i+1):
                    return True
            path.remove((r,c))
            return False
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c]==word[0]:
                    if backtracking(r,c,1):
                        return True
        return False
        
        