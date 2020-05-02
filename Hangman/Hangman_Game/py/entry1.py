from tkinter import *
import pymysql
def getWord(num):
    global guessedWord,wrongAttempts,gameOver,level,data,array
    level = num
    array = []
    gameOver = 0
    guessedWord = []
    wrongAttempts = 8
    conn = pymysql.connect(host="localhost",user="root",passwd="cout<<password;",db="hangman")
    cur = conn.cursor()
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
    for letter in data: 
       guessedWord.append("-")
    for index in range(7):
        array.append(0)
    main('-',array,data,level)
    
def callback(event):
    try:
        ch = chr(ord(event.char))
        if gameOver == 0 and ch.isalpha():
            main(chr(ord(event.char)),array,data,level)
    except:
        sound = Sound()
        sound.read('')
        sound.play()
        pass
def main(char,array,data,level):
    global wrongAttempts,gameOver
    w.delete(ALL)
    
    while (wrongAttempts != 0 and "-" in guessedWord):
        for index in range(len(data)):
             if char == data[index]:
                guessedWord[index] = char
                
        if char not in data:
            wrongAttempts = wrongAttempts - 1

        guesssedWord = ''.join(guessedWord)

        drawCount = 7 - wrongAttempts
        for index in range(drawCount):
            array[index] = 1
        w.create_text(250,50,font=("times roman", 30),text="HANGMAN",fill="#B0171F")
        w.create_text(750,150,font = ("times roman",10),text = "wrong attempts remaining : ")
        text = Label(master,text=wrongAttempts)
        text.place(x=845,y=142)
        w.create_text(750,170,font = ("times roman",10),text = "guess a character : ")
        if(array[0]):
            w.create_line(150,450,150,150, fill="#000000", width=4)
            w.create_line(300,150,150,150, fill="#000000", width=4)
            w.create_line(100,450,200,450, fill="#000000", width=4)
            w.create_line(300,150,300,200, fill="#000000", width=4)
            w.create_line(150,400,175,450, fill="#000000", width=4)
            w.create_line(150,400,125,450, fill="#000000", width=4)
        if(array[1]):
            img = PhotoImage(file="sadface.png")
            w.create_image(268,192, anchor=NW, image=img)
        if(array[2]):
            w.create_line(300,250,300,350, fill="#000000", width=4)
        if(array[3]):
            w.create_line(300,300,250,250, fill="#000000", width=4)
        if(array[4]):
            w.create_line(300,300,350,250, fill="#000000", width=4)
        if(array[5]):
            w.create_line(300,350,250,400, fill="#000000", width=4)
        if(array[6]):
            w.create_line(300,350,350,400, fill="#000000", width=4)
        
        w.create_text(750,230,font = ("times roman",20),text=guessedWord,fill="#B0171F")
        if(wrongAttempts == 0 ):
            w.create_text(750,380,font = ("times roman",10),text = "THE WORD WAS :    "+str(data))
            w.create_text(750,400,font = ("times roman",10),text = "YOU LAST")
            gameOver = 1
        if "-" not in guessedWord :
            w.create_text(750,380,font = ("times roman",10),text = "THE WORD WAS :    "+str(data))
            w.create_text(750,400,font = ("times roman",10),text = "CONGRATULATION!!!! YOU WON!!!!")
            gameOver = 1
        Button(master, text='newgame', command = lambda:getWord(level)).place(x=680,y=300)
        Button(master, text='exit',command = lambda:exit(0)).place(x=800,y=300)
        mainloop()   
if __name__ == "__main__":
    #array = []
    master = Tk()
    w = Canvas(master, width=1000, height=500)
    w.pack()
    w.create_text(250,50,font=("times roman", 30),text="HANGMAN",fill="#B0171F")
    Button(master, text='simple',command = lambda:getWord(1)).place(x=700,y=50)
    Button(master, text='moderate',command = lambda:getWord(2)).place(x=800,y=50)
    Button(master, text='difficult',command = lambda:getWord(3)).place(x=920,y=50)
    w.focus_set()
    w.bind("<Key>",callback)
    
