import java.util.*;

class Solution {
    
    private static final int[] DR = {1, -1, 0, 0};
    private static final int[] DC = {0, 0, 1, -1};
    private static final char EMPTY = '\0';
    
    public int solution(String[] storage, String[] requests) {
        
        int n = storage.length;
        int m = storage[0].length();
        
        char[][] board = new char[n + 2][m + 2];
        
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                board[i + 1][j + 1] = storage[i].charAt(j);
            }
        }
        
        int answer = n * m;
        
        for (String request: requests) {
            char target = request.charAt(0);
            if (request.length() >= 2) {
                answer -= useCrane(board, target, n, m);
            }
            else {
                answer -= useJige(board, target, n, m);
            }
        }        
        
        return answer;
    }
    
    private boolean[][] findExternal(char[][] storage, int n, int m) {
        int rowSize = n + 2;
        int colSize = m + 2;
        boolean[][] external = new boolean[rowSize][colSize];
        
        Queue<int[]> queue = new ArrayDeque<>();
        external[0][0] = true;
        queue.offer(new int[]{0, 0});
        
        // {0, 0}에서 시작해서 외부와 접한 칸 찾기
        while (!queue.isEmpty()) {
            int[] curr = queue.poll();
            int r = curr[0];
            int c = curr[1];
            
            for (int d = 0; d < 4; d++) {
                int nr = r + DR[d];
                int nc = c + DC[d];
                
                if (nr < 0 || nr >= rowSize || nc < 0 || nc >= colSize) continue;
                if (external[nr][nc]) continue;
                
                // 빈 칸이면 큐에 추가 / 아니면 상태만 변경 
                if (storage[nr][nc] == EMPTY) {
                    queue.offer(new int[]{nr, nc});
                }
                external[nr][nc] = true;
            }
        }
        
        return external;
    }
    
    // 지게차
    private int useJige(char[][] storage, char request, int n, int m) {
        boolean[][] external = findExternal(storage, n, m);
        List<int[]> getOut = new ArrayList<>();
        
        for (int i = 1; i < n + 1; i++) {
            for (int j = 1; j < m + 1; j++) {
                if (storage[i][j] != request || !external[i][j]) continue; 
                getOut.add(new int[]{i, j});
            }
        }
        
        for (int[] coor: getOut) {
            int r = coor[0];
            int c = coor[1];
            storage[r][c] = EMPTY;
        }
        
        return getOut.size();
    }
    
    // 크레인
    private int useCrane(char[][] storage, char request, int n, int m) {
        
        int removeCount = 0;
        
        for (int i = 1; i < n + 1; i++) {
            for (int j = 1; j < m + 1; j++) {
                if (storage[i][j] == request) {
                    storage[i][j] = EMPTY;
                    removeCount++;
                }
            }
        }
        
        return removeCount;
    }
}