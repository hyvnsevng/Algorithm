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
                int diag = dp[i-1][j-1];
                int up = dp[i-1][j];
                int left = dp[i][j-1];
                
                if (board[i-1][j-1] == 1) {               
                    dp[i][j] = Math.min(diag, Math.min(up, left)) + 1;
                }
                
                answer = Math.max(answer, dp[i][j]);
            }
        }
        
        return answer * answer;
    }
}