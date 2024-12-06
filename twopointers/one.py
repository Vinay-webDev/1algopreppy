
#Finding a first occurrence of pair with given sum (target)
target = 10
array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target2 = 55
array2 = [5, 10, 15, 20, 25, 30, 35, 40, 45]
class Solution:
    def find_pair(self, arr, target):
        left, right = 0, len(arr) - 1

        while (left < right):
            current_sum = arr[left] + arr[right]
            if current_sum == target:
                return [arr[left], arr[right]]
            elif current_sum < target:
                left += 1
            else:
                right -= 1
        return -1
# sol = Solution()
# print(sol.find_pair(array, target)) #[1, 9]
# print(sol.find_pair(array2, target2)) #[10, 45]

#print all pairs that can sum up to the target
target = 10
array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target2 = 55
array2 = [5, 10, 15, 20, 25, 30, 35, 40, 45]
class Solution:
    def find_all_pairs(self, arr, target):
        left, right = 0, len(arr) - 1
        res = []
        while (left < right):
            current_sum = arr[left] + arr[right]
            if current_sum == target:
                res.append([arr[left], arr[right]])
                left += 1
                right -= 1
            elif current_sum < target:
                left += 1
            else:
                right -= 1
        return res
# sol = Solution()
# print(sol.find_all_pairs(array, target)) #[[1, 9], [2, 8], [3, 7], [4, 6]]
# print(sol.find_all_pairs(array2, target2)) #[[10, 45], [15, 40], [20, 35], [25, 30]]

#swap all elements
array = [1, 2, 3, 4, 5]
array2 = ["hello", "bro", "how", "are", "you"]
class Solution:
    def swap_all(self, arr):
        left, right = 0, len(arr) - 1
        while left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
        return arr
# sol = Solution()
# print(sol.swap_all(array))  #[5, 4, 3, 2, 1]
# print(sol.swap_all(array2)) #['you', 'are', 'how', 'bro', 'hello']

#reverse words in a string
s = "hello bro nice to meet you"
s2 = "our house is too far"
s3 = "eat pizza and then go to work"
s4 = "a b c d e f g h i"
class Solution:
    def reverse_words(self, s):
        words = s.split(" ")
        left, right = 0, len(words) - 1
        while left < right:
            words[left], words[right] = words[right], words[left]
            left += 1
            right -= 1
        return " ".join(words)
# sol = Solution()
# print(sol.reverse_words(s)) #you meet to nice bro hello
# print(sol.reverse_words(s2)) #far too is house our
# print(sol.reverse_words(s3)) #work to go then and pizza eat
# print(sol.reverse_words(s4)) #i h g f e d c b a

#remove duplicates from a sorted array
array = [1, 1, 2, 3, 3, 4]
array2 = [100, 100, 300, 400]
class Solution:
    def remove_duplicates(self, arr):
        j = 1 #pointer for next position

        for i in range(1, len(arr)):
            if arr[i] != arr[i - 1]:
                arr[j] = arr[i]
                j += 1
        return arr[:j]
# sol = Solution()
# print(sol.remove_duplicates(array)) #[1, 2, 3, 4]
# print(sol.remove_duplicates(array2)) #[100, 300, 400]

#remove duplicates in-place and return new length
array = [1, 1, 2, 3, 3, 4]
array2 = [100, 100, 300, 400]
class Solution:
    def remove_duplicates(self, arr):
        j = 1
        for i in range(1, len(arr)):
            if arr[i] != arr[i - 1]:
                arr[j] = arr[i]
                j += 1
        return j
# sol = Solution()
# print(sol.remove_duplicates(array)) #4  
# print(sol.remove_duplicates(array2)) #3 










