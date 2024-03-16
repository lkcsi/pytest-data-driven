import yaml


def load_data_yml(filename, params: tuple[str]):
    with open(f"{filename}.yml", "r") as file:
        data: dict = yaml.safe_load(file)
        test_cases = list(data.keys())
        return (
            ",".join(params),
            [tuple(data[tc][p] for p in params) for tc in test_cases],
            test_cases,
        )


def pytest_generate_tests(metafunc):
    if any(marker.name == "data_driven" for marker in metafunc.definition.own_markers):
        a, b, c = load_data_yml(metafunc.definition.name, metafunc.fixturenames)
        metafunc.parametrize(a, b, ids=c)
