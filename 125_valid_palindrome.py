class Solution:
    def isPalindrome(self, s: str) -> bool:
        '''
        new_list = [expression for item in iterable if condition]
        expression: Her öğe için uygulanacak ifade.
        item: İterasyonun döndüğü öğe.
        iterable: İterasyonun uygulandığı dizi veya iterable (örneğin, liste, demet, vb.).
        condition: Opsiyonel bir koşul, isteğe bağlı olarak ifadeyi filtrelemek için kullanılır.
        numbers = [2, -15, 7, 0, -42, 3, -9]
        positive_numbers = [num if num >= 0 else -num for num in numbers]
        print(positive_numbers)  # Output: [2, 15, 7, 0, 42, 3, 9]

        words = ["apple", "banana", "cherry", "date"]
        capitalized_words = [word.capitalize() for word in words]
        print(capitalized_words)  # Output: ['Apple', 'Banana', 'Cherry', 'Date']

        numbers = [2, 15, 7, 0, 42, 3, 9]
        single_digit_numbers = [num for num in numbers if 0 <= num <= 9]
        print(single_digit_numbers)  # Output: [2, 7, 0, 3, 9]

        Bu tür bir kullanım, Python'da "List Comprehension" olarak adlandırılır. 
        List Comprehension, kompakt bir şekilde liste oluşturmanızı sağlayan bir yapıdır. 
        Temelde bir for döngüsü içinde if-else koşullarıyla birlikte kullanılır. L
        ist Comprehension, liste oluşturmak için daha okunabilir ve kompakt bir alternatif sunar.
        '''
        
        s = ''.join(char for char in s if char.isalnum()).lower()
        sreverse = s[::-1]
        return  s == sreverse 

class Solution2:
    def isPalindrome(self, s: str) -> bool:
        s = [c.lower() for c in s if c.isalnum()]
        return all (s[i] == s[~i] for i in range(len(s)//2))


'''
Kodun çalışma mantığı şu adımları takip eder:

for i in range(len(s)//2) döngüsü, dizedeki karakterlerin yarısını dolaşır. 
Bu yarısının kullanılmasının sebebi, bir karakterin simetrik bir yapının bir parçası olabilmesi için diğer karakterle eşleşmesi gerektiğinden, yalnızca yarısının kontrol edilmesidir. 
Yarısının dışına çıkıldığında simetri zaten kontrol edilmiş olur.

s[i] == s[~i] ifadesi, indeks i ile indeks ~i'deki (tamsayıyı tersleme operatörü kullanarak hesaplanan) karakterleri karşılaştırır. 
Tersleme operatörü, indeksi tersine çevirir. Örneğin, ~0 son indeksi, ~1 sondan bir önceki indeksi temsil eder.

Elde edilen sonuç, bir liste içinde toplanır. Her çift indeks için simetri durumu bir boole (True veya False) değeri olarak temsil edilir.

Sonuç olarak, kod, bir dizgenin belirli bir karakter simetrisine sahip olup olmadığını kontrol eder ve bu simetri durumunu bir liste olarak döndürür. 
Örnek olarak, "radar" dizgesi için çıktı [True, False, True] olacaktır; çünkü "r" ve "r" aynıdır (simetri var), "a" ve "a" aynıdır (simetri var), 
ancak "d" ve "a" aynı değildir (simetri yok).
all() fonksiyonu, bir iterable (örneğin liste, demet, dize vb.) içindeki tüm elemanların mantıksal olarak True değer döndürdüğünü kontrol etmek için kullanılır. 
Eğer tüm elemanlar True ise, all() fonksiyonu True değerini döner. Eğer en az bir eleman False ise, fonksiyon False değerini döner.
my_list = [True, True, True, True]
result = all(my_list)
print(result)  # True

my_list = [True, False, True, True]
result = all(my_list)
print(result)  # False

'''
s = "oNu()rruno"
solution = Solution()
result = solution.isPalindrome(s)
print(result)