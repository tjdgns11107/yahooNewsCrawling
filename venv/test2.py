import tkinter as tk
import MainCrawling as mc
import GetData as gd

TITLE_FONT = ("Helvetica", 24, "bold")
BUTTON_FONT_1 = ("Helvetica", 16, "bold")
BUTTON_FONT_2 = ("Helvetica", 14)

class ScrawlingApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title('News Scrawling')
        self.geometry("1200x960")
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.frames = {}
        frameTuple = (StartPage, Setting, TimeSetting, SearchSetting, NewsPage, ViewNews)

        for F in frameTuple:
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="news")

        # self.show_frame("StartPage")
        self.show_frame("NewsPage")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        def getdata():
            str = ['ソフトバンク']
            mc.MainCrawling(str)

        tk.Frame.__init__(self, parent)
        self.controller = controller

        label = tk.Label(self, text="News Scrawling", font=TITLE_FONT)
        settingButton = tk.Button(self, text="설정",
                                  command=lambda: controller.show_frame("Setting"))
        newsButton = tk.Button(self, text="뉴스 확인",
                               width=20, height=2, font=BUTTON_FONT_1,
                               command=lambda: controller.show_frame("NewsPage"))
        getDataButton = tk.Button(self, text="정보 수집", width=20, height=2 , font=BUTTON_FONT_1,
                                command=getdata)
        settingButton.pack(anchor='ne', padx=30, pady=30)
        label.pack(fill="x", pady=120)
        newsButton.pack(pady=100)
        getDataButton.pack()






class Setting(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label = tk.Label(self, text="설정", font=TITLE_FONT)
        timeButton = tk.Button(self, text="시간대 확인", width=25, height=3, font=BUTTON_FONT_2,
                               command=lambda: controller.show_frame("TimeSetting"))
        searchButton = tk.Button(self, text="검색어 확인", width=25, height=3, font=BUTTON_FONT_2,
                                 command=lambda: controller.show_frame("SearchSetting"))
        checkButton = tk.Button(self, text="홈으로", font=BUTTON_FONT_1, width=15, height=2,
                                command=lambda: controller.show_frame("StartPage"))

        label.pack(fill="x", pady=150)
        timeButton.pack(pady=30)
        searchButton.pack(pady=30)
        checkButton.pack(pady=80)


class TimeSetting(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label = tk.Label(self, text="시간대 설정", font=TITLE_FONT)
        checkButton = tk.Button(self, text="저장", font=BUTTON_FONT_1, width=15, height=2,
                                command=lambda: controller.show_frame("Setting"))

        label.pack(fill="x", pady=150)
        checkButton.pack(pady=30)

class SearchSetting(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label = tk.Label(self, text="검색어 설정", font=TITLE_FONT)
        checkButton = tk.Button(self, text="저장", font=BUTTON_FONT_1, width=15, height=2,
                                command=lambda: controller.show_frame("Setting"))

        label.pack(fill="x", pady=150)
        checkButton.pack(pady=30)

class NewsPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        #데이터 가져오기
        titles, contents, medias, keywords, days = gd.GetData.getData(self)

        label = tk.Label(self, text="News", font=TITLE_FONT)
        checkButton = tk.Button(self, text="저장", font=BUTTON_FONT_1, width=15, height=2,
                                command=lambda: controller.show_frame("Setting"))
        fram1 = tk.Frame(self, relief="solid", bd=1)
        scrollbar = tk.Scrollbar(fram1)
        scrollbar.pack(side="right", fill="y")

        listbox = tk.Listbox(fram1, yscrollcommand  = scrollbar.set , width=120, height=35)
        for idx in range(1, len(titles)):
            listbox.insert(idx, str(idx) +"  "+titles[idx-1])
        listbox.bind('<<ListboxSelect>>', NewsPage.event_for_listbox)
        listbox.pack()

        label.pack(fill="x", pady=60)
        fram1.pack(pady=30)
        checkButton.pack(pady=30)

    def event_for_listbox(self):


        print("Hello Event")
        # controller.show_frame("Setting")

class ViewNews(tk.Frame):
    def __init__(self,parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller


if __name__ == "__main__":
    app = ScrawlingApp()
    app.mainloop()
