'''Write a program in python which will take input:
    1. Distance (in feet)
 Number of forward steps = 3
 Number of backward steps = 3
 Each step = 1 feet
 
 Calculate number of steps taken to reach destination'''

#enter distance in feet
dis=int(input("Enter distance (in feet): "))
x=3         #forward steps
y=2         #backward steps
steps=0     #initializing steps to 0
i=0         #counter variable
while i<dis:
    if i+x<dis:     #to check if last_position + forward_steps < distance
        i+=x-y
        steps+=x+y
    else:           #if not then it means that man has reached to destination
        steps+=dis-i
        break

#printing total number of steps
print('Total steps taken:',steps)
        
