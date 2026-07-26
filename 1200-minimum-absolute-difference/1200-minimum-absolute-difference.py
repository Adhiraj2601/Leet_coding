class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        diffs = {}
        arr.sort()
        for i in range(1,len(arr)):
            dif = arr[i]-arr[i-1]
            pair = [arr[i - 1], arr[i]]
            if dif not in diffs:
                diffs[dif] = [pair]
            else:
                diffs[dif].append(pair)
        return diffs[min(diffs)]


        