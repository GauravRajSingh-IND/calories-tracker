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

        # Add landing page
        self.landing_page()

    def exit_window(self):
        self.window.mainloop()

    def landing_page(self):
        # welcome text.
        self.bg_canvas.create_text(500, 150, text="Welcome to Calories Tracker", font=('arial', 25, 'bold'),
                                   fill="snow")
        self.bg_canvas.place(x=0, y=0)

        # Button - New User.
        self.new_user = tkinter.Button(self.window, text="Create a new user", width=20, font=('arial', 25, 'bold'),
                                       bd=0, highlightthickness=0, height=1)
        self.new_user.place(x=350, y=455)

        # Button - Existing User
        self.exist_user = tkinter.Button(self.window, text="Link to existing user", width=20,
                                         font=('arial', 25, 'bold'),
                                         bd=0, highlightthickness=0, height=1)
        self.exist_user.place(x=350, y=540)


ui = UserInterface()
ui.exit_window()