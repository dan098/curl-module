import requests

url = input("insert link")

response = requests.get(url)
html_content = response.text

with open("page.html", "w", encoding="utf-8") as file:
    file.write(html_content)
