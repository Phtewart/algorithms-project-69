def search(docs, text):
    out = []

    for sub_text in docs:
        if sub_text['text'].find(text) != -1:
            out.append(sub_text['id'])
    return out