class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {} #val :index
        for i, n in enumerate(nums): #going through each number in list
            needed = target - n # the target minus the number in the list
            if needed in seen:
                return[seen[needed], i] #returns numbers locations
            seen[n] = i #if not seen previous, add that too our list
        return


                

        