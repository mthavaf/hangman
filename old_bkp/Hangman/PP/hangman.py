from graphics import *
import pymysql
import sys
import random
import string

def main():
        conn = pymysql.connect(host="localhost",user="root",passwd="cout<<password;",db="test")
        cur = conn.cursor()
        print ('you have 1:simple,2:medium and 3:complex\n')
        level = int(input('select the level you want to play\n'))
        if level == 1:
                cur.execute("SELECT word FROM easy ORDER BY RAND() LIMIT 1")
                data = cur.fetchone()
                data = data[0]       
        elif level == 2:
                cur.execute("SELECT word FROM moderate ORDER BY RAND() LIMIT 1")
                data = cur.fetchone()
                data = data[0]
        elif level == 3:
                cur.execute("SELECT word FROM difficult ORDER BY RAND() LIMIT 1")
                data = cur.fetchone()
                data = data[0]
        else:
                print ('that level doesnt exist!!')
        data = data.lower()
        wrongAttempts = 6
        lengthCount = 0
        guessed_letters=[]
        word_guessed = [] 
        for letter in data: 
            word_guessed.append("-") 
            joined_word= None 

        while (wrongAttempts != 0 and "-" in word_guessed):

                print ()
                print ("wrong attempts remaining : " + str(wrongAttempts))
                joined_word = "".join(word_guessed) 
                print(joined_word) 
                try:
                        char = input("Guess a character : ")
                except:
                        print ("That is not valid input. Please try again.")
                        continue
                else:
                        if not char.isalpha():
                                print  ("That is not a letter. Please try again.")
                                continue
                        elif len(char) > 1:
                                print("That is more than one letter. Please try again.")
                                continue
                        elif char in guessed_letters:
                                print  ("You have already guessed that letter. Please try again.")
                                continue
                        else:
                                pass
                guessed_letters.append(char)

                for letter in range(len(data)): 
                    if char == data[letter]: 
                        word_guessed[letter] = char 
                    
                if char not in data : 
                    wrongAttempts = wrongAttempts - 1
                    draw
    
    
        print(("\nThe word was ")+str(data)) 
    
        if "-" not in word_guessed :        
            print("Congratulation!!!! YOU WON!!!!") 
            sys.exit(0) 
        print("YOU LOST") 
            
if __name__ == '__main__': 
    main()

                




