from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        left_max = height[left]
        right_max = height[right]
        water = 0

        while left < right:
            if left_max < right_max:
                left += 1
                left_max = max(left_max, height[left])
                water += left_max - height[left]
            else:
                right -= 1
                right_max = max(right_max, height[right])
                water += right_max - height[right]
        
        return water


if __name__ == '__main__':
    solution = Solution()

    height = [0,1,0,2,1,0,1,3,2,1,2,1]
           #
       #   ## #
     # ## ######
    print(solution.trap(height)) # 6

    height = [4,2,0,3,2,5]
    print(solution.trap(height)) # 9

    height = [0,1,0,1,0]
    print(solution.trap(height)) # 1

    height = [1,0,1]
    print(solution.trap(height)) # 1

    height = [0,1,0,1,0,1,0]
    print(solution.trap(height)) # 2
    
    height = [0,2,0,1,0,1,0,1,0]
    print(solution.trap(height)) # 3

    height = [0,1,0,0,1,0]
    print(solution.trap(height)) # 2

    height = [0,2,0,0,1,0,1,0,1,0]
    print(solution.trap(height)) # 4

    height = [2,1,0,2]
    print(solution.trap(height)) # 3

    height = [5,4,1,2]
    #
    ##
    ##
    ## #
    ####
    print(solution.trap(height)) # 1

    height = [4,9,4,5,3,2]
     #     
     #
     #
     #
     # #
    ####
    #####
    ######
    ######
    print(solution.trap(height)) # 1

    height = [9,6,8,8,5,6,3,8]
    #      
    # ##   #
    # ##   #
    #### # #
    ###### #
    ###### #
    ########
    ########
    ########
    print(solution.trap(height)) # 12

    height = [9,6,8,8,5,6,3]
    #     
    # ##
    # ##
    #### #
    ######
    ######
    #######
    #######
    #######
    print(solution.trap(height)) # 3
