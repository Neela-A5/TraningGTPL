# Ascending order
i = 1              # Initialization
while i < 5:       # Condition
    print("GTPL", i)
    i = i+1         # Increment/Decrement

# Descending order
i = 5            
while i > 1:      
    print("GTPL")
    i = i-1  

# while within while Loop(Inner Loop Run only for One Time)
i = 1 
j = 1      
while i <= 5:      
    print("GTPL", end = " ") # 5 Times 
    while j <=3:
        print(" Coders") # 3 Times
        j = j + 1

    i = i+1  


#while within while Loop(Inner Loop Run evertime whwnever Outer loop runs)

i = 1 
    
while i <= 5:      
    print("GTPL", end = " ") # 5 Times 
    j = 1  
    while j <=3:
        print(" Coders", end= " ") # 3 Times     GTPL  Coders  Coders  Coders 

 
        j = j + 1
    print()

    i = i+1  