import argparse

PROVIDER_KEY_NAME = 'GOOGLE_API_KEY'

config = None


class Config:
    options: argparse.ArgumentParser

    def __init__(self):
        parser = argparse.ArgumentParser("make run")
        parser.add_argument("--algorithm", required=False, help="Use kdtree algorithm")
        parser.add_argument("--cargos-csv", required=False, help="The cargos CSV file path")
        parser.add_argument("--debug", required=False, help="Use debug features")
        parser.add_argument("--max-cargos", required=False, help="Max cargos per truck, default 1")
        parser.add_argument(
            "--remote",
            required=False,
            help="Use Google Routes provider to calculate distances, please set env var {}"
            .format(PROVIDER_KEY_NAME))
        parser.add_argument("--trucks-csv", required=False, help="The trucks CSV file path")
        self.options = parser.parse_args()

    def start(self):
        config = Config()
        return config


config = Config()
