import sys
import os
import cProfile
import tkinter as tk
from string import *
import tkinter.font as tkfont
import requests
from bs4 import BeautifulSoup
from wordList import wordList
from meaningList import meaningList
from icon import icon
import base64
translateDict = {a: {} for a in ascii_lowercase}
for word, meaning in zip(wordList, meaningList):
    translateDict[word[:1]][word] = meaning
