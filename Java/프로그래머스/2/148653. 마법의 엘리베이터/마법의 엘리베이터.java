class Solution {
    public int solution(int storey) {
        if (storey < 10) {
            return min(storey, 10 - storey + 1);
        }
        
        int div = storey / 10, remainder = storey % 10;
        return min(solution(div) + remainder, solution(div + 1) + 10 - remainder);
    }
    
    private int min(int A, int B) {
        if (A > B) return B;
        return A;
    }
}