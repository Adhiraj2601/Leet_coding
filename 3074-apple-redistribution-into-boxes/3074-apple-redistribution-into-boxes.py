class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        capacity.sort(reverse=True)
        s = sum(apple)
        c = 0
        cap = 0
        for i in capacity:
            cap = cap+int(i)
            if s>cap:
                c+=1
            else:
                c+=1
                break
            print(s,cap,c)
        return c
        