import requests
import bs4

def get_page(url: str) -> str:
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 OPR/91.0.4516.36"
    }
    response = requests.get(url=url, headers=headers)
    return response.text

def get_url(text, from_lang="english", to_lang="ukrainian"):
    url_text = "+".join(text.split())
    return f'https://context.reverso.net/translation/{from_lang}-{to_lang}/{url_text}'

def get_translation(html_content: str) -> list:
    soup = bs4.BeautifulSoup(html_content, "html.parser")
    translations = soup.select('#translations-content .display-term')
    return [term.text.strip() for term in translations]

if __name__ == "__main__":
    url = get_url("hands-on")
    html_content = get_page(url)
    print(get_translation(html_content))
