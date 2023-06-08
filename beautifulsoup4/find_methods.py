from bs4 import BeautifulSoup

# find method

html_doc = """
    <html>
        <head>
            <title>Example Page</title>
        </head>
        <body>
            <div id="main">
                <h1>Hello World</h1>
                <p class="info">This is a paragraph.</p>
                <p class="info">This is another paragraph.</p>
                <ul>
                    <li>Item 1</li>
                    <li>Item 2</li>
                    <li>Item 3</li>
                </ul>
            </div>
            <div id="secondary">
                <p>Some additional information.</p>
                <p>Some additional information.1</p>
                <p>Some additional information.2</p>
                <p>Some additional information.3</p>
                <p>Some additional information.4</p>
            </div>
        </body>
    </html>   

"""

# soup = BeautifulSoup(html_doc, "html.parser")
#
# div_tag = soup.find("div", {"id": "main"})
#
# h_tag = div_tag.find("h1")
#
# p_tag = div_tag.find("p", {"class": "info"})
#
# ul_tag = div_tag.find("ul", {"id": ""})
# print(div_tag)
# print()
# print(h_tag)
# print()
# print(ul_tag)
# print()
# print(p_tag)


# end find_method


# find_all method

html = """
    <html>
        <body>
            <h1>Заголовок 1</h1>
            <p class="text-class">Текст 1</p>
            <p class="text-class">Текст 2</p>
            <p id="text-id">Текст 3</p>
            <a href="https://google.com">Google</a>
            <a href="https://yandex.ru">Yandex</a>
        </body>
    </html>
"""


# soup = BeautifulSoup(html, "html.parser")
#
# p_tags = soup.find_all("p", attrs={"id": "text-id"})
# # print(*map(lambda x: x.text, p_tags), sep="\n")
#
# a_tags = soup.find_all("a")
#
# print(*map(lambda x: (x.text, x["href"]), a_tags), sep="\n")


soup = BeautifulSoup(html_doc, "html.parser")

all_p_tags = soup.find_all("p", recursive=True, attrs={
    "class": "text-class"
})
print(*map(lambda x: x.text, all_p_tags), sep="\n")
