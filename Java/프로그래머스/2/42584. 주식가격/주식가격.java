import java.util.Stack;

class Solution {
    public int[] solution(int[] prices) {
        int n = prices.length;
        int[] answer = new int[n];
        Stack<Integer[]> stack = new Stack<>();
        for (int i = 0; i < n; i++) {
            int price = prices[i];
            while (stack.size() > 0 && stack.peek()[0] > price) {
                Integer[] elem = stack.pop();
                answer[elem[1]] = i - elem[1];
            }
            
            stack.push(new Integer[]{price, i});
        }
        
        for (Integer[] elem: stack) {
            int price = elem[0];
            int i = elem[1];
            answer[i] = n - i - 1;
        }

        return answer;
    }
}