import random

def generate_test_data(n=5, min_value=1, max_value=10):
   return [random.randint(min_value, max_value) for _ in range(n)]