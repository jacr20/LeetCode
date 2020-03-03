class Solution:
    '''Simple algorithm to iterate through the list finding the elements which sum to the target.'''
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index = []
        for i in range(len(nums)):
            for j in range((i+1), len(nums)):
                if  nums[i] + nums[j] == target:
                    index.append(i)
                    index.append(j)
        
        return index



    def twoSum_ideal(nums, target):
        '''Creates key-value pair of the number and the index, if the difference between any subsequent numbers in the array and the target is in the dictionary, it's index can quickly be identified.'''
        h = {}
        for i, num in enumerate(nums):
            n = target - num
            if n not in h:
                h[num] = i
            else:
                return [h[n], i]

if __name__ == '__main__':
    print(Solution.twoSum(nums = [2,15,11,7],target =  9))
    print(Solution.twoSum_ideal(nums = [2,15,11,7],target =  9))

    
