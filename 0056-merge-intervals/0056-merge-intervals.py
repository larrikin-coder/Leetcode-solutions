class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []

        intervals.sort(key=lambda x:x[0]) # sorting based on first index of each interval
        merged_lst = [intervals[0]]
        for curr in intervals[1:]:
            last = merged_lst[-1] # last element in List(List(int))
            if last[1] >= curr[0]:
                last[1] = max(last[1],curr[1]) # merging the intervals
            else:
                merged_lst.append(curr)
        return merged_lst       




        