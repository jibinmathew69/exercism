def add_gigasecond(birth_date):
    import datetime
    return birth_date+datetime.timedelta(seconds=(10**9))