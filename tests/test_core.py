def test_import_package():
    import importlib
    pkg = importlib.import_module('linear_regression')
    assert pkg is not None
