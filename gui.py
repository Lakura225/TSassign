
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
        for F in (StartPage, tutorlog, seniorlog, senior, tutor):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Welcome, please choose a log in ", font=TITLE_FONT)
        label.pack(side="top", fill="x", pady=10)

        button1 = tk.Button(self, text="Tutor log in ",
                            command=lambda: controller.show_frame("tutorlog"))
        button2 = tk.Button(self, text="Senior personal tutor log in ",
                            command=lambda: controller.show_frame("seniorlog"))
        button1.pack()
        button2.pack()


class tutorlog(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Tutor Log in", font=TITLE_FONT)
        label.pack(side="top", fill="x", pady=10)
        button1 = tk.Button(self, text="Back",
                           command=lambda: controller.show_frame("StartPage"))
        button2 = tk.Button(self, text="Enter",
                            command=lambda: controller.show_frame("tutor"))
        button2.pack()
        button1.pack()

class seniorlog(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Senior personal tutor Log in", font=TITLE_FONT)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Back",
                           command=lambda: controller.show_frame("StartPage"))
        button1 = tk.Button(self, text="Enter",
                            command=lambda: controller.show_frame("senior"))
        button1.pack()
        button.pack()
class senior(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Search", font=TITLE_FONT)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Back",
                           command=lambda: controller.show_frame("seniorlog"))
        button.pack()

class tutor(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Search", font=TITLE_FONT)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Back",
                           command=lambda: controller.show_frame("tutorlog"))
        button.pack()




if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
