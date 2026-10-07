class Solution:
    def countSeniors(self, details: List[str]) -> int:
        senior_pattern = "\d{10}[MFO](\d{2})\d{2}"
        res = 0

        for d in details:
            match = re.search(senior_pattern, d)

            if match:
                age = match.group(1)
                if int(age) > 60:
                    res += 1
        
        return res
