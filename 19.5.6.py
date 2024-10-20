def process_test_data(*args, **kwargs):
   args_str = ', '.join(str(arg) for arg in args)
   kwargs_str = ', '.join(f'{k}={v}' for k, v in kwargs.items())
   return ', '.join([args_str, kwargs_str])