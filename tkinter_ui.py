import json
import tkinter
from tkinter import StringVar

from get_calories import Calories

class UserInterface:

    def __init__(self):

        self.username = None
        self.userdata = None

        self.existing_user_window_password = None
        self.existing_user_window_username = None

        self.calories = Calories()

        self.existing_user_window = None
        self.bg_canvas_existing_user = None

        self.new_user_window = None
        self.bg_canvas_new_user = None

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
                                       bd=0, highlightthickness=0, height=1, command= self.launch_new_user)
        self.new_user.place(x=350, y=455)

        # Button - Existing User
        self.exist_user = tkinter.Button(self.window, text="Link to existing user", width=20,
                                         font=('arial', 25, 'bold'),
                                         bd=0, highlightthickness=0, height=1, command= self.launch_existing_user)
        self.exist_user.place(x=350, y=540)

    def launch_existing_user(self):
        self.existing_user_window = tkinter.Toplevel()
        self.existing_user_window.title("Signup")
        self.existing_user_window.geometry("1000x1000")

        self.bg_canvas_existing_user = tkinter.Canvas(self.existing_user_window, height=1000, width=1000, highlightthickness=0, bd=0)
        self.bg_canvas_existing_user.create_image(500, 500, image= self.bg_image)

        # username input area
        self.username_var = tkinter.StringVar()
        self.password_var = tkinter.StringVar()

        self.existing_user_window_username = tkinter.Entry(self.existing_user_window, textvariable=self.username_var,
                                                      font=('arial', 25, 'bold'), bg="snow", bd= 0, fg= "black",
                                                      highlightthickness= 0)
        self.existing_user_window_username.place(x=350, y=455)

        self.existing_user_window_password = tkinter.Entry(self.existing_user_window, textvariable=self.password_var,
                                                      font=('arial', 25, 'bold'), bg="snow", bd= 0, fg= "black",
                                                      highlightthickness= 0, show= '*')
        self.existing_user_window_password.place(x=350, y=540)

        self.existing_user_window_login = tkinter.Button(self.existing_user_window, text="Login", width=15, font=('arial', 35, 'bold'),
                                       bd=0, highlightthickness=0, height=1, command= self.user_login)
        self.existing_user_window_login.place(x=335, y=680)

        self.bg_canvas_existing_user.place(x=0, y=0)

    def user_login(self):

        username = self.existing_user_window_username.get()
        password = self.existing_user_window_password.get()

        self.username = username

        with open('data.json', 'r') as file:
            data = json.load(file)

        # check if the user exist in the database.
        is_username_register = username in data

        # check if the password match.
        if is_username_register:
            if data[username]["account_info"]["password"] == password:
                is_password_match = True
            else:
                is_password_match = False

            self.userdata = data[username]
            print(self.userdata)

            # destroy existing_user_window_username and create new window.
            self.existing_user_window.destroy()

            # create a new window for user.
            self.user = tkinter.Toplevel()
            self.user.title(f'Welcome {username}')
            self.user.geometry('1000x1000')
            self.user.config(bg="slate blue")

            # welcome message for user.
            welcome_message = tkinter.Label(self.user, text= f"Welcome {username}", background= "slate blue",
                                            font= ('arial', 30, 'bold'), foreground= "snow")
            welcome_message.place(x= 350, y=50)

            today_workout = tkinter.Label(self.user, text=f"Please write your workout for today?", background="slate blue",
                                            font=('arial', 20, 'bold'), foreground="black")
            today_workout.place(x=300, y=150)

            self.exercise_var = StringVar()
            # Section to add today exercise.
            self.exercise = tkinter.Entry(self.user, textvariable=self.exercise_var, font=('arial', 25, 'bold'),
                                          highlightthickness= 0, width= 50)
            self.exercise.place(x= 150, y=200, height= 250)

            # get calories button.
            calories_button = tkinter.Button(self.user, text= "Calculate Calories", font= ('arial', 30, 'bold'),
                                             command= self.get_calories)
            calories_button.place(x=350, y=500)

    def get_calories(self):

        username = str(self.username)
        weight_kg = self.userdata['personal_info']['weight_kg']
        height_cm = self.userdata['personal_info']['height_cm']
        age = self.userdata['personal_info']['age']

        query = self.exercise.get()
        response = self.calories.get_calories(query = query, username=username, weight_kg=weight_kg, height_cm=height_cm, age=age)
        print(response)

    def launch_new_user(self):

        self.new_user_window = tkinter.Toplevel()
        self.new_user_window.title('Create New Account')
        self.new_user_window.geometry('1000x1000')
        self.new_user_window.config(bg= "slate blue")

        self.welcome_message = tkinter.Label(self.new_user_window,text="Welcome to Calories Tracker",
                                             font=('arial', 25, 'bold'), bg="slate blue")
        self.welcome_message.place(x=350, y=150)

        self.new_user_window_username = tkinter.Label(self.new_user_window,text="username:",
                                             font=('arial', 25, 'bold'), bg="slate blue")
        self.new_user_window_username.place(x=250, y=250)

        self.new_user_window_password = tkinter.Label(self.new_user_window, text="password:",
                                                      font=('arial', 25, 'bold'), bg="slate blue")
        self.new_user_window_password.place(x=250, y=300)

        self.new_user_window_email = tkinter.Label(self.new_user_window, text="email:",
                                                      font=('arial', 25, 'bold'), bg="slate blue")
        self.new_user_window_email.place(x=250, y=350)

        self.new_user_window_weight = tkinter.Label(self.new_user_window, text="weight:",
                                                   font=('arial', 25, 'bold'), bg="slate blue")
        self.new_user_window_weight.place(x=250, y=400)

        self.new_user_window_height = tkinter.Label(self.new_user_window, text="height:",
                                                    font=('arial', 25, 'bold'), bg="slate blue")
        self.new_user_window_height.place(x=250, y=450)

        self.new_user_window_age = tkinter.Label(self.new_user_window, text="age:",
                                                    font=('arial', 25, 'bold'), bg="slate blue")
        self.new_user_window_age.place(x=250, y=500)

        self.new_user_window_phone_number = tkinter.Label(self.new_user_window, text="Phone:",
                                                 font=('arial', 25, 'bold'), bg="slate blue")
        self.new_user_window_phone_number.place(x=250, y=550)

        # username input area
        self.username_var = tkinter.StringVar()
        self.password_var = tkinter.StringVar()
        self.email = tkinter.StringVar()
        self.weight = tkinter.StringVar()
        self.height = tkinter.StringVar()
        self.age = tkinter.StringVar()
        self.phone_number = tkinter.StringVar()

        self.new_user_window_username_text = tkinter.Entry(self.new_user_window, textvariable=self.username_var,
                                                           font=('arial', 25, 'bold'), bg="snow", bd=0, fg="black",
                                                           highlightthickness=0)
        self.new_user_window_username_text.place(x=400, y=255)

        self.new_user_window_password_text = tkinter.Entry(self.new_user_window, textvariable=self.password_var,
                                                           font=('arial', 25, 'bold'), bg="snow", bd=0, fg="black",
                                                           highlightthickness=0, show= '*')
        self.new_user_window_password_text.place(x=400, y=305)

        self.new_user_window_email_text = tkinter.Entry(self.new_user_window, textvariable=self.email,
                                                           font=('arial', 25, 'bold'), bg="snow", bd=0, fg="black",
                                                           highlightthickness=0)
        self.new_user_window_email_text.place(x=400, y=355)

        self.new_user_window_weight_text = tkinter.Entry(self.new_user_window, textvariable=self.weight,
                                                        font=('arial', 25, 'bold'), bg="snow", bd=0, fg="black",
                                                        highlightthickness=0)
        self.new_user_window_weight_text.place(x=400, y=405)

        self.new_user_window_height_text = tkinter.Entry(self.new_user_window, textvariable=self.height,
                                                         font=('arial', 25, 'bold'), bg="snow", bd=0, fg="black",
                                                         highlightthickness=0)
        self.new_user_window_height_text.place(x=400, y=455)

        self.new_user_window_age_text = tkinter.Entry(self.new_user_window, textvariable=self.age,
                                                         font=('arial', 25, 'bold'), bg="snow", bd=0, fg="black",
                                                         highlightthickness=0)
        self.new_user_window_age_text.place(x=400, y=505)

        self.new_user_window_phone_text = tkinter.Entry(self.new_user_window, textvariable=self.phone_number,
                                                      font=('arial', 25, 'bold'), bg="snow", bd=0, fg="black",
                                                      highlightthickness=0)
        self.new_user_window_phone_text.place(x=400, y=555)

        # SUBMIT BUTTON.
        self.new_user_window_submit = tkinter.Button(self.new_user_window, text="Submit", width=15,
                                                         font=('arial', 25, 'bold'),
                                                         bd=0, highlightthickness=0, height=1, command= self.register_new_user)
        self.new_user_window_submit.place(x=400, y=680)

    def register_new_user(self):
        username = self.new_user_window_username_text.get()
        password= self.new_user_window_password_text.get()
        email = self.new_user_window_email_text.get()
        weight = self.new_user_window_weight_text.get()
        height = self.new_user_window_height_text.get()
        age = self.new_user_window_age_text.get()
        phone_number = self.new_user_window_phone_text.get()

        response = self.calories.register_user(user=username, password=password, email=email, weight_kg= float(weight),
                                               height_cm= float(height), age= int(age), phone_number= int(phone_number))


        if response is None:
            self.new_user_window.destroy()

ui = UserInterface()
ui.exit_window()
