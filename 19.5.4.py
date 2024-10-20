def aggregate_data(*args, **kwargs):
   total_num = sum(arg for arg in args if type(arg) in [int, float])
   total_num += sum(value for value in kwargs.values() if type(value) in [int, float])
   total_str = sum(1 for arg in args if type(arg) == str)
   total_str += sum(1 for value in kwargs.values() if type(value) == str)
   return total_num, total_str