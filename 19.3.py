from random import random


def generate_user_data(count, first_names, last_names, age_diapason):
   for _ in range(count):
       name = random.choice(first_names)
       surname = random.choice(last_names)
       age = random.randint(age_diapason[0], age_diapason[1])
       yield name, surname, age