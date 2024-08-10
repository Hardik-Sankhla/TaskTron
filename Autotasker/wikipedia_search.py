import wikipedia as wiki

def search_wikipedia(query):
    return wiki.search(query)

def suggest_wikipedia(query):
    return wiki.suggest(query)

def summary_wikipedia(query, lang='en'):
    wiki.set_lang(lang)
    return wiki.summary(query)

def get_page_details(query):
    page = wiki.page(query)
    return {
        "title": page.title,
        "url": page.url,
        "content": page.content,
        "images": page.images,
        "links": page.links
    }
