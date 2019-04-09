# Pocket Colors
# Pocket 0 is green.
# For pockets 1 through 10, the odd = RED and the even = BLACK.
# For pockets 11 through 18, the odd = BLACK and the even = RED.
# For pockets 19 through 28, the odd = RED and the even = BLACK.
# For pockets 29 through 36, the odd = BLACK and the even = RED.


#Equation used 
# if (num % 2 == 0): #even 
# else: #odd


#VARIABLES
#No variable declared in this scope


#Code Begins Here
numP = int (input('Enter a valid pocket number: '))

while numP >= 0 and numP <= 36: #while loop initiation

   if numP == 0:
      print 'The color is GREEN'
   
   if numP > 0 and numP <=10:   
      if (numP % 2 == 0): #even
         print 'The color is BLACK'
      else: #odd
         print 'The color is RED'

   if numP >= 11 and numP <=18:
      if (numP % 2 == 0): #even
         print 'The color is RED'
      else: #odd
         print 'The color is BLACK'
      
   if numP >= 19 and numP <= 28:
      if (numP % 2 == 0): #even
         print 'The color is BLACK'
      else: #odd
         print 'The color is RED'
      
   if numP >= 29 and numP <= 36:
      if (numP % 2== 0): #even
         print 'The color is RED'
      else: #odd
         print 'The color is BLACK'
         
   numP = int (input('If you wish to continue enter another valid pocket number: ')) #while loop continuation statement
   
else: #while loop closing statement
   print 'Invalid pocket number!' 