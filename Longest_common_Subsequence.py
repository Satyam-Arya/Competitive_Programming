def longest_common_subsequence(str1, str2):
    m, n = len(str1), len(str2)

    # Initialize a 2D array to store the lengths of LCS
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Fill the dp array using the recurrence relation
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # The length of the longest common subsequence is stored in dp[m][n]
    return dp[m][n]

str1 = "ABCBDAB"
str2 = "BDCAB"
result = longest_common_subsequence(str1, str2)
print(f"The length of the longest common subsequence is: {result}")
