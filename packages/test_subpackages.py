
from foo import *
from foo.alpha import *


def test_package_publics():
    assert FOO_PUBLIC == 'FOO_PUBLIC'
    assert ALPHA_PUBLIC == 'ALPHA_PUBLIC'


def test_package_privates():
    try:
        assert _FOO_PRIVATE == '_FOO_PRIVATE'
    except:
        assert True
    else:
        assert False


def test_exposed_package_private():
    assert _ALPHA_PRIVATE == '_ALPHA_PRIVATE'


def test_other():
    from foo.alpha.other import the_other
    name, solar, common = the_other()
    assert name == 'OTHER'
    assert solar == 'SOLAR_PUBLIC'
    assert common == 'COMMON_PUBLIC'
