import inspect
import requests
import re
import os
from dotenv import load_dotenv

load_dotenv()

FILE_REGEX = re.compile(r"(\d+)\.py$")


def data_file():
    """Provides data file path for day specified in filename"""
    DATA_FILE = "aoc_data/day_{}.txt"
    return DATA_FILE.format(
        FILE_REGEX.search(inspect.stack()[1].filename).group(1)
    )


def today_url(call):
    """Provides input data URL for day specified in filename"""
    URL = "https://adventofcode.com/2022/day/{}/input"
    return URL.format(FILE_REGEX.search(call).group(1))


def retrieve_data(day_url):
    """Retrieves data from AoC"""
    SESSION = os.environ["session"]
    response = requests.get(
        url=day_url,
        cookies={"session": SESSION},
        headers={'Accept-Encoding': 'gzip'}
    )
    if response.ok:
        return response.text
    raise Exception("Error with data retrieval : check file name is accurate.")


def check_for_data():
    """Creates input data file for day if it does not already exists"""
    calling_filename = inspect.stack()[1].filename
    file = f"aoc_data/day_{FILE_REGEX.search(calling_filename).group(1)}.txt"
    if not os.path.exists(file):
        content = retrieve_data(today_url(calling_filename))
        f = open(file, "w")
        f.write(content)
        f.close()
