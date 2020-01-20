
import functools


def double_decorator(f):
    def wrapper(value):
        return 2 * f(value)
    return wrapper


@double_decorator
def increment(value):
    return value + 1


def string_wrapper(f):
    def wrapper(*args, **kwargs):
        return '[' + f(*args, **kwargs) + ']'
    return wrapper


@string_wrapper
def hello(someone, *others, **titled_others):
    parts = [someone] + list(others) + [f'{title}={other}' for title, other in titled_others.items()]
    return 'hello: ' + ', '.join(parts)


class ClassDecorator:

    def __init__(self, f):
        self.f = f
        self.count = 0

    def __call__(self, text):
        self.count += 1
        return f'{self.count}: {self.f(text)}'


@ClassDecorator
def upper(text):
    return text.upper()


class InstanceDecorator:

    def __init__(self, adjustment):
        self.adjustment = adjustment

    def __call__(self, f):
        def wrap(value):
            return f(value) + self.adjustment
        return wrap


@InstanceDecorator(-1)
def doubler(value):
    return value * 2


class ToggleDecorator:

    def __init__(self, toggle=True):
        self.toggle = toggle

    def __call__(self, f):
        def wrap(value):
            x = f(value)
            return -x if self.toggle else x
        return wrap


def nothing_decorator(f):
    @functools.wraps(f)
    def wrapper():
        return f()
    return wrapper


@nothing_decorator
def keep_my_name_please():
    return True


def test_decorator():
    assert increment(1) == 4
    
    s = hello('alice', 'gary', 'bob', mr='anderson', miss='heart')
    assert s == '[hello: alice, gary, bob, mr=anderson, miss=heart]'

    assert upper('hello') == '1: HELLO'
    assert upper('mr') == '2: MR'
    assert upper('anderson') == '3: ANDERSON'

    assert doubler(2) == 3


def test_toggle_decorator():
    toggle = ToggleDecorator()

    @toggle
    def plus_three(value):
        return value + 3

    assert plus_three(2) == -5

    toggle.toggle = False

    assert plus_three(2) == 5


def test_multiple_decorators():

    @double_decorator
    @InstanceDecorator(1)
    def identity(value):
        return value

    assert identity(2) == 6


def test_functools_wraps():
    assert increment.__name__ != 'increment'
    assert keep_my_name_please.__name__ == 'keep_my_name_please'