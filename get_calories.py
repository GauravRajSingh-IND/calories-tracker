import os
import json
import requests

from pixela import Pixela

END_POINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
APP_ID = "f8d3f5c1"
APP_KEY = "85e412a2ab3d7e88440bb01fc8b73ab7"


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

        # store user information in a json file for further use.
        if self.is_user_account_created:
            user_data = {
                        "account_info": {
                            "password": self.password,
                            "email": self.email,
                            "phone": self.phone_number
                                        },
                        "personal_info":{
                            "weight_kg": self.weight_kg,
                            "height_cm": self.height_cm,
                            "age": self.age
                                        },
                        "other_info":   {}
                        }

            # read existing json file.
            with open("data.json") as json_data:
                json_data = json.load(json_data)

            # append the new user data to json data
            json_data[self.username] = user_data

            # write the json data to json file.
            with open("data.json", "w") as file:
                json.dump(json_data, file)

        else:
            raise "User not register, Please try again"


    def get_calories(self, query:str, username:str, weight_kg:float, height_cm:float, age:int):
        """
        This function calculate the calories burned.
        :param query: name of the exercise.
        :param age: age of the user
        :param height_cm: height of the user
        :param weight_kg: weight of the user
        :param username: username.
        :return: dict object response.
        """

        # check if all the required parameters.
        if not all([query, username, weight_kg, height_cm, age]):
            raise "required parameters missing please try again."

        self.username = username

        headers = {
            'x-app-id': APP_ID,
            'x-app-key': APP_KEY
        }

        params = {
            'query':query,
            'weight_kg':weight_kg,
            'height_cm':height_cm,
            'age':age
        }

        try:
            response = requests.post(url=END_POINT, json=params, headers=headers)
            response.raise_for_status()

            # add the response to calories json file.
            with open("calories.json", "r") as json_data:
                data = json.load(json_data)

            # check if the username exist or not.
            is_user_exist = data.get(self.username)

            # if user don't exist.
            if is_user_exist is None:
                data[self.username] = {0:response.text}

            # if user exist.
            elif is_user_exist is not None:

                # find the last key number.
                next_key = int(list(data[self.username].keys())[-1]) + 1
                data[self.username][next_key] = response.text

            # dump json file.
            with open('calories.json', 'w') as file:
                json.dump(data, file)

            return response.text

        except requests.RequestException as e:
            return {'exercise': False}














