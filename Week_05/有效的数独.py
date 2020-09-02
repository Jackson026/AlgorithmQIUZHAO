class Solution:
    def isValidSudoku(self, board) -> bool:
        '''
            block_index = (row/3)*3 + col/3 (0~8)
        '''

        row=[[] for i in range(9)]
        col=[[] for j in range(9)]
        block=[[] for k in range(9)]
        for i in range(9):
            for j in range(9):
                num=board[i][j]
                block_index=(i//3)*3+j//3
                if num!='.':
                    num=int(num)
                    if num not in row[i]:
                        row[i].append(num)
                    else:
                        return False
                    if num not in col[j]:
                        col[j].append(num)
                    else:
                        return False
                    if num not in block[block_index]:
                        block[block_index].append(num)
                    else:
                        return False
        return True