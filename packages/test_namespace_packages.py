
import sys


def test_namespace_packages():
    sys.path.extend([
        'namespace_packages/folder_a',
        'namespace_packages/folder_b'])
    from some_project import alpha
    from some_project import beta
    assert 'alpha' == alpha.run()
    assert 'beta' == beta.run()
