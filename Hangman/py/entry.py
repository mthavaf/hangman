from tkinter import *
import pymysql
def main(char, wrongAttempts,array,data,guessedWord,level):
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
         
        
        w.create_text(750,200,text=guessedWord)
        textBox = Entry(master)
        textBox.place(x=750,y=250)
        Button(master, text='enter', command = lambda: main(textBox.get(), wrongAttempts,array,data,guessedWord,level)).place(x=750,y=300)
        if(wrongAttempts == 0 ):
            w.create_text(750,350,text = "the word was : "+str(data))
            w.create_text(750,370,text = "you lost")
        if "-" not in guessedWord :
            w.create_text(750,350,text = "the word was : "+str(data))
            w.create_text(750,370,text = "Congratulation!!!! YOU WON!!!!")
        Button(master, text='newgame', command = lambda:init(master,w,level)).place(x=830,y=300)
        mainloop()
def init(master,w,level):
    conn = pymysql.connect(host="localhost",user="root",passwd="ashwini123",db="hangman")
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

    guessedWord = []
    for letter in data: 
        guessedWord.append("-")
    array = []
    for index in range(7):
        array.append(0)
    main('-',8,array,data,guessedWord,level )
if __name__ == "__main__":
    master = Tk()
    w = Canvas(master, width=1000, height=500)
    w.pack()
    w.create_text(250,50,font=("times roman", 30),text="HANGMAN",fill="#B0171F")
    Button(master, text='simple',command = lambda:init(master,w,1)).place(x=700,y=50)
    Button(master, text='moderate',command = lambda:init(master,w,2)).place(x=800,y=50)
    Button(master, text='difficult',command = lambda:init(master,w,3)).place(x=920,y=50)
    
         
    
