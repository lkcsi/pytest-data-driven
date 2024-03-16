import yaml


def load_data_yml(filename, params: tuple[str]):
    with open(f"test_data/{filename}.yml", "r") as file:
        data: dict = yaml.safe_load(file)
        test_cases = list(data.keys())
        return (
            ",".join(params),
            [tuple(data[tc][p] for p in params) for tc in test_cases],
            test_cases,
        )
