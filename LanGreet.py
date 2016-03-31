#Language Program
#by Keary Mobley

from pygame import *


#=====================================
def LanGreet(a):
    Lan_select = {'ENGL': ['Hello', 'hello.wav'],
                  'SPAN': ['Hola', 'hola.wav'],
                  'FREN': ['Bonjour', 'bonjour.wav']
                 };
    try:
       return Lan_select[a]
    except:
       print "The input was invalid. Try again"



'''
    if a == 'ENGL':
        b = "Hello"
        c = 'hello.wav'
        return b,c
    elif a == 'SPAN':
        b = "Hola"
        c = 'hola.wav'
        return b,cls
    elif a == 'FREN':
        b = 'Bonjour'
        c = 'bonjour.wav'
        return b,c
    elif a == 'DUTC':
        b = 'Hallo'
        c = 'hallo.wav'
        return b,c
    elif a == 'GERM':
        b = 'Hallo'
        c = 'hallo.wav'
        return b,c
    #elif a == 'RUSS':
     #   b = "(Privet!)"
      #  c = 'privet.wav'
       # return b,c
    elif a == 'ITAL':
        b = 'Ciao'
        c = 'ciao.wav'
        return b,c
    #elif a == 'ARAB':
        #b = "(as-sal 'alaykum)"
        #c = 'assalam alaykum.wav'
        #return b,c
    #elif a == 'HEBR':
     #   b = '(salom)'
      #  c = 'salom.wav'
      #  return b,c
    #elif a == 'KORE':
     #   b = "(Annyeonghaseyo)"
      #  c = 'annyoung.wav'
        #return b,c
    #elif a == 'GREE':
     #   b = '! (ya)'
      #  c = 'ya.wav'
       # return b,c
    #elif a == 'JAPA':
     #   b = "(Konnichiwa)"
      #  c = 'konnichiwa.wav'
       # return b,c
    #elif a == 'CHIN':
     #   b = "(Ni Hao)"
      #  c = 'nihao.wav'
       # return b,c
    else:
        print("Either the spelling is incorrect")
        print("Or the language is not supported at this time.")
   '''     

#-------------------------------------
def PrintIntro():
    print("This is program displays hello in many different languages.")
    print("Also provided is an audio clip to help with pronunciation.")
    print("Languages can be accessed by inputing the correct abbreviations")
    print("The correct abbreviation is the first four letters of the language.")
    print("For example Russian would be  RUSS.")
    
    
#-------------------------------------
def main():
    PrintIntro()
    uinput = raw_input("Please insert language choice.")
    print LanGreet(uinput)


    '''
    win = GraphWin("Language Greetings", 800, 600)
    win.setCoords(0.0, 0.0, 3.0, 4.0)
    
    # Draw the interface
    
    Language = Text(Point(1,3), "   Language:")
    Language.setSize(30)
    Language.setFace('times roman')
    Language.setFill('blue')
    Language.setStyle('italic')
    Language.draw(win)
    Hello = Text(Point(0.75,2), "Hello:")
    Hello.setSize(30)
    Hello.setFace('times roman')
    Hello.setStyle('italic')
    Hello.setFill('green')
    Hello.draw(win)
    input1 = Entry(Point(2,3), 5)
    input1.setText("LANG")
    input1.draw(win)
    output = Text(Point(2,2),"")
    output.setSize(30)
    output.setFill('red')
    output.draw(win)
    rect = Rectangle(Point(1,.5), Point(2,1))
    rect.setFill('white')
    rect.draw(win)
    button = Text(Point(1.5,.75),"Translate")
    button.draw(win)
    
    

    # wait for a mouse click
    win.getMouse()

    # evaluate user input
    uinput = input1.getText()
    txtfile, wavfile = LanGreet(uinput)
    

    # display output and change button
    output.setText(txtfile)
    winsound.PlaySound(wavfile,winsound.SND_FILENAME)
    button.setText("Quit")

    # wait for click and then quit
    win.getMouse()
    win.close()
    '''
    

main()
