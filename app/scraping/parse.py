import requests
from bs4 import BeautifulSoup, Tag
from urllib.parse import urljoin

from app.config import to_find

BASE_URL = "https://djinni.co/jobs/"
PYTHON_DEVELOPER = "?all-keywords=&any-of-keywords=&exclude-keywords=&primary_keyword=Python"
PAGE = urljoin(BASE_URL, PYTHON_DEVELOPER)


def parse_single_vacancy(description: [Tag]) -> None:
    for i in description:
        for j in i:
            j = str(j).replace("<br/>", "").split()
            for element in j:
                element.replace("(", "").replace(")", "")
                if element in to_find:
                    to_find[element] += 1


def get_next_page(page_soup: BeautifulSoup) -> [str, None]:
    next_page = page_soup.select(".d-md-none > a[href]")
    try:
        python_developer = next_page[0]["href"]
    except IndexError:
        return
    return urljoin(BASE_URL, python_developer)


def get_page_info() -> dict:
    page = requests.get(PAGE).content
    soup = BeautifulSoup(page, "html.parser")
    next_page = get_next_page(soup)
    description = soup.select(".text-card")
    parse_single_vacancy(description)

    # while next_page:
    #     description = soup.select(".text-card")
    #     parse_single_vacancy(description)
    #     page = requests.get(urljoin(PAGE, next_page)).content
    #     soup = BeautifulSoup(page, "html.parser")
    #     next_page = get_next_page(soup)

    return to_find


if __name__ == '__main__':
    get_page_info()
