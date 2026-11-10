#LCSusingdynamicapproach
def lcs_tabulation_seq(s1, s2):
    m, n = len(s1), len(s2)
    dp = [[0]*(n+1) for _ in range(m+1)]
    for i in range(1, m+1):
        for j in range(1, n+1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    print("\nDP Table:")
    print("    ", *s2)
    for i in range(m+1):
        row_label = s1[i-1] if i > 0 else ' '
        print(row_label, *[f"{dp[i][j]:2}" for j in range(n+1)])
    i, j = m, n
    lcs_str = []
    while i > 0 and j > 0:
        if s1[i-1] == s2[j-1]:
            lcs_str.append(s1[i-1])
            i -= 1
            j -= 1
        elif dp[i-1][j] >= dp[i][j-1]:
            i -= 1
        else:
            j -= 1
    return ''.join(reversed(lcs_str))
s1 = input('Enter string1: ')
s2 = input('Enter string2: ')
lcs_result = lcs_tabulation_seq(s1, s2)
print("\nLCS:", lcs_result)
print("Length of common subsequence is:", len(lcs_result))
