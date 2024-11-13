import os
from langchain_ollama import OllamaEmbeddings
from langchain_pinecone import PineconeVectorStore
import pinecone
from indexing import stored_data

def embeding():
    embed = OllamaEmbeddings(
        model="llama3"
    )
    return embed

def query_pinecone(query):
    os.environ['PINECONE_API_KEY'] = '5e000385-2e76-4a2a-a9a7-2166c1e77885'
    #pinecone.init(api_key=os.getenv('PINECONE_API_KEY'))

    index_name = "princessdisney"
    embed = embeding()
    embedding_vector = embed.embed_query(query)
    store = stored_data()
    docs = store.similarity_search_by_vector(embedding_vector)
    return docs

def main():
    query = "elsa"
    docs = query_pinecone(query)
    if docs:
        print(docs[0].page_content)
    else:
        print("No matching documents found.")

if __name__ == "__main__":
    main()
