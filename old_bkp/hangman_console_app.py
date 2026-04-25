from graphics import *
import pymysql
import configparser

config = configparser.ConfigParser()
config.read('config.ini')
host = config['MySQL']['host']
username = config['MySQL']['username']
password = config['MySQL']['password']
database = config['MySQL']['database']


def drawHangman(wa, win):
    array = []
    for index in range(7):
        array.append(0)
    drawCount = 7 - wa
    for index in range(drawCount):
        array[index] = 1
    textCenter = Point(250, 50)
    text = Text(textCenter, "HANGMAN")
    text.setFace('times roman')
    text.setSize(30)
    text.setStyle('bold')
    text.setTextColor('red')
    text.draw(win)
    if(array[0]):
        # drawPillar
        base = Line(Point(100, 450), Point(200, 450))
        base.setOutline('black')
        base.setWidth(5)
        base.draw(win)
        leftSupport = Line(Point(150, 400), Point(175, 450))
        leftSupport.setOutline('black')
        leftSupport.setWidth(5)
        leftSupport.draw(win)
        rightSupport = Line(Point(150, 400), Point(125, 450))
        rightSupport.setOutline('black')
        rightSupport.setWidth(5)
        rightSupport.draw(win)
        pillar = Line(Point(150, 450), Point(150, 150))
        pillar.setOutline('black')
        pillar.setWidth(5)
        pillar.draw(win)
        upperBase = Line(Point(300, 150), Point(150, 150))
        upperBase.setOutline('black')
        upperBase.setWidth(5)
        upperBase.draw(win)
        hanger = Line(Point(300, 150), Point(300, 200))
        hanger.setOutline('black')
        hanger.setWidth(5)
        hanger.draw(win)
    if(array[1]):
        # drawFace
        face = Oval(Point(270, 200), Point(330, 250))
        faceCenter = face.getCenter()
        faceImage = Image(faceCenter, "./resources/sadface.png")
        faceImage.draw(win)
    if(array[2]):
        # drawTummy
        tummy = Line(Point(300, 250), Point(300, 350))
        tummy.setWidth(5)
        tummy.draw(win)
    if(array[3]):
        # drawLeftHand
        leftHand = Line(Point(300, 300), Point(250, 250))
        leftHand.setWidth(5)
        leftHand.draw(win)
    if(array[4]):
        # drawRightHand
        rightHand = Line(Point(300, 300), Point(350, 250))
        rightHand.setWidth(5)
        rightHand.draw(win)
    if(array[5]):
        # drawLeftLeg
        leftLeg = Line(Point(300, 350), Point(250, 400))
        leftLeg.setWidth(5)
        leftLeg.draw(win)
    if(array[6]):
        # drawRightLeg
        rightLeg = Line(Point(300, 350), Point(350, 400))
        rightLeg.setWidth(5)
        rightLeg.draw(win)
    return win


def main():
    conn = pymysql.connect(host=host, user=username,
                           passwd=password, db=database)
    cur = conn.cursor()
    win = GraphWin("Hangman", 1000, 500)
    cur.execute("SELECT word FROM easy ORDER BY RAND() LIMIT 1")
    data = cur.fetchone()
    data = data[0]
    data = data.lower()
    wrongAttempts = 7
    lengthCount = 0
    guessed_letters = []
    word_guessed = []
    for letter in data:
        word_guessed.append("-")
    joined_word = None
    while (wrongAttempts != 0 and "-" in word_guessed):
        print()
        print("wrong attempts remaining : " + str(wrongAttempts))
        joined_word = "".join(word_guessed)
        print(joined_word)
        try:
            char = input("Guess a character : ")
        except:
            print("That is not valid input. Please try again.")
            continue
        else:
            if not char.isalpha():
                print("That is not a letter. Please try again.")
                continue
            elif len(char) > 1:
                print("That is more than one letter. Please try again.")
                continue
            elif char in guessed_letters:
                print("You have already guessed that letter. Please try again.")
                continue
            else:
                pass
        guessed_letters.append(char)
        for letter in range(len(data)):
            if char == data[letter]:
                word_guessed[letter] = char
        if char not in data:
            wrongAttempts = wrongAttempts - 1
            win = drawHangman(wrongAttempts, win)
    print(("\nThe word was ")+str(data))


if __name__ == '__main__':
    main()
