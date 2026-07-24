class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        # using the coordinate trick ! 

        left = 0
        right = len(matrix) * len(matrix[0]) 
        

        while  left <= right: 

            mid = left + (right-left) // 2 
            # covert this into martix indices: 

            if target == matrix[mid // len(matrix[0])][mid % len(matrix[0])]:
                return True
            elif target > matrix[mid // len(matrix[0])][mid % len(matrix[0])]:
                left = mid + 1
            else: 
                right = mid - 1 
        
        return False
