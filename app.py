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
        SetOfIds = {None}
        SetOfIds.remove(None)
        self.SetOfIds = SetOfIds


class Trie:
    def __init__(self):
        self.root = self.getNode()
    def getNode(self):
        return TrieNode()
    def _charToIndex(self, ch):
        return ord(ch) - ord('a')
    def insert(self, key, file_id):
        if not self.search(key):
            my_root = self.root
            length = len(key)
            for level in range(length):
                index = self._charToIndex(key[level])
                if not my_root.children[index]:
                    my_root.children[index] = self.getNode()
                my_root = my_root.children[index]
            my_root.isEndOfWord = True
            (my_root.SetOfIds).add(file_id)
        else:
            self.search(key).add(file_id)
    def search(self, key):
        my_root = self.root
        length = len(key)
        for level in range(length):
            index = self._charToIndex(key[level])
            if not my_root.children[index]:
                return False
            my_root = my_root.children[index]
        if my_root != None and my_root.isEndOfWord:
            return my_root.SetOfIds
        return my_root != None and my_root.isEndOfWord
    def get_ids(self, key):
        if not self.search(key):
            return []
        return self.search(key)

list_1 = []
xmlFile = ""


def main():
    t = Trie()

    def openFile(location, word):
        thirdWindow = Toplevel(window)
        thirdWindow.geometry("700x500")
        thirdWindow.title(location)
        column2 = scrolledtext.ScrolledText(thirdWindow)
        column2.place(y=0, x=0, width=700, height=500)
        indexOFLines = []
        fileLocation = xmlFile + "/" + str(location)
        with open(fileLocation, "r") as myfile:
            data = myfile.readlines()
        index = 0

        for row in data:
            if word.lower() in row.lower():
                indexOFLines.append(str(index))

            index += 1
        for x in range(len(data)):
            if str(x) in indexOFLines:
                line = data[x].split()

                for ele in line:
                    if ele.replace('"', '').lower() == word.lower():
                        column2.insert(INSERT, ele, 'name')
                        column2.tag_config('name', background='yellow')
                        column2.insert(INSERT, " ")
                    else:
                        column2.insert(INSERT, ele + " ")
                column2.insert(INSERT, "\n")
            else:
                column2.insert(INSERT, data[x] + "\n")

    def search2(word):
        input_search = word
        output = list(t.get_ids(input_search.lower()))
        output_2 = len(t.get_ids(input_search.lower()))
        if output_2 == 0:
            messagebox.showinfo('warning', "Word not found!")
        else:
            searchWindow = Toplevel(window)
            searchWindow.geometry("400x500")
            output.sort()

            column2 = Listbox(searchWindow)
            column2.place(y=0, x=0, width=250, height=500)
            openButton = Button(searchWindow, text='Open', command=lambda: openFile(column2.get(column2.curselection()), word))
            openButton.place(x=300, height=50, y=200, width=50)
            countLabel = Label(searchWindow , text = "Number of files: " + str(output_2))
            countLabel.place(y=20, x=260)

            for row in output:
                column2.insert(END, str(row) + ".txt")

    def UploadAction(event=None):
        global list_1
        global xmlFile
        xmlFile = filedialog.askdirectory()
        list_1 = os.listdir(xmlFile)
        buildButton = tk.Button(window, text='Press Build and wait while the files are uploaded', bg='yellow2', fg='blue3', command=build)
        buildButton.place(x=0, y=100, width=500, height=50)

    window = tk.Tk()
    window.geometry("500x500")
    chooseButton = tk.Button(window, text='Choose a Folder', bg='yellow2', fg='blue3', command=UploadAction)
    chooseButton.place(x=0, y=0, width=500, height=100)

    def build():
        global word
        accepted_list = string.ascii_letters
        for file in list_1:
            file_id = int(file.replace('.txt', ''), 10)
            file_1= open(xmlFile + "/" + file, "r", encoding='utf-8', errors='ignore')
            file_con = file_1.read()
            for x in file_con:
                if not x in accepted_list:
                    file_con = file_con.replace(x, " ")
            list_2 = file_con.split()
            for word in list_2:
                t.insert(word.lower(), file_id)
        word = Entry(window)
        word.place(x=180, y=200, width=150)
        searchButton = Button(window, text="search", command=lambda: search2(word.get()))
        searchButton.place(x=250, y=220)

    window.mainloop()

if __name__ == '__main__':
    main()
