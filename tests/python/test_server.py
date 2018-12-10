from bs4 import BeautifulSoup
import requests

from demo_payment.options import options


# Index test alive
def test_alive():
    response = requests.get("http://" + options.demo_payment_website_url)
    assert response.status_code == 200


# Index test title
def test_html_title():
    response = requests.get("http://" + options.demo_payment_website_url)
    soup = BeautifulSoup(response.content, "html.parser")
    assert soup.title.text == "Home"
