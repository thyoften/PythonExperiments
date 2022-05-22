import datetime

WEDNESDAY = 2

def only_on_weekday(day):
    def wrapper(func):
        if datetime.date.today().weekday() == day:
            return func # replace it with func() to auto call
        else:
            print('Today''s not the day!')
            def empty():  # if not present an exception is thrown (NoneType is not callable)
                pass
            return empty

    return wrapper

@only_on_weekday(WEDNESDAY)
def test():
    print('IT IS WEDNESDAY MY DUDES')

test()
