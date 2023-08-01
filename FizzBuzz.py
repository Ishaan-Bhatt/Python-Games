def fizzBuzz (num):
    if num<0:
        print ("Invalid Inputs")
       
  
    for num in range(1,num+1):
        if num<0:
            print ("Invalid Inputs")
       
        elif num % 3 == 0 and num % 5 == 0:
            print ("Fizz Buzz")
        elif num % 3==0:
            print ("Fizz")
        elif num % 5 == 0:
            print ("Buzz")
      
        else:
            print (num)
print(fizzBuzz(5))
        
        
       
    
print (fizzBuzz(-35))

        
    
