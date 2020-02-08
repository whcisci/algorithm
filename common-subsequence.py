import numpy as np

class Solution:
    def longestCommonSubsequence(self, text1, text2):
        list_a = list(text1)
        list_b = list(text2)
        list_a.insert(0, 0)
        list_b.insert(0, 0)
        
        num_matrix = np.zeros((len(list_a),len(list_b)))

        for i in range(1, len(list_a)):
            for j in range(1, len(list_b)):
                if list_a[i] == list_b[j]:
                    num_matrix[i][j] = num_matrix[i-1][j-1] + 1
                else:
                    num_matrix[i][j] = max(num_matrix[i-1][j], num_matrix[i][j-1])
        print(num_matrix)
        return int(np.max(num_matrix)) 

word_a = input()
word_b = input()

result = Solution()
print(result.longestCommonSubsequence(word_a, word_b))