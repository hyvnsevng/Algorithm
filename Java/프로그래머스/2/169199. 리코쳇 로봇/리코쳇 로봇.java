import java.util.*;

class Solution {
    
    private static final int[] DR = {1, -1, 0, 0};
    private static final int[] DC = {0, 0, 1, -1};
    
    public int solution(String[] board) {
        int answer = 0;
        int n = board.length;
        int m = board[0].length();
        
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (board[i].charAt(j) == 'R') {
                    answer = bfs(board, n, m, i, j);
                    break;
                }
            }
        }
        
        
        return answer;
    }
    
    private int bfs(String[] board, int n, int m, int sr, int sc) {
        int res = 10000000;     // MAX
        boolean flag = false;   // 목표에 도달했는지
        
        Queue<Integer[]> queue = new ArrayDeque<>();
        queue.add(new Integer[] {sr, sc, 0});
        boolean[][] visited = new boolean[n][m];    // 방문 배열
        visited[sr][sc] = true;
        while (!queue.isEmpty()) {
            Integer[] curr = queue.poll();
            int r = curr[0];
            int c = curr[1];
            int cnt = curr[2];
            
            // 목표 지점이라면 최소 이동횟수 갱신
            if (board[r].charAt(c) == 'G' && cnt < res) {
                res = cnt;
                flag = true;
            }
            
            // 네 방향으로 끝까지 이동시킨다
            for (int i = 0; i < 4; i++) {
                int[] afterMove = move(board, n, m, r, c, i);
                int nr = afterMove[0];
                int nc = afterMove[1];
                
                // 방문하지 않았을 경우에만 큐에 추가
                if (!visited[nr][nc]) {
                    queue.add(new Integer[] {nr, nc, cnt + 1});
                    visited[nr][nc] = true;
                }
            }
        }
        if (flag) return res;
        return -1;
    }
    
    private int[] move(String[] board, int n, int m, int sr, int sc, int dir) {
        
        int dr = DR[dir], dc = DC[dir];
        int nr = sr + dr, nc = sc + dc;
        while (nr >= 0 && nr < n && nc >= 0 && nc < m && board[nr].charAt(nc) != 'D') {
            nr += dr;
            nc += dc;
        }
        
        return new int[]{nr - dr, nc - dc};
    }
}
