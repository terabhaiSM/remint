import os
import requests
from llama_index.llms.openai import OpenAI
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from IPython.display import Markdown, display

# Set OpenAI API Key
os.environ["OPENAI_API_KEY"] = "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"

def extract_content_from_pdf(pdf_path):
    documents = SimpleDirectoryReader(pdf_path).load_data()
    index = VectorStoreIndex(documents)
    query_engine = index.as_query_engine()
    response = query_engine.query("What is the summary of paper?")
    return response

def main():
    pdf_path= "uploads"
    print(pdf_path)
    if pdf_path:
        summary = extract_content_from_pdf(pdf_path)
        display(Markdown(f"{summary}"))
        print(summary)
    else:
        print("Failed to download or read the PDF.")

if __name__ == "__main__":
    main()
