from graphics import *

def main():
    win = GraphWin("Hangman", 500, 500)
    base = Line(Point(100,450), Point(200,450))
    base.draw(win)

    pillar = Line(Point(150,450),Point(150,150))
    pillar.draw(win)

    upperBase = Line(Point(300,150),Point(150,150))
    upperBase.draw(win)

    hanger = Line(Point(300,150),Point(300,200))
    hanger.draw(win)    

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

    tummy = Line(Point(300,250),Point(300,350))
    tummy.draw(win)

    leftHand = Line(Point(300,300),Point(250,250))
    leftHand.draw(win)

    rightHand = Line(Point(300,300),Point(350,250))
    rightHand.draw(win)

    leftLeg = Line(Point(300,350),Point(250,400))
    leftLeg.draw(win)

    rightLeg = Line(Point(300,350),Point(350,400))
    rightLeg.draw(win)
    
    win.getMouse() # Pause to view result
    win.close()    # Close window when done

main()
