class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # rows check, use a set and add each value, if you add a dupe return false
        for i in board: # grabs first row
            seen = set()
            for n in i:
                if n != ".":
                    if n in seen:
                        return False
                    else:
                        seen.add(n)
        # col check
        for i in range(len(board)):
            seen = set()
            for n in range(len(board[i])):
                if board[n][i] != ".":
                    if board[n][i] in seen:
                        return False
                    else:
                        seen.add(board[n][i])
        # 3x3 check
        # Each band is split (for rows) by 3, so iterate each row of bands and step by 3. then just do a range of 3 for rows.
        for i in range(0, len(board), 3):
            for n in range(0, len(board), 3):
                seen = set()
                #single box check
                for dr in range(3):
                    for dc in range(3):
                        if board[i+dr][n+dc] != ".":
                            if board[i+dr][n+dc] in seen:
                                return False
                            else:
                                seen.add(board[i+dr][n+dc])
        return True
