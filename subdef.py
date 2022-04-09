from imports import *

def settings(tkwindow, **kwargs):
    sets, tempicon = dict(zip(['over', 'tit', 'w', 'h', 'x', 'y', 'rszx', 'rszy'], [False, 'Please enter the title.', '1280', '720', '400', '100', False, False])), "icon.ico"
    [exec(f"sets['{key}'] = '{value}'") for key, value in kwargs.items() if key in sets.keys()]
    tkwindow.overrideredirect(sets['over'])
    tkwindow.title(sets['tit'])
    tkwindow.geometry(f"{sets['w']}x{sets['h']}+{sets['x']}+{sets['y']}")
    tkwindow.resizable(sets['rszx'], sets['rszy'])
    with open(tempicon, "wb") as iconFile:
        iconFile.write(base64.b64decode(icon))
    tkwindow.iconbitmap(tempicon)
    os.remove(tempicon)

def buttonsettings(root, fsize=30, **options):
    bfont = tkfont.Font(family="Consolas", size=fsize)
    button = tk.Button(root, width=8, height=3, relief='groove', font=bfont)
    button.configure(**options)
    return button

def alphabetsettings(option):
    # noinspection PyUnusedLocal
    def searchEvent(e):
        searchText = searchInput.get("1.0", tk.END).strip("\n")
        searchInput.delete(1.0, tk.END)
        try:
            meaningLabel.configure(text=BeautifulSoup(requests.get(f"http://endic.naver.com/search.nhn?query={searchText}").content, 'lxml').find('dl', {'class': 'list_e2'}).find('dd').find('span', {'class': 'fnt_k05'}).get_text())
        except:
            if searchText in translateDict.keys(): meaningLabel.configure(text=translateDict[searchText.lower()])
            else: meaningLabel.configure(text="단어의 뜻을 찾을 수 없습니다.")
    # noinspection PyUnusedLocal
    def selectList(e):
        try:
            selected = searchTipList.get(searchTipList.curselection()[0])
            searchInput.delete(1.0, tk.END)
            searchInput.insert(1.0, selected)
        except:
            pass
    alphabetWindow, tkFont = tk.Tk(), ("Consolas", 23)
    settings(alphabetWindow, tit=option, rszx=False, rszy=False, w=640, h=480)
    meaningLabel = tk.Label(alphabetWindow, text="단어를 입력해서 엔터키를 누르면 뜻이 나옵니다.", font=("Consolas", 12), wraplength=600)
    meaningLabel.grid(row=0, column=0, pady=20)
    searchFrame = tk.Frame(alphabetWindow)
    searchInput = tk.Text(searchFrame, width=35, height=1, font=tkFont)
    searchTipFrame = tk.Frame(searchFrame)
    searchTipList = tk.Listbox(searchTipFrame, width=34, height=9, font=tkFont)
    if option in ascii_uppercase : [searchTipList.insert(i, w) for i, w in enumerate(translateDict[option.lower()].keys())]
    else : [searchTipList.insert(i, w) for i, w in enumerate(wordList)]
    alphabetWindow.bind("<Return>", searchEvent)
    searchTipList.bind('<<ListboxSelect>>', selectList)
    searchTipScrollbar = tk.Scrollbar(searchTipFrame, orient="vertical", command=searchTipList.yview)
    searchTipList.pack(side="left", fill="y")
    searchTipScrollbar.pack(side="right", fill="y")
    searchInput.grid(row=0, column=0)
    searchTipFrame.grid(row=1, column=0)
    searchFrame.grid(row=1, column=0, padx=20)
    return alphabetWindow