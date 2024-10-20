def create_unique_checker():
    seen = set()

    def checker(value):
        if value in seen:
            return False
        else:
            seen.add(value)
            return True

    return checker