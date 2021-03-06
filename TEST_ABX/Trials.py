'''
Created on 2016-09-30

@author: tsico
'''

"""






Pour un trial :


Je veux que je recoive des informations et
je fais apparaitre une croix,
je fais apparaitre text_A pendant x sec,
blanc pour une moment x
je fais apparaitre text_B pendant x sec et deplace 
de x(random) vers la gauche ou droite, 
blanc pour un moment x,
je fais apparaitre text_A ou B pendant x sec et deplace 
de x(random) vers la gauche ou droite,
commence a accepter une reponse que l'image apparait
blanc pendant x sec et accepte tjr la reponse
si x sec est depasser feedback pour attente trop longue


Je veux retourner :
- Reponse = A ou B
- TR
- Historique deplacement


Variable differentes inter trial :
- path texture_a
- path texture_b

Variable meme inter trial :
- path_croix
- temps affichage A et B
- temps blanc
- temps max pour repondre



"""

import random
from psychopy import visual, core, event

def write_instruction(sentence, win, color):
    """
    
    Fonction qui affiche un text et attend pour qu'on appuie sur une touche
    Il y aura une indication d'appuyer sur une touche pour continuer dans le bas.
    
    """
    win = win
    written_instruction = sentence
    instruction = visual.TextStim(win, text=written_instruction, pos=(0.0, 0.2), color = color)
    instruction.draw()
    continuer = visual.TextStim(win, text="Appuyer sur une touche pour continuer", pos=(0.0, -0.6), height = 0.07,
                                color = str(color))
    continuer.draw()
    win.flip()
    thisResp=None
    while thisResp==None:
        allKeys=event.waitKeys()
        for thisKey in allKeys:
            if thisKey == "q" : 
                core.quit()
            thisResp = 1
    
def decompte(explication, temps, win, color):
    """
    Fonction qui cree un decompte d'une duree (temps) en secondes
    Explication sera le texte qui apparait au dessus des secondes, 
    exemple : "L'experimentation commmence dans :"
    """
    
    
    win = win
    secondes = temps
    text_explication = explication
    while secondes > 0 :
        explication_decompte = visual.TextStim(win, text=text_explication, pos=(0.0, 0.2), color = color)
        explication_decompte.draw()
        temps_decompte = visual.TextStim(win, text=str(secondes), pos=(0.0, -0.1), height = 0.5, color = color)
        temps_decompte.draw()
        secondes -= 1
        win.flip()
        core.wait(1)



def LorR():
    side = random.randint(1,2)
    if side == 1 :
        return float(-1)
    else :
        return float(1)
    
def SorB():
    size = random.randint(1,2)
    if size == 1 :
        return float(0.05)
    else :
        return float(0.1)










class ABX_trials(object):
    def __init__(self, primer = None, primer_time = None,pic_time = None, 
                 white_time = None, maxanswer_time = None, folder_path = None, win=None):
        self.pic_time = pic_time
        self.primer_time = primer_time
        self.white_time = white_time
        self.maxanswer_time = maxanswer_time
        self.win = win
        self.primer = visual.ImageStim(self.win, image=primer)
        self.mouse = event.Mouse(visible=False, newPos=None, win=None)
        self.folder_path = folder_path + "\\"
        
        
        
    def trial(self, path_A, path_B, AorB):
        
        
        stimA = visual.ImageStim(self.win, image=self.folder_path + path_A)
        stimBpos = SorB()*LorR()
        stimB = visual.ImageStim(self.win, image=self.folder_path + path_B, pos = (stimBpos,0))
        
        
        self.win.flip()
        core.wait(1)
        self.primer.draw()
        self.win.flip()
        core.wait(self.primer_time)
        
        stimA.draw()
        self.win.flip()
        core.wait(self.pic_time)
        self.win.flip()
        core.wait(self.white_time)
        
        stimB.draw()
        self.win.flip()
        core.wait(self.pic_time)
        self.win.flip()
        core.wait(self.white_time)
        
        
        stimXpos = stimBpos + SorB()*LorR()
        if AorB == 1 :
            stimX = visual.ImageStim(self.win, image=self.folder_path + path_B, pos = (stimXpos,0))
            stimX.draw()
        else :
            stimX = visual.ImageStim(self.win, image=self.folder_path + path_B, pos = (stimXpos,0))
            stimX.draw()
        self.win.flip()
        time_stim = core.getTime()
        
        thisResp=None
        while thisResp==None:
            allKeys=event.waitKeys(maxWait=float(self.pic_time),timeStamped=True)
            if allKeys == None :
                instruction = visual.TextStim(self.win, text="A=1    B=2", pos=(0.0, 0.0), color = "Black")
                instruction.draw()
                self.win.flip()
                allKeys=event.waitKeys(maxWait=float(self.maxanswer_time - self.pic_time),timeStamped=True)
                
            if allKeys == None :
                thisResp = "Nothing"
            else :
                for thisTuple in allKeys:
                    thisResp = [thisTuple[0], thisTuple[1]]
            
        if thisResp[0] == "num_1" :
            thisResp[0] = 1
        elif thisResp[0] == "num_2" :
            thisResp[0] = 2
        elif thisResp[0] == "q" :
            core.quit() 
            event.clearEvents()
        elif thisResp == "Nothing":
            write_instruction(u"Il est important de r\xe9pondre dans les %s secondes apr\xe8s l'apparition du stimulus 3." 
                              %str(self.maxanswer_time), self.win, "black")
        else :
            write_instruction("Mauvaise touche", self.win, "black")
        
            
        if thisResp[0] == 1 or thisResp[0] == 2 :
            thisResp[1] = thisResp[1] - time_stim
            
            
        return thisResp #Dictionnaire [1 ou 2, TR]
    


        

        
        
        
        
        
        