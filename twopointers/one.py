
#1. Finding a first occurrence of pair with given sum (target)
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

#2. print all pairs that can sum up to the target
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

#3. 
