import json
import markdownify

def get_template():
    with open('template.html', 'r') as template:
        t = template.read()
    return t

def replace_content(doc_title, doc_question, doc_answer):
    template = get_template()
    template = template.replace('doc_title', doc_title)
    template = template.replace('doc_question', doc_question)
    template = template.replace('doc_answer', doc_answer)
    return template

def create_file(filename, content):
    name = filename + '.html'
    f = open(name, 'w+', encoding='utf-8')
    f.write(content)
    f.close()

def create_file_md(filename, content):
    name = filename + '.md'
    f = open(name, 'w+', encoding='utf-8')
    f.write(markdownify.markdownify(content, heading_style="ATX"))
    f.close()


# create_file('123', 'test content')

f = open('FaqArticles.json', 'r', encoding='utf-8')
data = json.load(f)
f.close()

for article in data:
    content = replace_content(doc_title=article['articleTitle'], doc_question=article['articleQuestion'], doc_answer=article['articleAnswer'])
    create_file_md(filename=article['alias'], content=content)
    #print(content)



    # alias
