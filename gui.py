
import tkinter as tk   


TITLE_FONT = ("Helvetica", 18 )

class SampleApp(tk.Tk):
    
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
    

        self.frames = {}
        for F in (StartPage, search, quit):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

class quit(tk.Frame):
    def quit(self):
        global root
        root.quit()

    #root = Tk()
    #while True:
    #    Button(root, text="Quit", command=quit).pack()
   #     root.mainloop()

class StartPage(tk.Frame):

    def __init__(self, parent, controller, quit):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Cardiff university, Personal Tutor system ", font=TITLE_FONT)
        label.pack(side="top", fill="x", pady=10)

        button1 = tk.Button(self, text="Continue",
                            command=lambda: controller.show_frame("search"))
        button2 = tk.Button(self, text="Exit ",
                            command=lambda: controller.show_frame("quit"))#exit tk function
        button1.pack()
        button2.pack()


class search(tk.Frame):

    def __init__(self, parent, controller, quit):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Please choose a search", font=TITLE_FONT)
        label.pack(side="top", fill="x", pady=10)
        button1 = tk.Button(self, text="list of tutees for a particular personal tutor",
                            command=lambda: controller.show_frame(""))
        button2 = tk.Button(self, text=" Search for individual students ",
                            command=lambda: controller.show_frame(""))#links to function needs to trigger input 
        button3 = tk.Button(self, text="Quota of tutees",
                            command=lambda: controller.show_frame(""))
        button4 = tk.Button(self, text="Back",
                           command=lambda: controller.show_frame("StartPage"))
        button1.pack()
        button2.pack()
        button3.pack()
        button4.pack()
                                                                  

if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
