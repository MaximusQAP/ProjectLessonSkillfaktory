def check_data_format(**kwargs):
   for key, value in kwargs.items():
       if type(key) != str or not (type(value) == int or type(value) == float):
           return False
   return True