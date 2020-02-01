import argparse

PROVIDER_KEY_NAME = 'GOOGLE_API_KEY'


class Config:
    options: argparse.ArgumentParser

    def __init__(self):
        parser = argparse.ArgumentParser("make run")
        parser.add_argument("--algorithm", required=False, help="Use kdtree algorithm")
        parser.add_argument("--debug", required=False, help="Use debug features")
        parser.add_argument(
            "--remote",
            required=False,
            help="Use Google Routes provider to calculate distances, please set env var {}"
            .format(PROVIDER_KEY_NAME))
        self.options = parser.parse_args()

    def start(self):
        return self.options


config = Config()
