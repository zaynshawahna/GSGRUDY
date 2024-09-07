import random
import logging


def Fibonacci(n):
    if n==0:
        return [0]
    if n==1:
        return [0,1]
    arr=[0,1]
    for i in range(2,n):
        number=arr[-1]+arr[-2]
        arr.append(number)
    return arr   
 
def FibonacciNextOnly(n):
    if n==0:
        return 0
    if n==1:
        return 0,1
    a,b=0,1
    for i in range(2,n):
        number=a+b
        a=b
        b=number
    return b        

def startFibonacciGame():
 try:

    numberOfSeq = int(input("enter the number of Fibonacci sequence you want:"))
    if numberOfSeq < 0:
        logging.error("enter a non negatinve value")
        raise ValueError(" enter a non negatinve value")
    str1=input("if you need to see Fibonacci sequence press y, any other character you will see only the next number of you sequence:")
    if str1=='y':
       
         if numberOfSeq == 0 :
                print(f"old Fibonacci sequence []")
                print(f"next number in sequence 0")    
                print(f"new Fibonacci sequence [0]")
                logging.info("user passed the game by entering 0")
         elif numberOfSeq == 1 :
                print(f"old Fibonacci sequence [0]")
                print(f"next number in sequence 1")    
                print(f"new Fibonacci sequence [0, 1]")   
                logging.info("user passed the game by entering 1")   
         else:    
                numberOfSeq=numberOfSeq+1
                newSeq=Fibonacci(numberOfSeq)
                print(f"old Fibonacci sequence {newSeq[0:len(newSeq)-1]}")
                print(f"next number in sequence {newSeq[-2] +newSeq[-3]}")
                print(f"new Fibonacci sequence {newSeq}")
                logging.info("user passed the game by entering a number grater than 1")

    else:
         if numberOfSeq == 0 :
                print(f"next number in sequence 0")    
                logging.info("user passed the game by entering 0")
         elif numberOfSeq == 1 :
                print(f"next number in sequence 1")    
                logging.info("user passed the game by entering 1")   
         else:    
                numberOfSeq=numberOfSeq+1
                nextNumber=FibonacciNextOnly(numberOfSeq)
                print(f"next number in sequence {nextNumber}")
                logging.info("user passed the game by entering a number grater than 1")


    

 except ValueError as e:
    logging.error(f"not integer{e}")




def MissingNumberGame():
   array1 = random.sample(range(1, 11), 9)
   logging.info("the random array created done succesfuly")
   print("random array from 1-10 and one number is missing (generated array) is :", array1)
   array2=[2, 1, 5, 4, 6, 9, 7, 8, 10]
   print(f"missing number is :{list(set(array2)-set(array1))}")
   logging.info("user find missing number")


if __name__=="__main__":

   
    print("-------------------")
    print("task1")
    print("next Fibonacci number game")
    startFibonacciGame()
    print("end task1")
    print("-------------------")

    while True:
      nextGame=input("press any key to start missing number game")
      if nextGame is not None:
         break
   
    print("-------------------")
    print("task2")
    print("missing number game")
    MissingNumberGame()
    print("end task2")
    print("-------------------")

   



