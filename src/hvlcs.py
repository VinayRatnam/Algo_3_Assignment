def hvlcs_algo(values, s1, s2):
    
    rows = len(s1) + 1
    cols = len(s2) + 1
    
    dp = [[0] * cols for _ in range(rows)]

    for row in range(1, rows):
        for col in range(1, cols):
            if s1[row-1] == s2[col-1]:
                dp[row][col] = dp[row-1][col-1] + values[s1[row-1]]
            else:
                dp[row][col] = max(dp[row-1][col], dp[row][col-1])

    bt = []
    row = rows - 1
    col = cols - 1
    
    while row > 0 and col > 0:
        
        if s1[row-1] == s2[col-1]:
            bt.append(s1[row-1])
            row -= 1
            col -= 1
        
        elif dp[row-1][col] > dp[row][col-1]:
            row -= 1
        else:
            col -= 1
            
    
    bt.reverse()
    
    return (dp[-1][-1], bt.join())