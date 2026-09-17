class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        
        stack = []
        for ans in asteroids:
            if ans > 0:
                stack.append(ans)
            else:
                while stack and stack[-1] > 0 :
                    
                    


                    if stack[-1] < -ans:
                        stack.pop()
                        continue

                    

                    if stack[-1] == -ans:
                        stack.pop()
                        break

                    if stack[-1] > -ans:
                        break
            
                else:
                    stack.append(ans)
                   
            


        return stack