import random;
from PyQt5.QtWidgets import QApplication, QLabel, QtCore, QtGui
import sys 

def secretsanta(names : list):
    print("--------------------");
    foundG = set(); # will hold the indexes of the names in the dictionary
    foundR = set(); # will hold the indexes of the names that have been assigned a giver
    pairs = {};

    if(len(names) == 1):
        return None;

    for item in names: # populates the hashmap
        pairs[item] = None;

    while ((len(foundG) < len(names)) and (len(foundR) < len(names))):
        giver = random.randint(0, len(names)-1);
        recipient = random.randint(0, len(names)-1);
        if giver not in foundG and (recipient not in foundR):
            if(pairs.get(names[giver]) == None and (giver != recipient)): # or we could pairs[giver]
                pairs[names[giver]] = names[recipient];
                foundR.add(recipient);
                foundG.add(giver);

    for item in pairs:
        print(pairs[item] + " - > " + item);

if __name__ == '__main__':
    # app = QApplication([]);
    # label = QLabel("Hello World")
    # label.show();
    # app.exec_();

    names = [];
    command = input("Type in a name or done: ")

    while(command != "done" and command != ""):
        if(command not in names):
            names.append(command);
        command = input("Type in a name or done: ")

    secretsanta(names);




