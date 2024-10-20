def compare_test_results(expected, actual):
   return [exp == act for exp, act in zip(expected, actual)]