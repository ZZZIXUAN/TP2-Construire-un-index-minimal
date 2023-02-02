import json
import requests
import nltk


def index(start, end):  # load the list of URLs in JSON format
    nltk.download('punkt')
    from lxml import etree
    with open(r'crawled_urls.json', 'r') as file:
        urls = json.load(file)
    print(urls)

    index_list = []
    for url in urls[start:end]:
        print(url)
        try:
            res = requests.get(url, timeout=10).text
            text = etree.HTML(res).xpath('//text()')
            text = ''.join([i.strip() for i in text if i.strip() != ''])
            index_list.append({'text': text})
        except (Exception,):
            pass

    titles = [ind['text'] for ind in index_list]  # extract the titles from the URLs
    print(titles)

    from nltk.tokenize import word_tokenize  # tokenize the word
    titles_tokenized = [word_tokenize(title) for title in titles]

    vocabulary = set()  # build a vocabulary of unique tokens
    for title in titles_tokenized:
        for token in title:
            vocabulary.add(token)

    documents = {}  # create a dictionary of document IDs and tokens
    for i, title in enumerate(titles_tokenized):
        documents[i] = title

    index_web = {}  # build the web index
    for term in vocabulary:
        postings = []
        for doc_id, doc_tokens in documents.items():
            if term in doc_tokens:
                postings.append(doc_id)
        index_web[term] = postings

    num_documents = len(documents)  # get some statistics on the documents
    num_tokens = sum([len(doc) for doc in documents.values()])
    average_tokens_per_document = num_tokens / num_documents

    with open('title.non_pos_index.json', 'w') as index_file:  # write the index and metadata to file
        json.dump(index_web, index_file)

    metadata = {
        'num_documents': num_documents,
        'num_tokens': num_tokens,
        'average_tokens_per_document': average_tokens_per_document
    }

    with open('metadata.json', 'w') as metadata_file:
        json.dump(metadata, metadata_file)

    print("Index and metadata saved successfully!")
