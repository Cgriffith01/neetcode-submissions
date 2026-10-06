class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #dictionary to track how many times each number appears
        count = {} 
        # list of empty buckets, one for every possible count from 0 to len(nums)
        freq = [[] for i in range(len(nums) + 1)]
        
        # go through every number in the input list
        for n in nums:
        # add 1 to its count, starting from 0 if we haven't seen it yet
            count[n] = 1 + count.get(n, 0)

        # go through each number and its total count
        for n, c in count.items():
            # drop the number into the bucket that matches its count
            freq[c].append(n)

        # empty list to hold the final answer
        res = []

        # walk the buckets backwards, from highest count down to 1
        for i in range(len(freq) - 1, 0, -1):
            # go through each number sitting in this bucket
            for n in freq[i]:
                # add the number to the answer
                res.append(n)
                # once we have k numbers, we're done
                if len(res) == k:
                # return the answer and exit the function
                    return res

            





        