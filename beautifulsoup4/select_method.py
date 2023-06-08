from bs4 import BeautifulSoup


html = """
<html>
    <body>
        <h1>Заголовок 1</h1>
        <p class="text-class">Текст 1</p>
        <p class="text-class">Текст 2</p>
        <p id="text-id">Текст 3</p>
    </body>
</html>
"""

soup = BeautifulSoup(html, "html.parser")

print(*map(lambda x: x.text, soup.select("p.text-class")), sep="\n")
print(*map(lambda x: x.text, soup.select("body p")), sep="\n")



