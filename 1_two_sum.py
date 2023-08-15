from typing import List

'''
solution 2
'''
class Solution2:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []
        
        for i in range(0 , len(nums)-1):   
            for j in range(i+1,len(nums)):
                if((nums[i] + nums[j]) == target):
                    result.append(i)
                    result.append(j)

        return result
    
'''
solution 1
'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_to_index = {}  # Sayıları ve indexlerini saklamak için bir sözlük oluşturuyoruz.
        
        '''
        enumerate(nums) fonksiyonu, bir dizi veya liste üzerinde döngü yaparken hem elemanın değerini hem de indisini almanızı sağlar.
        Bu, genellikle bir döngü içinde elemanın indeksine erişmek veya her bir elemanın konumunu takip etmek istediğinizde kullanışlıdır.
        nums = [2, 7, 11, 15]

        for i, num in enumerate(nums):
            print(f"Index: {i}, Value: {num}")

        Index: 0, Value: 2
        Index: 1, Value: 7
        Index: 2, Value: 11
        Index: 3, Value: 15

        '''
        for i, num in enumerate(nums):
            complement = target - num  #complement = tamamlayıcı yani diyor ki listede gezerken hedef 3 ve sayı 1 ise tamamlayıcı = 2 olacak.
            
            if complement in num_to_index:
                return [num_to_index[complement], i]
            
            num_to_index[num] = i
        
        return []  # Eğer çözüm bulunamazsa boş bir liste döndürüyoruz.

'''

HASH TABLE NEDİR?
# Bir hash tablosu oluşturma (sözlük)
hash_table = {}

# Anahtar-değer çiftlerini ekleme
hash_table["apple"] = 50
hash_table["banana"] = 30
hash_table["cherry"] = 40

# Anahtar-değer çiftlerini erişme
print(hash_table["apple"])   # Output: 50
print(hash_table["banana"])  # Output: 30
print(hash_table["cherry"])  # Output: 40

# Anahtarın varlığını kontrol etme
if "apple" in hash_table:
    print("Apple exists in the hash table.")
else:
    print("Apple does not exist in the hash table.")

# Değerleri güncelleme
hash_table["apple"] = 60
print(hash_table["apple"])  # Output: 60

# Anahtarları ve değerleri gezme
for key, value in hash_table.items():
    print(f"Key: {key}, Value: {value}")

'''



nums = [1, 2, 4, 5]
target = 6
solution = Solution()
result = solution.twoSum(nums, target)
print(result)