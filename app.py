import tkinter as tk
from tkinter import filedialog
from tkinter import font as tkFont  # for convenience
import os
import json
"""

list_1=[]


xmlFile = ""
def UploadAction(event=None):
    global list_1
    global xmlFile
    xmlFile = filedialog.askdirectory()
    list_1 = os.listdir(xmlFile)
    for row in list_1 :
        print(row )

print(111)
window = tk.Tk()
window.geometry("500x500")
chooseButton = tk.Button(window, text='Choose File', bg='yellow2' , fg='white'  ,command=UploadAction)
chooseButton.place(x = 0 , y=0 , width =500 , height = 100 )

window.mainloop()

#######################
import codecs
words={None}
words.clear()
#lot_id_con=[] #lot means list of tups.
#tup_1=()
d_id_con={}
d_word_id={}
#list_1=(os.listdir("C:\\Users\\BoshBosh\\Desktop\\DS\\questions")) #list_1 is a list of all 100,002 files
##
print(list_1[0])
for file in list_1:
    file_id=int(file.replace('.txt',''),10)
    with codecs.open("C:\\Users\\BoshBosh\\Desktop\\DS\\questions\\"+file, "r", encoding='utf-8', errors='ignore') as file_1:
        #global d_id_con
        file_con=file_1.read()
        #tup_1=(file_id,file_con)
        d_id_con[file_id] = file_con
        #lot_id_con.append(tup_1)
    list_2=file_con.split();
    for word in list_2:
        words.add(word)
words=list(words)
print(d_id_con[0])
print(d_id_con[12])
print(len(d_id_con))
print(words[0])
print(words[15])
for word_2 in words:
    list_3=[]
    #global d_word_id
    for id,con in d_id_con.items():
        if word_2 in con:
            list_3.append(id)
    d_word_id[word_2]=str(list_3)
    #list_3.clear()
#######################################
print(str(d_word_id))
print(len(d_word_id))
print(type(d_word_id))
print(type(str(d_word_id)))
with open('C:\\Users\\BoshBosh\\Desktop\\DS\\database.txt',mode='w') as file_2:
    file_2.write(str(d_word_id))

with open('C:\\Users\\BoshBosh\\Desktop\\DS\\database.txt',mode='r') as file_2:
    d3=file_2.read()
    d2=d3.replace("'","\"")
    d_word_id_saved = json.loads(d2)

#######################################
print(len(words))
print(d_word_id['Which'])
print(len(d_word_id))

##################################################################################################################
#hna ya hala
"""
d={'pp': str([1,5,9]), 'qq': str([2,52,7]), 'tt': str([54,6,103])}

print(type(d))
with open('C:\\Users\\BoshBosh\\Desktop\\DS\\database.txt',mode='w') as file_2:
    file_2.write(str(d))

with open('C:\\Users\\BoshBosh\\Desktop\\DS\\database.txt',mode='r') as file_2:
    d3=file_2.read()
    print(d3)
    print(type(d3))
    d2=d3.replace("'","\"")
    print(d2)
    print(type(d2))
    #file_2.seek(0)
    res = json.loads(d2)
    print(res)
    print(type(res))



