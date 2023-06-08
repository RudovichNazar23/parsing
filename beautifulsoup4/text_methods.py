from bs4 import BeautifulSoup

html_doc = """
<html>
    <body>
        <div id="main">
            <p>This is a paragraph</p>
        </div>
        <ul>
            <li>Item 1</li>
            <li>Item 2</li>
            <li>Item 3</li>
        </ul>
    </body>
</html>
"""


soup = BeautifulSoup(html_doc, "html.parser")

p_elem = soup.find("ul")
# print(*map(lambda x: x.get_text(), p_elem))

all_text = soup.get_text()
print(all_text)
