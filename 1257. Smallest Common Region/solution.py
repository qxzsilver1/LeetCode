class Solution:
    def findSmallestRegion(self, regions: list[list[str]], region1: str, region2: str) -> str:
        parent = { child: row[0] for row in regions for child in row[1:] }
        ancestors = set()

        while True:
            ancestors.add(region1)

            if region1 not in parent:
                break
            
            region1 = parent[region1]
        
        while region2 not in ancestors:
            region2 = parent[region2]
        
        return region2
