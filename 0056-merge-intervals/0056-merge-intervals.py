class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []
        i = 0
        while i<len(intervals)-1:
            if intervals[i][1]>=intervals[i+1][0] and intervals[i][1]<=intervals[i+1][1]:
                temp = [intervals[i][0],intervals[i+1][1]]
                del intervals[i:i+2]
                intervals.insert(i, temp)

            elif intervals[i][1]>=intervals[i+1][0] and intervals[i][1]>=intervals[i+1][1]:
                del intervals[i+1]

            else:
                i+=1
        return intervals
        