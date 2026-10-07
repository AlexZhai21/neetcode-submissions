class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        h = len(matrix) 
        w = len(matrix[0]) #numbers per row
        l = 0
        r = h - 1
        while l <= r:
            m_r = l + ((r - l + 1) // 2)
            if matrix[m_r][0] <= target <= matrix[m_r][w - 1]: #this means the target, if its in this matrix, would be in this row
                l_ans = 0
                r_ans = w - 1
                while l_ans <= r_ans:
                    m_ans = l_ans + ((r_ans - l_ans + 1) //2)
                    if matrix[m_r][m_ans] == target:
                        return True
                    elif matrix[m_r][m_ans] > target:
                        r_ans = m_ans - 1
                    else:
                        l_ans = m_ans + 1
                return False
            elif target > matrix[m_r][w-1]: #this means its in the greater half
                l = m_r + 1
            else:
                r = m_r - 1
        return False
    