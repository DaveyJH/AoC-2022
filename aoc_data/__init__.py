import inspect
import requests
import re
import os
from dotenv import load_dotenv

load_dotenv()

SESSION = os.environ["session"]
URL = "https://adventofcode.com/2022/day/{}/input"
FILE_REGEX = re.compile(r"(\d+)\.py$")


def today_url(call):
    return URL.format(FILE_REGEX.search(call).group(1))


def retrieve_data(day_url):
    response = requests.get(
        url=day_url,
        cookies={"session": SESSION},
        headers={'Accept-Encoding': 'gzip'}
    )
    if response.ok:
        return response.text
    raise Exception("Error with data retrieval : check file name is accurate.")


def check_for_data():
    calling_filename = inspect.stack()[1].filename
    file = f"aoc_data/day_{FILE_REGEX.search(calling_filename).group(1)}.txt"
    if not os.path.exists(file):
        content = retrieve_data(today_url(calling_filename))
        f = open(file, "w")
        f.write(content)
        f.close()
