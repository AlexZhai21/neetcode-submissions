class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        h = len(matrix) 
        w = len(matrix[0]) #numbers per row
        l = 0
        r = h - 1
        while l <= r:
            m_r = l + ((r - l + 1) // 2)
            if matrix[m_r][0] <= target <= matrix[m_r][w - 1]: #this means the target, if its in this matrix, would be in this row
                for i in matrix[m_r]:
                    if i == target:
                        return True
                return False
            elif target > matrix[m_r][w-1]: #this means its in the greater half
                l = m_r + 1
            else:
                r = m_r - 1
        return False
    