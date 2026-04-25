from graphics import *
import pymysql
import sys
import random
import string

drawWindow = 0
def drawHangman(wa):
        if drawWindow == 0:
                win = GraphWin("Hangman", 500, 500)
                drawWindow = 1
        array = []
        for index in range(7):
                array.append(0)
        drawCount = 7 - wa
        for index in range(drawCount):
                array[index]=1
        if(array[0]):
                #drawPillar
                base = Line(Point(100,450), Point(200,450))
                base.draw(win)

                pillar = Line(Point(150,450),Point(150,150))
                pillar.draw(win)

                upperBase = Line(Point(300,150),Point(150,150))
                upperBase.draw(win)

                hanger = Line(Point(300,150),Point(300,200))
                hanger.draw(win)
        if(array[1]):
                #drawTillFace
                face = Oval(Point(270,200),Point(330,250))
                face.draw(win)

                leftEye = Oval(Point(285,220),Point(289,227))
                leftEye.draw(win)

                rightEye = Oval(Point(315,220),Point(319,227))
                rightEye.draw(win)

                nose = Oval(Point(298,225),Point(305,232))
                nose.draw(win)

                mouth = Line(Point(290,240),Point(310,240))
                mouth.draw(win)

        if(array[2]):
                #drawTillTummy
                tummy = Line(Point(300,250),Point(300,350))
                tummy.draw(win)
                
        if(array[3]):
                #drawTillLeftHand
                leftHand = Line(Point(300,300),Point(250,250))
                leftHand.draw(win)
                
        if(array[4]):
                #drawTillRightHand
                rightHand = Line(Point(300,300),Point(350,250))
                rightHand.draw(win)

        if(array[5]):
                #drawTillLeftLeg
                leftLeg = Line(Point(300,350),Point(250,400))
                leftLeg.draw(win)

        if(array[6]):
                #drawTillRightLeg
                rightLeg = Line(Point(300,350),Point(350,400))
                rightLeg.draw(win)
        
        

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
        wrongAttempts = 7
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
                    drawHangman(wrongAttempts)
    
    
        print(("\nThe word was ")+str(data)) 
    
        if "-" not in word_guessed :        
            print("Congratulation!!!! YOU WON!!!!") 
            sys.exit(0) 
        print("YOU LOST") 
            
#if __name__ == '__main__': 
main()

                




