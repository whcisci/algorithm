class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        list_a = list(text1)
        list_b = list(text2)
        list_a.insert(0, 0)
        list_b.insert(0, 0)
        
        num_matrix = [[0]*len(list_b) for _ in range(len(list_a))]

        for i in range(1, len(list_a)):
            for j in range(1, len(list_b)):
                if list_a[i] == list_b[j]:
                    num_matrix[i][j] = num_matrix[i-1][j-1] + 1
                else:
                    num_matrix[i][j] = max(num_matrix[i-1][j], num_matrix[i][j-1])
        #print(num_matrix)

        return num_matrix[-1][-1]