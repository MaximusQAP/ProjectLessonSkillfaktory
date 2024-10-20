tests_run = 0
tests_failed = 0

def test_case_generator():
    case_id = 0

    def run_test(test):
        nonlocal case_id
        global tests_run
        global tests_failed
        tests_run += 1
        if not test():
            tests_failed += 1
        case_id += 1
        return case_id

    return run_test