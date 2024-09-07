import random
import logging

def MissingNumberGame():
   array1 = random.sample(range(1, 11), 9)
   logging.info("the random array created done succesfuly")
   print("random array from 1-10 and one number is missing (generated array) is :", array1)
   array2=[2, 1, 5, 4, 6, 9, 7, 8, 10]
   print(f"missing number is :{list(set(array2)-set(array1))}")
   logging.info("user find missing number")


if __name__=="__main__":

   

   
    print("-------------------")
    print("task2")
    print("missing number game")
    MissingNumberGame()
    print("end task2")
    print("-------------------")