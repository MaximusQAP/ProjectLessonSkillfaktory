def filter_api_tests(test_cases):
   return list(filter(lambda test_case: test_case["type"] == "API", test_cases))