from typing import List
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maximum = 0
        for i in range(len(accounts)):
            toplam = 0
            for j in range(len(accounts[i])):
                toplam += accounts[i][j]
                if (toplam > maximum):
                    maximum = toplam

        return maximum
    
'''

Yukarıdaki koda benzer bir yaklaşım 
def richest_customer_wealth(accounts):
    max_wealth = 0
    
    for customer in accounts:
        wealth = sum(customer)
        max_wealth = max(max_wealth, wealth)
        
    return max_wealth

# Örnek girdiler
accounts1 = [[1, 2, 3], [3, 2, 1]]
accounts2 = [[1, 5], [7, 3], [3, 5]]
accounts3 = [[2, 8, 7], [7, 1, 3], [1, 9, 5]]

print(richest_customer_wealth(accounts1))  # 6
print(richest_customer_wealth(accounts2))  # 10
print(richest_customer_wealth(accounts3))  # 17

 Bu tür basit algoritmalar genellikle "brute force" veya "greedy" algoritmaları olarak adlandırılır, 
 çünkü doğrudan sorunun tanımına uygun bir şekilde işlem yaparlar.
'''


'''
HASH TABLE YAKLASIMI
def richest_customer_wealth(accounts):
    wealth_dict = {}  # Müşteri varlıklarını saklayacak hash tablosu

    for customer in accounts:
        wealth = sum(customer)
        if wealth in wealth_dict:
            wealth_dict[wealth] += 1
        else:
            wealth_dict[wealth] = 1

    max_wealth = max(wealth_dict.keys())
    return max_wealth
'''
accounts = [[1,5],[7,3],[3,5]]

wealthiest = Solution()
result = wealthiest.maximumWealth(accounts)
print(result)

