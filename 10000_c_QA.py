import requests
from bs4 import BeautifulSoup

stack_url = "https://stackoverflow.com/q/"

for x in range(1, 201):
    res = requests.get(f'https://stackoverflow.com/questions/tagged/c%20-c%2b%2b%20-curses?tab=votes&page={x}&pagesize=50')

    soup = BeautifulSoup(res.text, "html.parser")

    questions = soup.select(".question-summary")

    print("-" * 80, end="\n")
    print({x}, end="\n")
    print("-" * 80, end="\n")

    for que in questions:
        q_txt = que.select_one('.question-hyperlink').getText()
        q_id = que.get('id').split("-")[-1]

        print(q_txt)
        print(f'{stack_url}{q_id}')
        print("stat:")
        print("tags: ", end="")

        tags = que.select_one(".tags")

        for t in tags.find_all('a'):
            t = t.getText()
            print(t, end=", ")

        print(end="\n")
        print("-\n",)


