def has_failures(test_results):
   return any(result == "fail" for result in test_results)

def all_passed_or_skipped(test_results):
   return all(result in ["pass", "skip"] for result in test_results)