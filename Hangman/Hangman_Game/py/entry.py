from tkinter import *
import pymysql
def getWord(arg):
    global level
    global data
    level = arg
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
    global guessedWord
    for letter in data: 
       guessedWord.append("-")
    main('-',8,array,guessedWord,level)
def callback(event):
    print(repr(event.char))
    main(chr(ord(event.char)), wrongAttempts,array,guessedWord,level)

def main(char, wrongAttempts,array,guessedWord,level):
    print (wrongattempts)
    while (wrongAttempts != 0 and "-" in guessedWord):
        w.delete(ALL)
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
        w.create_text(750,150,text = "wrong attempts remaining : ")
        text = Label(master,text=wrongAttempts)
        text.place(x=835,y=142)
        w.create_text(750,170,text = "guess a character : ")
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
        print(guessedWord)
        w.create_text(750,200,text=guessedWord)
        """textBox = Entry(master)
        textBox.place(x=750,y=250)"""
        #Button(master, text='enter', command = lambda: main(textBox.get(), wrongAttempts,array,data,guessedWord,level)).place(x=750,y=300)
        if(wrongAttempts == 0 ):
            w.create_text(750,350,text = "the word was : "+str(data))
            w.create_text(750,370,text = "you lost")
        if "-" not in guessedWord :
            w.create_text(750,350,text = "the word was : "+str(data))
            w.create_text(750,370,text = "Congratulation!!!! YOU WON!!!!")
        Button(master, text='newgame', command = lambda:getWord(level)).place(x=830,y=300)
        Button(master, text='exit',command = lambda:exit(0)).place(x=900,y=400)
        mainloop()

    
if __name__ == "__main__":
    level = 0
    array = []
    data = ""
    guessedWord = []
    for index in range(7):
        array.append(0)
    wrongAttempts = 8
    master = Tk()
    w = Canvas(master, width=1000, height=500)
    w.pack()
    w.create_text(250,50,font=("times roman", 30),text="HANGMAN",fill="#B0171F")
    Button(master, text='simple',command = lambda:getWord(1)).place(x=700,y=50)
    Button(master, text='moderate',command = lambda:getWord(2)).place(x=800,y=50)
    Button(master, text='difficult',command = lambda:getWord(3)).place(x=920,y=50)
    w.focus_set()
    w.bind("<Key>",callback)
    
