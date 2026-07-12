class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        # using the coordinate trick ! 
        matrix = matrix 
        target = target 
        left = 0
        right = len(matrix) * len(matrix[0]) - 1 
        
        C= len(matrix[0])

        while  left <= right: 

            mid = left + (right-left) // 2 
            # covert this into martix indices: 

            if target == matrix[mid // C ][mid % C]:
                return True
            elif target > matrix[mid // C ][mid % C ]:
                left = mid + 1
            else: 
                right = mid - 1 
        
        return False
