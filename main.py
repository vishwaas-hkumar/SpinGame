import pygame as py
import random
import math
py.init()
py.display.set_caption("Spin")
clock=py.time.Clock()
speed=5 #5
Gamespeed=60 #60
#Dimensions and positions
width,height=500,800 #500,800
X,Y=[],[0,-200,-400,-600,-800] #[0,-200,-400,-600,-800]
Hw,Hh=250,40#Horizontal block #250,40
Mw,Mh=100,40#Central block #100,40
Sw,Sh=120,90#Side block #120,90
BGblockwidth = 100 #100
BGblockheight = 100 #100
BGblockX1 = [0, 150, 300, 450]#[0, 150, 300, 450]
BGblockX2 = [0, 150, 300, 450]#[0, 150, 300, 450]
BGblockY1 = [50, 350, 650]#[50, 350, 650]
BGblockY2 = [200,500] #[200,500]
ObsWidth,ObsHeight,x=0,0,0

#RGB colour codes
BG_Grey=(95,95,95) #(95,95,95)
Green=(0,255,0) #(0,255,0)
Black=(0,0,0) #(0,0,0)
C_Grey=(75,75,75)
White=(255,255,255) #(255,255,255)
Blue=(0,0,255) #(0,0,255)
Red=(255,0,0)#(255,0,0)
c1, c2, c3 = Red, Green, Red
Gdec=2
BGactivator=True
BGc1,BGc2=Green,Red
alphaVal=0
SCORECHECK=False
Display=py.display.set_mode((width,height))
def GameEXIT():
    py.quit()
    quit()

def Obstacles(X,Y,ObsWidth,ObsHeight):
    colour=White
    for i in range(5):
        py.draw.rect(Display,colour,[X[i],Y[i],ObsWidth[i],ObsHeight[i]])

def textObj(dispText, Tfont,colour):
    textSurface=Tfont.render(dispText,True,colour)
    return textSurface,textSurface.get_rect()

def msg_disp(dispText,dispX,dispY,dispSize,colour,useFont):
    Tfont=py.font.SysFont(useFont,dispSize)
    TextSurf,TextBox,=textObj(dispText,Tfont,colour)
    TextBox.center= (dispX,dispY)
    Display.blit(TextSurf,TextBox)

def Collided():
    global X,Y,TypeRand,ObsHeight,ObsWidth,Gamespeed,Gdec,BGblockX2,BGblockX1,BGblockY1,BGblockY2
    BGblockX1 = [0, 150, 300, 450]  # [0, 150, 300, 450]
    BGblockX2 = [0, 150, 300, 450]  # [0, 150, 300, 450]
    BGblockY1 = [50, 350, 650]  # [50, 350, 650]
    BGblockY2 = [200, 500]  # [200,500]
    X,Y =[], [0, -200, -400, -600, -800]
    if Gdec==1:
        Gamespeed=40
    elif Gdec==2:
        Gamespeed=60
    elif Gdec==3:
        Gamespeed=80
    TypeRand, ObsWidth, ObsHeight = [], [], []
    LoopBreaker=False
    while not LoopBreaker:
        for event in py.event.get():
            if event.type == py.QUIT:
                GameEXIT()
        mouse,click=py.mouse.get_pos(),py.mouse.get_pressed()
        Display.fill((55, 55, 55))
        msg_disp("Your Score: " + str(SCORE), width / 2, height / 2, 40, Green, "Calibri")
        msg_disp("You Collided", width / 2, 150, 80, Red, "TimesNewRoman")

        if (mouse[0]-width//4)**2 + (mouse[1]-3*height//4)**2 <= 60**2:
            py.draw.circle(Display, (0,170,0), (width // 4, 3 * height // 4), 70)
            msg_disp("Retry", width // 4, 3 * height // 4, 50, (190,190,190), "Calibri")
            if click[0]==1:
                LoopBreaker =True
                MainToGame()
                GameLoop()
        else:
            py.draw.circle(Display,Green,(width//4,3*height//4),60)
            msg_disp("Retry",width//4,3*height//4,40,White,"Calibri")

        if (mouse[0]-3*width//4)**2 + (mouse[1]-3*height//4)**2<= 60**2:
            py.draw.circle(Display,(170,0,0),(3*width//4, 3*height//4), 70)
            msg_disp("Menu", 3*width // 4, 3 * height // 4, 50, (190, 190, 190), "Calibri")
            if click[0]==1:
                LoopBreaker = True
                DeathScreenToMain()
                MainMenu()
        else:
            py.draw.circle(Display, Red, (3 * width // 4, 3 * height // 4), 60)
            msg_disp("Menu", 3 * width // 4, 3 * height // 4, 40, White, "Calibri")
        py.display.update()

def BG():
    global alphaVal,x,SCORECHECK
    if alphaVal>=255:
        x=-1
    elif alphaVal<=0:
        x=1
    if SCORE//1500==SCORE/1500:
        SCORECHECK=True
    if SCORE//3000==SCORE/3000:
        SCORECHECK=False

    if SCORECHECK:
        if BGblockX1[3]>width:
            del(BGblockX1[3])
            BGblockX1.insert(0,-100)
        for i in BGblockX1:
            for j in BGblockY1:
                BGblockSurf = py.Surface((BGblockwidth, BGblockheight))
                BGblockSurf.set_alpha(alphaVal)
                BGblockSurf.fill((0,0,0))
                Display.blit(BGblockSurf, (i, j))

        if BGblockX2[0]<-100:
            del(BGblockX2[0])
            BGblockX2.insert(3,width)
        for i in BGblockX2:
            for j in BGblockY2:
                BGblockSurf = py.Surface((BGblockwidth, BGblockheight))
                BGblockSurf.set_alpha(255-alphaVal)
                BGblockSurf.fill((0, 0, 0))
                Display.blit(BGblockSurf, (i, j))
        for i in range(len(BGblockX1)):
            BGblockX1[i]+=1
            BGblockX2[i] -= 1
    else:
        if BGblockX1[0] < -100:
            del (BGblockX1[0])
            BGblockX1.insert(3, width)
        for i in BGblockX1:
            for j in BGblockY1:
                BGblockSurf = py.Surface((BGblockwidth, BGblockheight))
                BGblockSurf.set_alpha(alphaVal)
                BGblockSurf.fill((0, 0, 0))
                Display.blit(BGblockSurf, (i, j))

        if BGblockX2[3] >width:
            del (BGblockX2[3])
            BGblockX2.insert(0, -100)
        for i in BGblockX2:
            for j in BGblockY2:
                BGblockSurf = py.Surface((BGblockwidth, BGblockheight))
                BGblockSurf.set_alpha(255 - alphaVal)
                BGblockSurf.fill((0, 0, 0))
                Display.blit(BGblockSurf, (i, j))
        for i in range(len(BGblockX1)):
            BGblockX1[i] -= 1
            BGblockX2[i] += 1
    alphaVal+=x
def BallSprite(xBlue,yBlue,xRed,yRed):
    py.draw.circle(Display,Blue,(int(xBlue),int(yBlue)),12)
    py.draw.circle(Display, Red, (int(xRed), int(yRed)), 12)

def Circumference(XposCircum,YposCircum,colourCircum):
    py.draw.circle(Display, colourCircum, (XposCircum, YposCircum), 110,2)#110,2

def MainToSettings(x_change,ScreenX):
    LoopBreaker=False
    global event
    while not LoopBreaker:
        for event in py.event.get():
            if event.type == py.QUIT:
                GameEXIT()
        Display.fill((10, 20, 20))
        py.draw.rect(Display,(50,50,50),[ScreenX,0,450,800])
        if (ScreenX>=0 and x_change!=-10) or (x_change!=10 and ScreenX<=-450):
            x_change=0
            LoopBreaker=True
        ScreenX += x_change
        py.display.update()
        clock.tick(60)
def SettingsOptBG():
    global BGactivator,BGc1,BGc2
    msg_disp("Background:",150,600,30,White,"TimesNewRoman")
    mouse, click = py.mouse.get_pos(), py.mouse.get_pressed()
    if BGactivator==True:
        BGc1=Green
        BGc2=Red
    elif BGactivator==False:
        BGc1=Red
        BGc2=Green
    if 80<mouse[0]<230 and 650<mouse[1]<690:
        if BGactivator==True:
            BGc1=(0,190,0)
        else:
            BGc1=(190,0,0)
        py.draw.rect(Display, BGc1, [80, 650, 150, 40])
        msg_disp("ON", 155, 670, 30, (170,170,170), "TimesNewRoman")
        if click[0]==1:
            BGactivator=True
    else:
        py.draw.rect(Display,BGc1,[80,650,150,40])
        msg_disp("ON",155,670,30,White,"TimesNewRoman")
    if 80 < mouse[0] < 230 and 720 < mouse[1] < 760:
        if BGactivator==False:
            BGc2=(0,190,0)
        else:
            BGc2=(190,0,0)
        py.draw.rect(Display, BGc2, [80, 720, 150, 40])
        msg_disp("OFF", 155, 740, 30, (170,170,170), "TimesNewRoman")
        if click[0]==1:
            BGactivator=False
    else:
        py.draw.rect(Display, BGc2, [80, 720, 150, 40])
        msg_disp("OFF", 155, 740, 30, White, "TimesNewRoman")

def SettingsOptSpeed():
    global Gamespeed,Gdec
    msg_disp("Game Speed:",150,250,30,White,"TimesNewRoman")
    mouse, click = py.mouse.get_pos(), py.mouse.get_pressed()
    if Gamespeed==60:
        c1,c2,c3=Red, Green, Red
    elif Gamespeed==40:
        c1, c2, c3 = Green, Red, Red
    elif Gamespeed ==80:
        c1,c2,c3=Red,Red,Green
    if 80<mouse[0]<230 and 300<mouse[1]<340:
        if Gamespeed==40:
            c1=(0,190,0)
        else:
            c1=(190,0,0)
        py.draw.rect(Display, c1, [80, 300, 150, 40])
        msg_disp("Low",155,320,30,(170,170,170),"TimesNewRoman")
        if click[0]==1:
            Gamespeed=40
            Gdec=1
    else:
        if Gamespeed==40:
            c1=(0,255,0)
        else:
            c1=(255,0,0)
        py.draw.rect(Display, c1, [80, 300, 150, 40])
        msg_disp("Low",155,320,30,White,"TimesNewRoman")
    if 80<mouse[0]<230 and 400<mouse[1]<440:
        if Gamespeed == 60:
            c2 = (0, 190, 0)
        else:
            c2 = (190, 0, 0)
        py.draw.rect(Display, c2, [80, 400, 150, 40])
        msg_disp("Medium", 155, 420, 30, (170, 170, 170), "TimesNewRoman")
        if click[0] == 1:
            Gamespeed = 60
            Gdec=2
    else:
        if Gamespeed == 60:
            c2 = (0, 255, 0)
        else:
            c2 = (255, 0, 0)
        py.draw.rect(Display, c2, [80, 400, 150, 40])
        msg_disp("Medium", 155, 420, 30, White, "TimesNewRoman")
    if 80<mouse[0]<230 and 500<mouse[1]<540:
        if Gamespeed == 80:
            c3 = (0, 190, 0)
        else:
            c3 = (190, 0, 0)
        py.draw.rect(Display, c3, [80, 500, 150, 40])
        msg_disp("High", 155, 520, 30, (170, 170, 170), "TimesNewRoman")
        if click[0] == 1:
            Gamespeed = 80
            Gdec=3
    else:
        if Gamespeed == 80:
            c3 = (0, 255, 0)
        else:
            c3 = (255, 0, 0)
        py.draw.rect(Display, c3, [80, 500, 150, 40])
        msg_disp("High", 155, 520, 30, White, "TimesNewRoman")
    py.display.update()

def Settings():
    LoopBreaker = False
    global event
    while not LoopBreaker:
        for event in py.event.get():
            if event.type == py.QUIT:
                GameEXIT()
        mouse, click = py.mouse.get_pos(), py.mouse.get_pressed()
        py.draw.circle(Display, (150, 150, 150), (40, 40), 30)
        if (mouse[0] - 40) ** 2 + (mouse[1] - 40) ** 2 <= 30 ** 2:
            for HyphenIncr in range(0, 25, 12):
                msg_disp("-",28 + HyphenIncr, 38, 60, (200, 200, 200), "Calibri")
            msg_disp("<",+ 30, 40, 60, (200, 200, 200), "Calibri")
            if click[0] == 1:
                MainToSettings(-10,0)
                MainMenu()
        else:
            py.draw.circle(Display, (100, 100, 100), (40, 40), 30)
            for HyphenIncr in range(0, 30, 12):
                msg_disp("-", 28 + HyphenIncr, 38, 60, White, "Calibri")
            msg_disp("<", 30, 40, 60, White, "Calibri")
        msg_disp("Controls:",80,100,25,White,"TimesNewRoman")
        msg_disp("Left Arrow: anti-clockwise revolution", 170, 125, 20,White, "TimesNewRoman")
        msg_disp("Right Arrow: clockwise revolution", 160, 145, 20,White, "TimesNewRoman")
        SettingsOptSpeed()
        SettingsOptBG()
        py.display.update()
        clock.tick(60)

def SettingsIcon(colour):
    py.draw.circle(Display, colour, (100, 650), 55,4)
    py.draw.circle(Display,colour,(100,650),25)
    py.draw.line(Display,colour,(60,650),(140,650),10)
    py.draw.line(Display, colour, (100, 610), (100, 690), 10)
    py.draw.polygon(Display,colour,((67,623),(73,617),(133,677),(127,683)))
    py.draw.polygon(Display, colour, ((127, 617), (133, 623), (73, 683), (67, 677)))
    py.draw.circle(Display, (10,20,20), (100, 650), 13)

def MainToGame():
    y_change=8
    lowerY=800
    UpperY=-450
    LoopBreaker= False
    global event
    while not LoopBreaker:
        for event in py.event.get():
            if event.type == py.QUIT:
                GameEXIT()
        py.draw.rect(Display,BG_Grey,[0,UpperY,500,450])
        py.draw.rect(Display, BG_Grey, [0, lowerY, 500, 450])
        UpperY+=y_change
        lowerY-=y_change
        if UpperY>=0:
            LoopBreaker=True
        clock.tick(60)
        py.display.update()

def DeathScreenToMain():
    LoopBreaker=False
    x_change=6
    LeftX=-520
    RightX=500
    while not LoopBreaker:
        for event in py.event.get():
            if event.type == py.QUIT:
                GameEXIT()
        py.draw.rect(Display,(10,20,20),[LeftX,0,520,800])
        py.draw.rect(Display,(10,20,20),[RightX,0,520,800])
        LeftX+=x_change
        RightX-=x_change
        if LeftX >= 0:
            LoopBreaker=True
        py.display.update()
        clock.tick(60)

def MainMenu():
    Intro=True
    Ang,SwapColMain=0,0
    global event
    while Intro:
        for event in py.event.get():
            if event.type == py.QUIT:
                GameEXIT()
        if SwapColMain==200:
            SwapColMain=0

        mouse = py.mouse.get_pos()
        click=py.mouse.get_pressed()

        Ang+=0.3#0.3
        xBlueMain = (width // 2 + 110 * math.cos(math.radians(Ang)))  # 110 = Revolution radius
        yBlueMain = (height // 2 + 110 * math.sin(math.radians(Ang)))
        xRedMain = (width // 2 - 110 * math.cos(math.radians(Ang)))
        yRedMain = (height // 2 - 110 * math.sin(math.radians(Ang)))

        Display.fill((10, 20, 20))  # (10,20,20)

        msg_disp("SP", 170, 165, 150, Red, "Colonna")
        msg_disp("IN", 330, 165, 150, Blue, "Colonna")
        if (mouse[0]-(width//2))**2 + (mouse[1]-(height//2))**2<= 110**2:
            Circumference(width // 2, height // 2, (170,170,170))
            py.draw.polygon(Display, (170,170,170),[(300, 400), (230, 330), (230, 470)])# right(300,400),top(230,330),bottom(230,470)
            if click[0]==1:
                Intro=False
                MainToGame()
                GameLoop()
        else:
            Circumference(width // 2, height // 2, White)
            py.draw.polygon(Display, White,[(300, 400), (230, 330), (230, 470)])  # right(300,400),top(230,330),bottom(230,470)

        if (mouse[0] - 100)**2 + (mouse[1]-650)**2 <= 55**2:
            SettingsIcon((170,170,170))
            if click[0]==1:
                Intro=False
                MainToSettings(10,-450)
                Settings()
        else:
            SettingsIcon(White)
        if SwapColMain<100:
            BallSprite(xBlueMain, yBlueMain, xRedMain, yRedMain)
        else:
            BallSprite(xRedMain, yRedMain, xBlueMain, yBlueMain)
        msg_disp("By Vishwas and Purvik",width//2,750,30,White,"Colonna")

        SwapColMain+=1
        py.display.update()

        clock.tick(60)#60

def GameLoop():
    global X,Y,Hw,Hh,Mh,Mw,Gamespeed,SCORE,c1,c2,c3,Gdec,BGblockX1,BGblockX2,BGactivator
    ExitLoop=False
    SCORE=0
    TypeRand,ObsWidth,ObsHeight=[],[],[]
    for i in range(5):
        TypeRand.append(random.randint(1,5))

    for i in range(5):
        if TypeRand[i]==1:
            X.append(0)
            ObsWidth.append(Hw)
            ObsHeight.append(Hh)
        elif TypeRand[i]==2:
            X.append(width-Hw)
            ObsWidth.append(Hw)
            ObsHeight.append(Hh)
        elif TypeRand[i]==3:
            X.append(width/2-Mw/2)
            ObsWidth.append(Mw)
            ObsHeight.append(Mh)
        elif TypeRand[i]==4:
            X.append(width/4-Sw/2)
            ObsWidth.append(Sw)
            ObsHeight.append(Sh)
            for j in range(i,5):
                Y[j]-=50
        elif TypeRand[i]==5:
            X.append(3*width / 4 - Sw / 2)
            ObsWidth.append(Sw)
            ObsHeight.append(Sh)
            for j in range(i,5):
                Y[j]-=50
    RevolutionAngle=0
    xBlue, yBlue, xRed, yRed = 360, 600, 140, 600 #360,600,140,600
    xBallpos = width / 2
    yBallpos = 3 * height / 4
    Revolution_Radius = 110  # 110

    while not ExitLoop:
        global event
        for event in py.event.get():
            if event.type==py.QUIT:
                GameEXIT()
        if event.type ==py.KEYDOWN:
                if RevolutionAngle >= 360:
                    RevolutionAngle-=360
                elif RevolutionAngle<=-360:
                    RevolutionAngle+=360
                if event.key==py.K_RIGHT:
                    RevolutionAngle += 4.5 #4.5
                elif event.key==py.K_LEFT:
                    RevolutionAngle-=4.5 #4.5

                xBlue = (xBallpos + Revolution_Radius * math.cos(math.radians(RevolutionAngle)))
                yBlue = (yBallpos + Revolution_Radius * math.sin(math.radians(RevolutionAngle)))
                xRed = (xBallpos - Revolution_Radius * math.cos(math.radians(RevolutionAngle)))
                yRed = (yBallpos - Revolution_Radius * math.sin(math.radians(RevolutionAngle)))


        Display.fill(BG_Grey)
        if BGactivator==True:
            BG()

        Circumference(width // 2,3 * height // 4,C_Grey)

        Obstacles(X,Y,ObsWidth,ObsHeight)


        halfHitBox = 6 * (2 ** 0.5)
        for i in range(0, 3):
            if (X[i] < xRed + halfHitBox and X[i] + ObsWidth[i] > xRed - halfHitBox and Y[i] < yRed + halfHitBox and Y[
                i] + ObsHeight[i] > yRed - halfHitBox) or (
                    X[i] < xBlue + halfHitBox and X[i] + ObsWidth[i] > xBlue - halfHitBox and Y[
                i] < yBlue + halfHitBox and Y[i] + ObsHeight[i] > yBlue - halfHitBox):
                if c1 == Green:
                    Gamespeed = 40
                elif c2 == Green:
                    Gamespeed = 60
                elif c3 == Green:
                    Gamespeed = 80
                Collided()


        for i in range(5):
            Y[i]+=speed
        if Y[0]>height:
            del(X[0])
            del(Y[0])
            del(TypeRand[0])
            del(ObsHeight[0])
            del(ObsWidth[0])
            TypeRand.append(random.randint(1,5))
            LargeBlockCount=TypeRand.count(4)+TypeRand.count(5)
            if TypeRand[4]==1:
                X.append(0)
                Y.append(-200-50*LargeBlockCount)
                ObsWidth.append(Hw)
                ObsHeight.append(Hh)
            elif TypeRand[4]==2:
                X.append(width-Hw)
                Y.append(-200-50*LargeBlockCount)
                ObsWidth.append(Hw)
                ObsHeight.append(Hh)
            elif TypeRand[4]==3:
                X.append(width/2-Mw/2)
                Y.append(-200-50*LargeBlockCount)
                ObsWidth.append(Mw)
                ObsHeight.append(Mh)
            elif TypeRand[4]==4:
                X.append(width/4-Sw/2)
                Y.append(-200-50*LargeBlockCount)
                ObsWidth.append(Sw)
                ObsHeight.append(Sh)
            elif TypeRand[4] == 5:
                X.append(3*width / 4 - Sw / 2)
                Y.append(-200-50*LargeBlockCount)
                ObsWidth.append(Sw)
                ObsHeight.append(Sh)

        BallSprite(xBlue,yBlue,xRed,yRed)
        msg_disp("Score: "+str(SCORE),70,30,24,Green,"Calibri")
        Gamespeed+=0.01 #0.01
        SCORE+=1 #1

        py.display.update()
        clock.tick(Gamespeed) #60


MainMenu()
py.quit()
quit()



