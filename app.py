import tkinter as tk
from tkinter import filedialog
from tkinter import font as tkFont  # for convenience
import os
import json
import codecs
import string

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
            return ("Word not found!")
        return self.search(key)

list_1 = []
xmlFile = ""

def main():
    t = Trie()
    def UploadAction(event=None):
        global list_1
        global xmlFile
        xmlFile = filedialog.askdirectory()
        list_1 = os.listdir(xmlFile)
        for row in list_1:
            print(row)
    window = tk.Tk()
    window.geometry("500x500")
    chooseButton = tk.Button(window, text='Choose File', bg='yellow2', fg='white', command=UploadAction)
    chooseButton.place(x=0, y=0, width=500, height=100)

    window.mainloop()

    accepted_list = string.ascii_letters
    for file in list_1:
        file_id = int(file.replace('.txt', ''), 10)
        print(file_id)

        with codecs.open("C:\\Users\\BoshBosh\\Desktop\\DS\\questions\\" + file, "r", encoding='utf-8', errors='ignore') as file_1:
            file_con = file_1.read()
            for x in file_con:
                if not x in accepted_list:
                    file_con = file_con.replace(x, " ")

            list_2 = file_con.split()
            print(list_2)
            for word in list_2:
                t.insert(word.lower(), file_id)

    while True:
        input_search = input("Enter a word: ")
        output = t.get_ids(input_search.lower())
        print(output)

if __name__ == '__main__':
    main()
