from graphics import *
from random import randint
from time import sleep

def drawCircle(win,cent,rad,col):
    '''takes window, point object, numerical value, string'''
    '''Function draws a circle to a window'''
    C = Circle(cent, rad)
    C.setFill(col)
    C.draw(win)
    return C

def ear(win, fCent, fRad, col, lEar):
    '''takes window, point object, numerical value, string and boolean'''
    '''function creates an ear'''
    earRad = 0.4*fRad
    
    if lEar:
        #draw left ear
        earCentX = fCent.getX()-((2./3)*fRad)
        earCentY = fCent.getY()+ fRad
        earCent = Point(earCentX, earCentY)
        ear = drawCircle(win, earCent, earRad, col)
    else:
        #draw right ear
        earCentX = fCent.getX()+((2./3)*fRad)
        earCentY = fCent.getY()+ fRad
        earCent = Point(earCentX, earCentY)
        ear = drawCircle(win, earCent, earRad, col)
    return ear

def eye(win,fCent, fRad, col, mode, lEye):
    '''takes window, point object, numerical value, string and boolean'''
    '''function creates an eye'''
    eyeRad = 0.3*fRad
    pupRad = (2./3) * eyeRad
    if lEye:
        #draw left eye
        eyeCentX = fCent.getX()-(0.4*fRad)
        eyeCentY = fCent.getY()+ (0.4*fRad)
        eyeCent = Point(eyeCentX, eyeCentY)
        eye = drawCircle(win, eyeCent, eyeRad, "white")
        pupil = drawCircle(win, eyeCent, pupRad, "black")
        #draw left eyelid
        p1x = eyeCentX - eyeRad
        if mode==1: #wink
            eye.setFill(col)
            pupil.setFill(col)
            pupil.setOutline(col)
            p1y = eyeCentY - eyeRad
            px1 = eyeCentX-eyeRad
            px2 = eyeCentX+eyeRad
            py = eyeCentY
            lid = Line(Point(px1,py),Point(px2, py))
            lid.draw(win)

##        elif mode==2: #narrow eyes???
##            p1y = eyeCentY + 0.5*eyeRad
##            p1 = Point(p1x, p1y)
##            p2x = eyeCentX + eyeRad
##            p2y = eyeCentY + eyeRad
##            p2 = Point(p2x, p2y)
##            lid = Rectangle(p1, p2)
##            lid.setFill(col)
##            lid.setOutline(col)
##            lid.draw(win)
        else:
            p1y = eyeCentY + 0.5*eyeRad #eyelid
            p1 = Point(p1x, p1y)
            p2x = eyeCentX + eyeRad
            p2y = eyeCentY + eyeRad
            p2 = Point(p2x, p2y)
            lid = Rectangle(p1, p2)
            lid.setFill(col)
            lid.setOutline(col)
            lid.draw(win)
            
    else:
        #draw right eye
        eyeCentX = fCent.getX()+(0.4*fRad)
        eyeCentY = fCent.getY()+ (0.4*fRad)
        eyeCent = Point(eyeCentX, eyeCentY)
        eye = drawCircle(win, eyeCent, eyeRad, "white")
        pupil = drawCircle(win, eyeCent, pupRad, "black")
        #draw right eyelid
        p11x = eyeCentX - eyeRad
        p11y = eyeCentY + 0.5*eyeRad
        p11 = Point(p11x, p11y)
        p22x = eyeCentX + eyeRad
        p22y = eyeCentY + eyeRad
        p22 = Point(p22x, p22y)
        lid = Rectangle(p11, p22)
        lid.setFill(col)
        lid.setOutline(col)
        lid.draw(win)
      
    return eye, pupil, lid
    
def drawEars(win,fCent, fRad, col):
    '''takes window, point object, numerical value, string'''
    '''function creates and draws bear ears'''
    lEar = ear(win, fCent, fRad, col, True)
    rEar = ear(win, fCent, fRad, col, False)
    return lEar, rEar

def drawEyes(win,fCent, fRad, col, wink):
    '''takes window, point object, numerical value, string, boolean'''
    '''function creates and draws bear eyes'''

    lEye = eye(win,fCent, fRad, col, wink, True)
    rEye = eye(win,fCent, fRad, col, wink, False)
    
    return lEye, rEye

def drawNose(win,fCent, fRad):
    noseP1 = fCent
    nP2x = fCent.getX() - 0.2*fRad
    nP2_3Y = fCent.getY() - 0.25*fRad
    nP3x = fCent.getX() + 0.2*fRad
    noseP2 = Point(nP2x, nP2_3Y)
    noseP3 = Point(nP3x, nP2_3Y)
    nose = Polygon(noseP1, noseP2, noseP3)
    nose.setFill("pink")
    nose.draw(win)
    return nose

#TO-DO:include parameter 'wink' which takes out tongue if True
def mouth(win, fCent, fRad, col, mode):
    '''takes window, point object, numerical value, string and boolean'''
    '''mouth = 1 --> tongue out when wink,''' 
    '''function creates a mouth with tongue'''
    c1_c2x = fCent.getX()
    c1y = fCent.getY() - 0.4*fRad
    c2y = fCent.getY() - 0.2*fRad
    tx = fCent.getX()
    ty = fCent.getY() - 0.5*fRad
    c1 = Point(c1_c2x,c1y)
    c2 = Point(c1_c2x,c2y)
    tC = Point(tx, ty)
    rad = 0.3*fRad
    tRad = 0.5*rad
    t = drawCircle(win, tC, tRad, "red") #tongue
    if mode==1: #tongue out
        m1 = drawCircle(win, c1,rad,"white")
        t = drawCircle(win, tC, 0.5*rad, "red") #tongue
        m1.setOutline(col)
        m2 = drawCircle(win, c2,rad, col)
        m2.setOutline(col)
    elif mode ==2: #twisted mouth for narrowed eyes
        t.undraw()
        l1x = fCent.getX() - rad
        l1y = fCent.getY() - 0.4*fRad
        l2x = fCent.getX() + rad
        l2y = fCent.getY() - 0.4*fRad
        l2y2 = fCent.getY() - 0.45*fRad
        m1 = Line(Point(l1x,l1y), Point(l2x,l2y))
        m1.draw(win)
        m2 = Line(Point(l1x,l1y), Point(l2x,l2y2))
        m2.draw(win)
    else: #just a wide smile
        t.undraw()
        m1 = drawCircle(win, c1,rad,"white")
        m1.setOutline(col)
        m2 = drawCircle(win, c2,rad, col)
        m2.setOutline(col)
        
    return m1, t, m2

def drawMouth(win, fCent, fRad, col, mode):
    '''takes window, point object, numerical value, string'''
    m = mouth(win, fCent, fRad, col, mode)
    return m
    
def drawFace(win,cent, fRad, col, mode):
    '''takes window, point object, numerical value, string, boolean'''
    '''function draws the bear's full face'''
    ears = drawEars(win,cent,fRad, col)
    face = drawCircle(win, cent, fRad, col)
    eyes = drawEyes(win,cent,fRad, col, mode)
    mouth = drawMouth(win, cent, fRad, col, mode)
    nose = drawNose(win, cent, fRad)
    return ears, face, eyes, mouth, nose
    
def genColor():
    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255)
    return color_rgb(r,g,b)

def undrawFace(face):
    '''function undraws the elements of the bear's face'''
    #undraw eyes
    face[2][0].undraw(),face[2][1].undraw()
    #undraw ears
    face[0][0].undraw(),face[0][1].undraw()
    #undraw mouth
    face[3][0].undraw()
    #undraw nose
    face[4].undraw()
    #undraw face
    face[1].undraw()

def drawBear():
    '''function draws a bear with center at user's click''' 
    win = GraphWin("Bear", 800,800)
    win.setCoords(0,0,100,100)

    #draw default bear
    cent = Point(50,50)
    fRad = 20
    col = genColor()
    mode = 0
    face = drawFace(win, cent, fRad, col, mode)
    facesOnDisplay = []

    #TO-DO: Change bear's facial expressions: already have a wink
    #move on to automatic bears all over the place
    flag = True
    try:
        while flag:
            facesOnDisplay.append(face)
            c = Point(randint(0,100),randint(0,100))#c = win.getMouse()
            sleep(1.5)
            if c.getX()>5 or c.getY()>5:
                col = genColor()
                fRad = randint(10,50)
                face = drawFace(win, c, fRad, col, mode%3)
            
            else:
                win.close()
                print "great!!"
                flag = False
            mode = mode + 1

    except:
        win.close()
        print "Done!!!"


