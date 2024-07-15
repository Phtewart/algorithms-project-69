import re

def search(docs, text):
    out = []
    term = re.findall(r'\w+', text)

    for sub_text in docs:
        for word in term:
            if sub_text['text'].find(str(word)) != -1:
                out.append(sub_text['id'])

    return out

