import os
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_ollama import OllamaEmbeddings
from langchain_pinecone import PineconeVectorStore
from pinecone import Pinecone

from langchain.chains.question_answering import load_qa_chain

def split_t(princess):
    text_splitter = CharacterTextSplitter(
        chunk_size=1000,
        separator="\n\n"
    )
    return text_splitter.split_documents(princess)

def embeding():
    embed = OllamaEmbeddings(
        model="nomic-embed-text"
    )
    return embed

def pinecone_store(texts, embed):
    os.environ['PINECONE_API_KEY'] = '5e000385-2e76-4a2a-a9a7-2166c1e77885'
    #pinecone.init(api_key=os.getenv('PINECONE_API_KEY'))

    index_name = "princessdisney"
    return PineconeVectorStore.from_documents(texts, embed, index_name=index_name)

def stored_data(store):
    stored=store
    return stored

def q_a(llm):
    chain=load_qa_chain(llm, chain_type="stuff")
    return chain

def retrieve_query(query,k=2):
    os.environ['PINECONE_API_KEY'] = '5e000385-2e76-4a2a-a9a7-2166c1e77885'
    api_key = os.environ.get("PINECONE_API_KEY")
    index_name = "princessdisney"
    embed = embeding()
    query_vector=embed.embed_query(query)
    pc = Pinecone(api_key=api_key)
    index = pc.Index(index_name)
    store= index.query(vector=query_vector,top_k=2)
    #matching_results=store.similarity_search(query,k=k)

    text_field = "text"  
    vectorstore = PineconeVectorStore(  index, embed, text_field )  
    res=vectorstore.similarity_search(  query, k=1)
    return res
    




def main():
    file_path = os.path.join('data', 'formatted_disney_princesses.txt')
    princess = TextLoader(file_path).load()
    embed = embeding()
    texts = split_t(princess)
    #print(len(texts))
    vectors=embed.embed_query("who is ")
    print(len(vectors))
    query="snow white"
    store=pinecone_store(texts,embed)
    print(store)
    matching_results=store.similarity_search(store, query,k=2)
    print(matching_results)
    #"elsa", k=2,
    #)
    #print(results)
    

if __name__ == "__main__":
    main()
