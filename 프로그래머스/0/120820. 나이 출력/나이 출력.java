class Solution {
    public int solution(int age) {
        int answer = 0;
        int year = 2022;
        if(0 < age && age <= 120) {
            answer = year + 1 - age;
        }
        return answer;
    }
}