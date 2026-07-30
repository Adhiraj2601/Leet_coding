class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:

        events = []
        for x, y, l in squares:
            events.append((y, 1, x, x + l))
            events.append((y + l, -1, x, x + l))

        events.sort()
        active = []
        prev_y = events[0][0]
        total_area = 0

        segments = []  

        def covered_x():
            if not active:
                return 0
            active.sort()
            total = 0
            s, e = active[0]
            for ns, ne in active[1:]:
                if ns > e:
                    total += e - s
                    s, e = ns, ne
                else:
                    e = max(e, ne)
            total += e - s
            return total

        for y, typ, x1, x2 in events:
            dy = y - prev_y
            if dy > 0:
                width = covered_x()
                if width > 0:
                    segments.append((prev_y, y, width, total_area))
                    total_area += width * dy

            if typ == 1:
                active.append((x1, x2))
            else:
                active.remove((x1, x2))

            prev_y = y

        half = total_area / 2

        for y1, y2, width, area_before in segments:
            area_here = width * (y2 - y1)
            if area_before + area_here >= half:
                return y1 + (half - area_before) / width

        return 0.0

