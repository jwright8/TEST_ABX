'''
Created on 2016-09-30

@author: tsico
'''
from psychopy import data, gui, visual
from Trials import ABX_trials, write_instruction, decompte
import json

script_folder_path = "C:\Users\\tsico\\workspace\\TEST_ABX\\"
texture_folder_location = "C:\\Exp\\Textures3inv\\"

param_name = "parametres.json"


with open(script_folder_path + param_name, "r") as params_file :
    params = json.load(params_file)

expInfo = {'participant':'', 'session':'001'}
gui.DlgFromDict(dictionary=expInfo, title="ABX")
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = "ABX"

with open(script_folder_path + params["Path_textures"], "r") as trials_file :
    list_of_trials = json.load(trials_file)
    

file_name = expInfo["participant"]+ "-" + params[u"Path_textures"][len(params[u"Path_textures"])-18:len(params[u"Path_textures"])-12] + "-" +params[u"Path_textures"][len(params[u"Path_textures"])-7:len(params[u"Path_textures"])-5]

win = visual.Window(fullscr = True, color="white")
Result_data = data.ExperimentHandler(name='ABX', version='1', extraInfo=expInfo, 
                                     runtimeInfo=None, originPath=params["Data_folder"], savePickle=False, 
                                     saveWideText=True, dataFileName=file_name, 
                                     autoLog=True)


ABX_trials = ABX_trials(primer = texture_folder_location + str(params[u"Primer"]), 
                        primer_time = float(params[u"Primer_time"]),
                        pic_time = float(params[u"Pic_time"]), 
                        white_time = float(params[u"White_time"]),
                        maxanswer_time = float(params[u"Maxanswer_time"]), 
                        folder_path = texture_folder_location + str(params[u"PRATIQUE_folder"]),
                        win = win)


write_instruction(u"Bonjour, vous vous appr\xeatez \xe0 faire une t\xe2che de type ABX.  Nous vous d\xe9crirons d'abords la t\xe2che, vous aurez ensuite quelques essais de pratique, puis la t\xe2che commencera. ", win, "Black")
write_instruction(u"Pour chaque essai, vous verrez 3 textures une \xe0 la suite de l'autre. La premi\xe8re et la deuxi\xe8me seront diff\xe9rentes, mais la troisi\xe8me sera soit la premi\xe8re ou la deuxi\xe8me.", win, "Black")
write_instruction(u"Vous devrez d\xe9terminer de laquelle il s'agit en appuyant sur 1 ou 2 sur votre clavier num\xe9rique. Vous pouvez appuyer d\xe8s l'apparition de la troisi\xe8me image et aurez %s secondes apr\xe8s l'apparition de celle-ci pour r\xe9pondre. "%params[u"Maxanswer_time"], win, "Black")
write_instruction(u"\xcates-vous pr\xeat \xe0 commencer la pratique?", win, "Black")
decompte(u"La pratique commmence dans :", 5, win, "Black")



for this_trial in params[u"PRATIQUE_LIST"] :
    ABX_trials.trial(this_trial["TextureA"], this_trial["TextureB"], this_trial["X"])

ABX_trials.folder_path = texture_folder_location + str(params[u"Texture_folder"])+ "\\"


write_instruction(u"Appuyez si vous \xeates pr\xeat \xe0 commencer la t\xe2che principale.", win, "Black")
decompte(u"L'exp\xe9rimentation commmence dans :", 5, win, "Black")




n = 0

while len(list_of_trials) > 117 :

    this_trial = list_of_trials[0]
    trial = ABX_trials.trial(this_trial["TextureA"], this_trial["TextureB"], this_trial["X"])
    if str(trial[0]).isdigit() :
        trial_res_info = {}
        n += 1
        trial_res_info["Type"] = this_trial["Type"]
        trial_res_info["AorB"] = this_trial["X"]
        trial_res_info["TR"] = trial[1]
        if this_trial["X"] - trial[0] == 0 :
            trial_res_info["Resultat"] = 1
        else :
            trial_res_info["Resultat"] = 0
            
        trial_res_info["CategorieA"] = this_trial["CategorieA"]
        trial_res_info["CategorieB"] = this_trial["CategorieB"]
        trial_res_info["n"] = n
        for item in trial_res_info :
            Result_data.addData(item, trial_res_info[item])
        Result_data.nextEntry()
        list_of_trials.remove(this_trial)
    else :
        list_of_trials.append(this_trial)
        list_of_trials.remove(this_trial)


    
    











