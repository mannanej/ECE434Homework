# import requests
# from bs4 import BeautifulSoup

# BASE_URL = 'https://news.ycombinator.com'
# USERNAME = "mannanej"
# PASSWORD = "P!glet6386"

# s = requests.Session()

# data = {"goto": "news", "acct": USERNAME, "pw": PASSWORD}
# r = s.post(f'{BASE_URL}/login', data=data)

# soup = BeautifulSoup(r.text, 'html.parser')
# if soup.find(id='logout') is not None:
# 	print('Successfully logged in')
# else:
# 	print('Authentication Error')
# url = 'https://uam1.dexcom.com/identity/login?signin=c0a3aa23e3b82c441c3b1d9a6185fb17'
# from requests import Session
# from bs4 import BeautifulSoup as bs
# with Session() as s:
#     site = s.get("http://quotes.toscrape.com/login")
#     bs_content = bs(site.content, "html.parser")
#     token = bs_content.find("input", {"name":"csrf_token"})["value"]
#     login_data = {"username":"admin","password":"12345", "csrf_token":token}
#     s.post("http://quotes.toscrape.com/login",login_data)
#     home_page = s.get("http://quotes.toscrape.com")
#     print(home_page.content)

from requests import Session
from bs4 import BeautifulSoup as bs
with Session() as s:
    site = s.get("https://uam1.dexcom.com/identity/login?signin=c0a3aa23e3b82c441c3b1d9a6185fb17")
    bs_content = bs(site.content, "html.parser")
    # token = bs_content.find("input", {"name":"csrf_token"})["value"]
    login_data = {"username":"eddiemannan@gmail.com","password":"P!glet6386"}
    click_data = {"ember79"}
    s.post("https://uam1.dexcom.com/identity/login?signin=c0a3aa23e3b82c441c3b1d9a6185fb17",login_data)
    home_page = s.get("https://clarity.dexcom.com/#/overview")
    s.post("https://clarity.dexcom.com/#/overview", click_data)
    print(home_page.content)