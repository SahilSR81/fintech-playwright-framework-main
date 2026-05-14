import configparser
import os

config = configparser.ConfigParser()

config_path = os.path.join(
    os.path.dirname(os.path.dirname(__file__)),
    "config",
    "config.ini"
)

config.read(config_path)


class ConfigReader:

    @staticmethod
    def get_base_url():
        return config.get("COMMON", "base_url")

    @staticmethod
    def get_browser():
        return config.get("COMMON", "browser")

    @staticmethod
    def get_timeout():
        return config.getint("COMMON", "timeout")

    @staticmethod
    def get_headless():
        return config.getboolean("COMMON", "headless")

    @staticmethod
    def get_page_load_timeout():
        return config.getint(
            "COMMON",
            "page_load_timeout"
        )