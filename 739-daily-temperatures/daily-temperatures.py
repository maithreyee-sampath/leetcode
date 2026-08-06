class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] #we will store a pair of temp adn it's index
        answer = [0]*len(temperatures)
        

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                st, si = stack.pop() #pop the temperature and index
                answer[si] = (i-si)
            stack.append([t, i])
        return answer
