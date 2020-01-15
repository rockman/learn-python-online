
def test_import_from_some_directory():
    try:
        import utils
    except:
        assert True
    else:
        assert False

def test_import_from_some_directory_after_modifying_sys_path():
    import sys
    sys.path.append('some_directory')
    import utils
