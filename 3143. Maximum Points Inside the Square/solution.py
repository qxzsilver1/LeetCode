class Solution:
    def maxPointsInsideSquare(self, points: List[List[int]], s: str) -> int:
        tag_points = list(zip(s, [max(abs(x[0]), abs(x[1])) for x in points]))
        tag_points.sort(key= lambda x: x[1])
        
        # tag_points.sort(key= lambda x: x[1][0] ** 2 + x[1][1] ** 2)

        dist_to_tag = defaultdict(list)

        for t, point_dist in tag_points:
            dist_to_tag[point_dist].append(t)
        
        bucket_counts = [0] * 26

        res = 0

        for dist, lst in dist_to_tag.items():
            if len(set(lst)) != len(lst):
                return res
            
            for tag in lst:
                bucket_counts[ord(tag) - ord('a')] += 1

                if bucket_counts[ord(tag) - ord('a')] == 2:
                    return res
            
            res += len(lst)

        # for t, point in tag_points:
        #     bucket_counts[ord(t) - ord('a')] += 1

        #     if bucket_counts[ord(t) - ord('a')] == 2:
        #         return res
            
        #     res += 1
        
        return res
