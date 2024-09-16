import tkinter

class UserInterface:

    def __init__(self):
        self.window = tkinter.Tk()
        self.window.title("Calories Tracker")
        self.window.geometry("1000x1000")

        self.bg_image = tkinter.PhotoImage(file="Images/UI/login_bg.png")

        # background canvas
        self.bg_canvas = tkinter.Canvas(self.window, height=1000, width=1000, highlightthickness=0, bd=0)
        self.bg_canvas.create_image(500, 500, image= self.bg_image)
        self.bg_canvas.place(x=0, y=0)

    def exit_window(self):
        self.window.mainloop()


ui = UserInterface()
ui.exit_window()