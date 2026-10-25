class Solution(object):
    def asteroidCollision(self, asteroids):
        
        stack = []
        
        for i in range(len(asteroids)):

            alive = True

            while stack and stack[-1] > 0 and asteroids[i] < 0:

                if stack[-1] < abs(asteroids[i]):
                    stack.pop()

                elif stack[-1] == abs(asteroids[i]):
                    stack.pop()
                    alive = False
                    break
                    
                else:
                    alive = False
                    break

            if alive:
                stack.append(asteroids[i])

        return stack