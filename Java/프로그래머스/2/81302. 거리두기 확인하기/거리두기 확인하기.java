class Solution {
        
    static int[] dx = {1, -1, 0, 0};
    static int[] dy = {0, 0, 1, -1};
    static int size = 5;
    
    public int[] solution(String[][] places) {
        
        int n = places.length;
        int[] answer = new int[n];
        
        for (int i = 0; i < n; i++) {
            String[] place = places[i];
            answer[i] = checkDistanceKeeped(place);
        }
        
        return answer;
    }
    
    private int checkDistanceKeeped(String[] place) {
        
        for (int r = 0; r < size; r++) {
            for (int c = 0; c < size; c++) {
                if (place[r].charAt(c) == 'P') {
                    boolean[][] visited = new boolean[size][size];
                    int res = dfs(place, visited, r, c, r, c, 0);
                    if (res == 0) return 0;
                }
            }
        }
        
        return 1;
    }
    
    private int dfs(String[] place, boolean[][] visited, int startX, int startY, int currX, int currY, int depth) {
        // 맨해튼 거리가 3 이상
        if (depth >= 3) return 1;
        
        visited[currX][currY] = true;
        
        // 거리두기 지키지 않은 경우
        if (depth > 0 && place[currX].charAt(currY) == 'P') {
            return 0;
        }        
        
        // 다음 노드 탐색 
        for (int i = 0; i < 4; i++) {
            int nx = currX + dx[i];
            int ny = currY + dy[i];
            // 대기실 범위 내의 방문하지 않은 노드 중 파티션이 아닌 노드
            if (nx >= 0 && nx < 5 && ny >= 0 && ny < 5 && !visited[nx][ny] && place[nx].charAt(ny) != 'X') {
                int res = dfs(place, visited, startX, startY, nx, ny, depth + 1);
                if (res == 0) return 0;
            }
        }
        
        return 1;
    }
}
