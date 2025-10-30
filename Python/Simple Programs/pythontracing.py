#1. Result is 3 and runs twice
# def transform(a,b):
#     if a > b:
#         return a - transform(a-1,b)
#     elif a < b:
#         return b + transform(a, b-1)
#     else:
#         return a
# 
# print(transform(2,2))

#2. Result is 3, state of a: 6,3,2,1,0
# def mystery(a, b):
#     if a == 0:
#         return b
#     if b == 0:
#         return a
#     if a % 2 == 0:
#         return mystery(a // 2, b) + 2
#     else:
#         return mystery(a - 1, b - 1) - 1
#     
# result = mystery(6, 3)
# print(result)

#Lists -- 4 Problems

#1.
# nums = [5, 10, 15, 20, 25]
# for i in range(len(nums)):
#     if i % 2 == 0:
#         nums[i] += i
#     else:
#         nums[i] *= i
# 
# nums.reverse()
# print(nums)

#2.
# nums = [3, 7, 2, 8, 1, 6]
# for i in range(len(nums)):
#     if nums[i] % 2 == 0:
#         nums[i] *= 2
#     else:
#         nums[i] -= 1
# 
# print(nums)

#3. prints out APPLE, DATE, FIG; filtered is a list
# words = ["apple", "banana", "cherry", "date", "fig"]
# filtered = [word.upper() for word in words if len(word) < 6]
# print(filtered)


#4.
# def process_file(filename):
#     file = open(filename, 'r')
#     lines = file.readlines()
#     result = []
#     for line in lines:
#         words = line.split()
#         for word in words:
#             if len(word) > 3:
#                 result.append(word)
#     file.close()
#     return result
# output = process_file('example.txt')
# print(output)

1.
# matrix = [[1, 2, 4], [12, 5, 6], [7, 8, 9]]
# for row in matrix:
#     for _ in row:
#         if _ % 3 == 0:
#             print(_)

#2.
# grid = [[2, 3, 4], 
#         [5, 6, 7], 
#         [8, 9, 10]]
# 
# for i in range(len(grid)):
#     for j in range(len(grid[i])):
#         if (i + j) % 2 == 0:
#             grid[i][j] *= 2
#         else:
#             grid[i][j] -= 1
# 
# for row in grid:
#     print(row)

# def search_grid(grid, i, j):
#     if i >= len(grid) or j >= len(grid[0]):
#         return 0
#     if grid[i][j] == 1:
#         return 1 + search_grid(grid, i + 1, j) + search_grid(grid, i, j + 1)
#     return search_grid(grid, i + 1, j) + search_grid(grid, i, j + 1)
# 
# matrix = [[1, 0, 1],
#           [0, 1, 0],
#           [1, 1, 0]]
# count = search_grid(matrix, 0, 0)
# print(count)


def words_words(filename):
    file = open(filename, 'r')
    word_count = {}
    for line in file:
        words = line.split()
        for word in words:
            word = word.lower().strip(",.!?")
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1
    file.close()
    return word_count

track = words_words('lyrics.txt')
print(track)







