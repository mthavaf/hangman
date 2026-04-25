import pymysql
import configparser

config = configparser.ConfigParser()
config.read('config.ini')
host = config['MySQL']['host']
username = config['MySQL']['username']
password = config['MySQL']['password']
database = config['MySQL']['database']


def main():
    fp = open("./resources/cities.txt", 'r')
    string = fp.read()
    stringArray = string.split()
    #print (stringArray)
    conn = pymysql.connect(host=host, user=username,
                           passwd=password, db=database)
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS easy (word VARCHAR(100))")
    cur.execute("CREATE TABLE IF NOT EXISTS moderate (word VARCHAR(100))")
    cur.execute("CREATE TABLE IF NOT EXISTS difficult (word VARCHAR(100))")
    for string in stringArray:
        #print (string)
        if len(string) < 6:
            # print("easy")
            cur.execute("INSERT INTO easy VALUES('"+string+"')")
            conn.commit()
        elif len(string) < 9:
           # print("moderate")
            cur.execute("INSERT INTO moderate VALUES('"+string+"')")
            conn.commit()
        else:
            # print("difficult")
            cur.execute("INSERT INTO difficult VALUES('"+string+"')")
            conn.commit()
    cur.close()
    conn.close()
    fp.close()


if __name__ == '__main__':
    main()
