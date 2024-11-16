# https://leetcode.com/problems/search-insert-position/description/

# list = [1,3,5,6]
# def searchInsert(nums, target: int) -> int:
#       res = 0
#       for i, v in enumerate(nums):
#             if v >= target: return i
#             res +=1
#       return res

# print(searchInsert(list, 7))

# class Solution:
#     def searchInsert(self,nums, target: int) -> int:
#         res = 0
#         for i, v in enumerate(nums):
#                 if v >= target: return i
#                 res +=1
#         return res


# https://leetcode.com/problems/roman-to-integer/

#  int value = 0;
#       if (c == 'I')
#             value = 1;
#       else if (c == 'V')
#             value = 5;
#       else if (c == 'X')
#             value = 10;
#       else if (c == 'L')
#             value = 50;
#       else if (c == 'C')
#             value = 100;
#       else if (c == 'D')
#             value = 500;
#       else if (c == 'M')
#             value = 1000;


# def romanToInt(s: str) -> int:
#       c_val=0
#       result = 0
#       old_val = 1001

#       for v in s:
#             match v:
#                   case "I": c_val = 1
#                   case "V": c_val = 5
#                   case "X": c_val = 10
#                   case "L": c_val = 50
#                   case "C": c_val = 100
#                   case "D": c_val = 500
#                   case "M": c_val = 1000

#             result += c_val
#             if old_val < c_val : result -= 2 * old_val

#             old_val = c_val

#       return result


# print(romanToInt("MMMDXLIV"))

# https://leetcode.com/problems/longest-common-prefix/description/


# lt = [1,2,3,3,4,1,2,3,4,1,2,3,4]

# print([i for i in lt if i == 1 or i == 2 or i == 3 or i == 4])
# import math

# st ={-2,4-3,-4,5,-6,8,6,-5,7,-8, True}

# for i in st:
#       if i == 1:
#             print(bool(i), type(bool(i)) )
#             continue

#       print(str(i), type(str(i)))


# lt = [7,1,2,5,3,9,4,7,8]

# dc1 = {}
# dc2 = {}

# for k, i in enumerate(lt):
#       if i > 5 and i < 10:
#             dc1[k] = i
#       else:
#             dc2[k] = i

# print(dc1)
# print(dc2)

# def is_juft(num):
#       r = num
#       while True:
#             r = r / 2
#             qol = r - int(r)
#             if qol == 0:
#                   return True
#             else:
#                   return False

# def is_juft2(num):
#       r = num
#       while True:
#             if num < 0: r * -1
#             r-=2
#             if r < 2:
#                   break

#       if r == 0:
#             return True
#       else:
#             return False

# print(is_juft2(-8))


# lt = [7,1,2,5,3,9,4,7,8]

# sum = 0

# for i in lt:
#       if is_juft(i):
#             sum+=i
# print(sum)


# num = 123456789
# strp = ''

# for i in str(num):
#       if not is_juft(int(i)):
#             strp += i

# print(list(strp))


# lt = ["Khan", "Kuliev", "Khamatov", "Khanova",
#       "Khanovich", "Khamatova", "Khamatovich", "Khanov"]


# manba = {
#     "male": "Khan Khanovich Kuliev Khamatov Khamatovich Khamatova Khamatovich Khanov",
#     "female": "Khanova Khamatova Khanov"
# }

# for i in lt:
#     if i in manba["male"]:
#         print("male: ", i)
#     elif i in manba["female"]:
#         print("female: ", i)
#         break


# n = int(input("number kiriting: "))

# lst = []

# for I in range(1, n+1):
#     lt1 = []

#     for II in range(n-1, n+1):
#         lt2 = []

#         for III in range(1, n+1):
#             lt3 = []

#             for IV in range(1, n+1):
#                 lt3.append(IV)

#             lt2.append(lt3)

#         lt1.append(lt2)

#     lst.append(lt1)

#     lt1 = []

# print(lst)


# def create_list(n):
#     lst = []
#     if n == 0:
#         for i in range(n):
#             lst.append(i)
#     for i in range(n):
#         lst.append(create_list(n-1))

#     return lst

# print(create_list(n))

# i = 11

# while i > 10:
#     print("katta")