import java.util.*;

class Solution
{
    public int solution(int [][]board)
    {
        int answer = 0;
        int n = board.length;
        int m = board[0].length;
        int[][] dp = new int[n + 1][m + 1];
        
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= m; j++) {
                int a = dp[i-1][j-1];
                int b = dp[i-1][j];
                int c = dp[i][j-1];
                
                if (board[i-1][j-1] == 0) dp[i][j] = 0;
                else {
                    dp[i][j] = Math.min(a, Math.min(b, c)) + 1;
                }
                
                answer = Math.max(answer, dp[i][j]);
            }
        }
        
        return answer * answer;
    }
}

/**
0, 0, 0, 0, 0
0, 0, 1, 2, 3
0, 1, 2, 4, ?
0, 2, 4
0, 0

*/