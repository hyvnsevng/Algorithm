import java.util.Stack;

class Solution {
    public int[] solution(int[] prices) {
        
        int n = prices.length;
        int[] answer = new int[n];
        
        Stack<Integer> stack = new Stack<>();
        for (int i = 0; i < n; i++) {
            int price = prices[i];  // 현재 가격
            
            // 스택 내에서 현재 가격 이하인 시점을 모두 pop하여 answer에 기간을 저장한다. 
            while (!stack.empty() && prices[stack.peek()] > price) {
                Integer comparedPrice = stack.pop();
                answer[comparedPrice] = i - comparedPrice;
            }
            
            // 현재 시점 스택에 push
            stack.push(i);
        }
        
        // 끝까지 떨어지지 않은 가격들 처리하기
        while (!stack.empty()) {
            int i = stack.pop();
            answer[i] = n - i - 1;
        }

        return answer;
    }
}