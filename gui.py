import tkinter as tk
from tkinter import filedialog
from tkinter import font as tkFont  # for convenience
import os
import json
import codecs
import string
from tkinter import *
from tkinter import messagebox
from tkinter import scrolledtext
from tkinter import Canvas
from tkinter import ttk
from functools import partial


class TrieNode:

    def __init__(self):
        self.children = [None] * 26
        self.isEndOfWord = False
        setofids = {None}
        setofids.remove(None)
        self.setofids = setofids

class Trie:

    def __init__(self):
        self.root = self.getNode()

    def getNode(self):
        return TrieNode()

    def _charToIndex(self, ch):
        return ord(ch) - ord('a')

    def insert(self, key, file_id):
        if not self.search(key):
            pCrawl = self.root
            length = len(key)
            for level in range(length):
                index = self._charToIndex(key[level])
                if not pCrawl.children[index]:
                    pCrawl.children[index] = self.getNode()
                pCrawl = pCrawl.children[index]
            pCrawl.isEndOfWord = True
            (pCrawl.setofids).add(file_id)
        else:
            self.search(key).add(file_id)

    def search(self, key):
        pCrawl = self.root
        length = len(key)
        for level in range(length):
            index = self._charToIndex(key[level])
            if not pCrawl.children[index]:
                return False
            pCrawl = pCrawl.children[index]
        if pCrawl != None and pCrawl.isEndOfWord:
            return pCrawl.setofids
        return pCrawl != None and pCrawl.isEndOfWord

    def get_ids(self, key):
        if not self.search(key):
            return ( "Word not found!")
        return self.search(key)


list_1 = []
xmlFile = ""
# word = ""


def main():
    # word = ""
    t = Trie()
    def openFile(location , word) :
        thirdWindow = Toplevel(window)
        thirdWindow.geometry("700x500")
        thirdWindow.title(location)
        column2 = scrolledtext.ScrolledText(thirdWindow)
        column2.place(y = 0 , x = 0 , width=700 , height= 500)

        indexOFLines = []
        fileLocation = xmlFile + "/" + str(location)
        with open (fileLocation, "r") as myfile:
            data=myfile.readlines()
        index = 0
        print(word)
        for row in data :
            if word.lower() in row.lower() :
                indexOFLines.append(str(index))
                print('yes')
            index +=1   
    
        for x in range(len(data)) :
            if str(x) in indexOFLines :
                line = data[x].split()
                print(data[x])
                for ele in line :
                    # print(word.replace('"', '').lower())
                    if ele.replace('"', '').lower() == word.lower() :
                        column2.insert(INSERT, ele ,'name')
                        column2.tag_config('name', background='yellow') 
                        column2.insert(INSERT, " ")
                    else: 
                        column2.insert(INSERT, ele + " " )

                column2.insert(INSERT,  "\n" )
            else :
                column2.insert(INSERT, data[x]+ "\n" )

    def search2(word) :
        input_search = word
        output = t.get_ids(input_search.lower())
        if output  == "Word not found!" :
            messagebox.showinfo('warning', "Word not found!")
        else :
            searchWindow = Toplevel(window)
            searchWindow.geometry("400x500")
            location = 0
            flag = 0
            xLocation = 0
            output = list(t.get_ids(input_search.lower()))
            output_2 = len(t.get_ids(input_search.lower()))
            output.sort()
            print (f'Number of files containing this word = {output_2}')
            print(f'These files are: {output}')
            print(word)
            counter = 0 
            column2 = Listbox(searchWindow)
            column2.place(y = 0 , x = 0 , width=250 , height= 500)
            openButton = Button(searchWindow , text = 'open' , command = lambda:openFile(column2.get(column2.curselection()) , word)) 
            openButton.place(x = 300 , height =50 , y = 200  , width=50)
            
            for row in output :
                # fileButton = Button(searchWindow , text = row , command = partial(openFile , row )) 
                # fileButton.place(x = xLocation , height =30 , y = flag  , width=50)
                # if xLocation == 1400 :
                #     xLocation=0
                #     flag +=30
                # else :
                #     xLocation+=50
                column2.insert(END, str(row) + ".txt")

    def UploadAction(event=None):
        global list_1
        global xmlFile
        xmlFile = filedialog.askdirectory()
        list_1 = os.listdir(xmlFile)
        buildButton = tk.Button(window, text='Build', bg='yellow2', fg='white', command=build)
        buildButton.place(x=0, y=100, width=500, height=50)

    window = tk.Tk()
    window.geometry("500x500")
    chooseButton = tk.Button(window, text='Choose File', bg='yellow2', fg='white', command=UploadAction)
    chooseButton.place(x=0, y=0, width=500, height=100)
    # word 
   
   

    def build() :
        global word 
        accepted_list = string.ascii_letters
        for file in list_1:
            file_id = int(file.replace('.txt', ''), 10)
            print(file_id)

            with codecs.open(xmlFile + "/" + file, "r", encoding='utf-8', errors='ignore') as file_1:
                file_con = file_1.read()
                for x in file_con:
                    if not x in accepted_list:
                        file_con = file_con.replace(x, " ")

                list_2 = file_con.split()
                print(list_2)
                for word in list_2:
                    t.insert(word.lower(), file_id)
    # while True:
        word = Entry(window)
        word.place(x = 180 , y =200 , width =150)
        # searchWord = word.get()
        searchButton = Button(window , text = "search" ,  command =lambda:search2(word.get()))
        searchButton.place(x=250 , y =220)


    window.mainloop()


if __name__ == '__main__':
    main()
