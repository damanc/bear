from graphics import *
from random import randint
def drawCircle(win,cent,rad,col):
    '''Function draws a circle to a window'''
    C = Circle(cent, rad)
    C.setFill(col)
    C.draw(win)
    return C

def drawEars(win,fCent, fRad, col): #face-center and face-radius
    '''function creates and draws bear ears. Pretty sure this mess could be reduced.'''
    earRad = 0.4*fRad
    #draw left ear
    lEarCentX = fCent.getX()-((2./3)*fRad)
    lEarCentY = fCent.getY()+ fRad
    lEarCent = Point(lEarCentX, lEarCentY)
    lEar = drawCircle(win, lEarCent, earRad, col)
    #draw right ear
    rEarCentX = fCent.getX()+((2./3)*fRad)
    rEarCentY = fCent.getY()+ fRad
    rEarCent = Point(rEarCentX, rEarCentY)
    rEar = drawCircle(win, rEarCent, earRad, col)
    return lEar, rEar

def drawEyes(win,fCent, fRad):
    '''function creates and draws bear eyes. Pretty sure this mess could be reduced.'''
    eyeRad = 0.3*fRad
    pupRad = (2./3) * eyeRad
    #draw left eye
    lEyeCentX = fCent.getX()-(0.4*fRad)
    lEyeCentY = fCent.getY()+ (0.4*fRad)
    lEyeCent = Point(lEyeCentX, lEyeCentY)
    lEye = drawCircle(win, lEyeCent, eyeRad, "white")
    lPup = drawCircle(win, lEyeCent, pupRad, "black")
    #draw right eye
    rEyeCentX = fCent.getX()+(0.4*fRad)
    rEyeCentY = fCent.getY()+ (0.4*fRad)
    rEyeCent = Point(rEyeCentX, rEyeCentY)
    rEye = drawCircle(win, rEyeCent, eyeRad, "white")
    rPup = drawCircle(win, rEyeCent, pupRad, "black")
    return lEye, lPup, rEye, rPup

#TO-DO: Draw mouth and nose

def drawFace(win,cent, fRad, col):
    '''function draws the bear's full face. Order matters!!!'''
    ears = drawEars(win,cent,fRad, col)
    face = drawCircle(win, cent, fRad, col)
    eyes = drawEyes(win,cent,fRad)
    return ears, face, eyes
    
def genColor():
    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255)
    return color_rgb(r,g,b)

def undrawFace(face):
    '''function undraws the elements of the bear's face'''
    #undraw eyes
    face[2][0].undraw(),face[2][1].undraw(),face[2][2].undraw(),face[2][3].undraw()
    #undraw ears
    face[0][0].undraw(),face[0][1].undraw()
    #undraw face
    face[1].undraw()
    
def drawBear():
    '''function draws a bear with center at user's click''' 
    win = GraphWin("Bear", 500,500)
    win.setCoords(0,0,100,100)

    #draw default bear
    cent = Point(50,50)
    fRad = 20 
    col = genColor()
    face = drawFace(win, cent, fRad, col)

    #TO-DO: Change bear's facial expressions when user clicks anywhere in the screen
    #Can't think of how to do this though!!
    #maybe move on to automatic bears all over the place at some point
    flag = True
    while flag:
        c = win.getMouse()
        if c.getX()>5or c.getY()>5: #quit button at bottom left corner
            undrawFace(face)
            col = genColor()
            fRad = randint(10,80)
            face = drawFace(win, c, fRad, col)
            
        else:
            win.close()
            flag = False
    

