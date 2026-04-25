import pymysql

def main():
    fp = open("cities.txt",'r')
    string = fp.read()
    stringArray = string.split()
    #print (stringArray)
    conn = pymysql.connect(host="localhost",user="root",passwd="admin",db="hangman")
    cur = conn.cursor()
    for string in stringArray:
        #print (string)
        if len(string) < 6:
            #print("easy")
            cur.execute("INSERT INTO easy VALUES('"+string+"')")
            conn.commit()
        elif len(string) < 9:
           #print("moderate")
            cur.execute("INSERT INTO moderate VALUES('"+string+"')")
            conn.commit()
        else:
            #print("difficult")
            cur.execute("INSERT INTO difficult VALUES('"+string+"')")
            conn.commit()
    cur.close()
    conn.close()
    fp.close()
if __name__ == '__main__':
    main()
