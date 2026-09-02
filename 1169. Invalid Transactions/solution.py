class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        invalid = []

        transaction_time = defaultdict(dict)

        for txn in transactions:
            name, str_time, amount, city = txn.split(',')
            time = int(str_time)

            if name not in transaction_time[time]:
                transaction_time[time][name] = {city, }
            else:
                transaction_time[time][name].add(city)
        
        for txn in transactions:
            name, str_time, amount, city = txn.split(',')
            time = int(str_time)

            if int(amount) > 1000:
                invalid.append(txn)
                continue
            
            for inval_time in range(time - 60, time + 61):
                if inval_time not in transaction_time:
                    continue
                
                if name not in transaction_time[inval_time]:
                    continue
                
                txn_by_name_time = transaction_time[inval_time][name]

                if city not in txn_by_name_time or len(txn_by_name_time) > 1:
                    invalid.append(txn)
                    break
            
        return invalid
