import pygame
import pygame.gfxdraw
import sys
import time
import random
import domande
def check_score(answered="wrong"):
    ''' here we check if the answer is right '''
    global qnum, points
    
    # until there are domande.domande (before last)
    hit.play() # click sound
    if qnum < len(domande.domande):
        print(qnum, len(domande.domande))
        if answered == "right":
            time.sleep(.1) # to avoid adding more point when pressing too much
            points += 1
            # Show the score text
        qnum += 1 # counter for next question in the list
        score.change_text(str(points))
        # Change the text of the question
        title.change_text(domande.domande[qnum-1][0], color="cyan")
        # change the question number
        num_question.change_text(str(qnum))
        show_question(qnum) # delete old buttons and show new
        

    # for the last question...
    elif qnum == len(domande.domande):
        print(qnum, len(domande.domande))
        if answered == "right":
            kill()
            time.sleep(.1)
            points +=1
        score.change_text("You reached a score of " + str(points))
    time.sleep(.5)

def check_score(answered="wrong"):
    ''' here we check if the answer is right '''
    global qnum, points
    
    # until there are domande.domande (before last)
    hit.play() # click sound
    if qnum &lt; len(domande.domande):
        print(qnum, len(domande.domande))
        if answered == "right":
            time.sleep(.1) # to avoid adding more point when pressing too much
            points += 1
            # Show the score text
        qnum += 1 # counter for next question in the list
        score.change_text(str(points))
        # Change the text of the question
        title.change_text(domande.domande[qnum-1][0], color="cyan")
        # change the question number
        num_question.change_text(str(qnum))
        show_question(qnum) # delete old buttons and show new
        
 
    # for the last question...
    elif qnum == len(domande.domande):
        print(qnum, len(domande.domande))
        if answered == "right":
            kill()
            time.sleep(.1)
            points +=1
        score.change_text("You reached a score of " + str(points))
    time.sleep(.5)