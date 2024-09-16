import os
import requests

from pixela import Pixela

END_POINT = "https://trackapi.nutritionix.com/v2/natural/exercise"


class Calories:

    def __init__(self):

        self.username = None
        self.password = None
        self.email = None
        self.phone_number = None
        self.weight_kg = None
        self.height_cm = None
        self.age = None

        # create pixela object.
        self.Pixela = Pixela()
        self.is_user_account_created = None

    def register_user(self, user:str, password:str, email:str, weight_kg:float, height_cm:float, age:int,
                      phone_number:int ):
        """
        This function register/ create a user account on the application as well as pixela.
        :param phone_number: 10 digits number of the user.
        :param user:  username which will be used while login
        :param password: password of the user
        :param email: a valid email id.
        :param weight_kg: weight in kilograms
        :param height_cm: height in centimeters
        :param age: age of the user, should be in int format.
        :return: dict of the response
        """

        if not all([user, password, email, phone_number, weight_kg, height_cm, age, phone_number]):
            raise "Please enter all the required parameters and try again"

        # assign parameters
        self.username = user
        self.password = password
        self.email = email
        self.weight_kg = weight_kg
        self.height_cm = height_cm
        self.age = age
        self.phone_number = phone_number

        # check if pixela username is already taken.
        response_pixela_user = requests.get(url=f"https://pixe.la/@{self.username}").status_code
        if response_pixela_user == 404:
            is_valid_pixela = True

        else:
            is_valid_pixela = False
            raise "username already taken, Please try again with different username."

        # create a user  account in pixela using Pixela object
        response = self.Pixela.User().create_new_user(token=self.password, username= self.username)
        self.is_user_account_created = response['response']['isSuccess']

        # create store user information in a json file for further use.






client = Calories()
client.register_user("jobner171294", "testtesttest", "test", 12.5, 12, 12, 1213123)








