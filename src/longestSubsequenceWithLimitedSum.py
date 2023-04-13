class Solution(object):
    def answerQueries(self, nums, queries):
        nums.sort()
        def func(query):
            summ = 0
            for i, num in enumerate(nums):
                summ += num
                if summ > query:
                    return i
            return len(nums)

        return [func(query) for query in queries]