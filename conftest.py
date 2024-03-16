from utils import load_data_yml


def pytest_generate_tests(metafunc):
    if any(marker.name == "data_driven" for marker in metafunc.definition.own_markers):
        a, b, c = load_data_yml(metafunc.definition.name, metafunc.fixturenames)
        metafunc.parametrize(a, b, ids=c)
