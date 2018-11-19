from bs4 import BeautifulSoup
import requests


# Index test alive
def test_alive():
    response = requests.get("http://127.0.0.1:8080/")
    assert response.status_code == 200


# Index test title
def test_html_title():
    response = requests.get("http://127.0.0.1:8080/")
    soup = BeautifulSoup(response.content, "html.parser")
    assert soup.title.text == "Home"
