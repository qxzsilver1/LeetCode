class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        txn_dict = defaultdict(list)
        txn_set = set(transactions)
        transcations = list(txn_set)
        
        res_dict = defaultdict(int)
        res = []

        for txn in transactions:
            name, time, amount, city = txn.split(',')
            time = int(time)
            amount = int(amount)

            if name not in txn_dict:
                txn_dict[name] = [(time, amount, city)]
            else:
                txn_dict[name].append((time, amount, city))
        
        txn_dict_sorted = {k: sorted(v, key= lambda x: (x[0], -x[1])) for k, v in txn_dict.items()}
        
        for name in txn_dict_sorted:
            name_txns = txn_dict_sorted[name]

            prev_amount, prev_time, prev_city = -1, -1, ''
            prev_cnt = 0
            min_amount, min_time_in_hr_interval, min_city = -1, float('inf'), ''
            
            for i in range(len(name_txns)):
                if i == 0 or name_txns[i][0] - min_time_in_hr_interval > 60:
                    min_time_in_hr_interval = name_txns[i][0]
                    min_amount = name_txns[i][1]
                    min_city = name_txns[i][2]
                    min_cnt = 1
                elif i != 0 and name_txns[i][0] == min_time_in_hr_interval and name_txns[i][1] == min_amount and name_txns[i][2] == min_city:
                    min_cnt += 1
                
                if name_txns[i][1] > 1000:
                    res_dict[name + ',' + str(name_txns[i][0]) + ',' + str(name_txns[i][1]) + ',' + name_txns[i][2]] += 1
                elif i != 0 and name_txns[i][0] - prev_time <= 60 and prev_city != name_txns[i][2]:
                    res_dict[name + ',' + str(name_txns[i][0]) + ',' + str(name_txns[i][1]) + ',' + name_txns[i][2]] += 1

                    prev_str = name + ',' + str(prev_time) + ',' + str(prev_amount) + ',' + prev_city
                    
                    if prev_str not in res_dict:
                        res_dict[prev_str] += prev_cnt
                
                if i != 0 and name_txns[i][0] - min_time_in_hr_interval <= 60 and min_city != name_txns[i][2]:
                    min_str = name + ',' + str(min_time_in_hr_interval) + ',' + str(min_amount) + ',' + min_city

                    if min_str not in res_dict:
                        res_dict[min_str] += min_cnt
                    
                    curr_str = name + ',' + str(name_txns[i][0]) + ',' + str(name_txns[i][1]) + ',' + name_txns[i][2]

                    if curr_str not in res_dict:
                        res_dict[curr_str] += 1
                
                if name_txns[i][0] == prev_time and name_txns[i][1] == prev_amount and name_txns[i][2] == prev_city:
                    prev_cnt += 1
                else:
                    prev_cnt = 1
                prev_amount = name_txns[i][1]
                prev_time = name_txns[i][0]
                prev_city = name_txns[i][2]
        
        for k, v in res_dict.items():
            res.extend([k] * v)
        
        return res
