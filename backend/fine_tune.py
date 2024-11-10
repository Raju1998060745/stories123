import pandas as pd
from langchain_community.document_loaders.csv_loader import CSVLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma





#loader = CSVLoader(file_path="hf://datasets/FareedKhan/1k_stories_100_genre/1k_stories_100_genre.csv")
#data = loader.load()
#print(data stories)

with open("data/formatted_disney_princesses.txt") as f:
    princess = f.read()



text_splitter = CharacterTextSplitter(
    chunk_size=1000,
    separator="\n\n"
)
print (text_splitter)
texts = text_splitter.split_text(princess)
#print(texts[0])




#text = "LangChain is the framework for building context-aware reasoning applications"

#vectorstore = InMemoryVectorStore.from_texts(
#    [texts[0]],
#    embedding=embeddings,
#)
#embedding = embeddings.embed_documents(texts)

#print(len(embedding[0]))
# Use the vectorstore as a retriever
#retriever = vectorstore.as_retriever() kk

# Retrieve the most similar text
#retrieved_documents = retriever.invoke("Cinderella?")

# show the retrieved document's content
#print(retrieved_documents[0].page_content)
db = Chroma.from_documents(texts, OllamaEmbeddings(model="llama3"))

query = "Elsa"
docs = db.similarity_search(query)
print(docs[0].page_content)