'''Makenson Noel 

   Programming Practice 
   
   Interview Prep'''

# The purpose of this is to practice python programming for interviews



#Loop 


i = 0 

#Practice class
class practice:

    def __init__():
        
        A = [1,2,3,4,5,6,7,8,9]

        length = len(A)

        i = 0
        temp = 0
        j = length - 1
        
        for i in range (length):
            i+=1
            j=-1
            
            while (i <= length):
                # swap
                temp = A[i]
                A[i] = A[j]
                A[j] = temp

            print(A[i])

            
class_object = practice.__init__()


