class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        queue = [char for char in S]
        aux_queue = []
        opened = 0
        print(queue)
        for i in range (0, len(queue)):
            print(queue[-1])
            if(queue[-1] == ')'):
                aux_queue.append(queue.pop())
                print("pop queue")
            elif(queue[-1] == '('):
                if(len(aux_queue) > 0):
                    aux_queue.pop()
                    queue.pop()
                    print("pop aux")
                else:
                    queue.pop()
                    opened += 1
                    print("add 1")
        
        return opened + len(aux_queue)
    
    
