

class Doubler:

    def __call__(self, value):
        return 2 * value


def multiplier(first, *rest):
    result = first
    for value in rest:
        result *= value
    return result


def arguments(a, b, *args, x, y, **kwargs):
    return (a + b,
            len(args),
            x - y,
            ', '.join(f'{k}={v}' for k, v in kwargs.items())
           )


def transpose(matrix):
    return tuple(zip(*matrix))


def foo(alpha, beta, *others):
    return alpha.upper(), -beta, tuple(reversed(others))


def forwarder(f, *args, **kwargs):
    return f(*args, **kwargs)


def test_callable_instance():
    doubler = Doubler()

    assert doubler(2) == 4


def test_callables():
    assert callable(Doubler)
    assert callable(Doubler())
    assert callable(list.append)
    assert callable(lambda x: x)
    assert not callable(42)
    assert not callable("hello")


def test_multiple_arguments():
    assert multiplier(2, 3, 4) == 24
    assert multiplier(3, 4) == 12
    assert multiplier(4) == 4

    try:
        multiplier()
    except:
        assert True


def test_arguments():
    a, b, c, d = arguments(1, 2, 3, 4, y=5, x=6, foo=42, bar='hello')

    assert a == 3
    assert b == 2
    assert c == 1
    assert d == 'foo=42, bar=hello'


def test_transpose():
    m = ((1, 2, 3), (4, 5, 6))
    assert transpose(m) == ((1, 4), (2, 5), (3, 6))


def test_extended_call_syntax():
    args = ('hello', 42, 'x', Doubler, -1)
    x, y, z = foo(*args)

    assert x == 'HELLO'
    assert y == -42
    assert z == (-1, Doubler, 'x')


def test_forwarding_arguments():
    a, b, c, d = forwarder(arguments, 1, 2, 3, 4, y=5, x=6, foo=42, bar='hello')

    assert a == 3
    assert b == 2
    assert c == 1
    assert d == 'foo=42, bar=hello'

