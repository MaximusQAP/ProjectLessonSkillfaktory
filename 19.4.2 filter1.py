phone_numbers = ['123-456-7890', '123.456.7890', '(123) 456-7890', '+1234567890', '1234567890']

def format_phone_number(number):
   return ''.join(filter(str.isdigit, number))

formatted_numbers = list(map(format_phone_number, phone_numbers))