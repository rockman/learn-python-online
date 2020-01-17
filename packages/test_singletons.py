
import sys
sys.path.append('modules_are_singletons')

def test_modules_are_singletons():
    import alpha
    import beta
    import data
    assert 2 == len(data.get_items())
    assert 'alpha' in data.get_items()
    assert 'beta' in data.get_items()

