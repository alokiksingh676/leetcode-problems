class Solution:
    def numberofsteps(self,num:int)->int:
        steps=0
        while num>0:
            if num%2==0:
                num//=2
            else:
                num-=1

            steps+=1
        return steps
    
num=int(input("enter a number: "))
result=Solution().numberofsteps(num)
print(f"number of steps to reduce {num} to zero is: {result}")