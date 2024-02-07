from langchain_community.document_loaders import YoutubeLoader
from langchain.schema import Document
import nltk
from langchain.text_splitter import NLTKTextSplitter
nltk.download('punkt')
# from langchain_community.document_transformers import DoctranTextTranslator
# from dotenv import load_dotenv
# from langchain_community.text_splitter import RecursingCharacterTextSplitter
# lets try this code for first time hehehehe
# load_dotenv("api.env")
text = YoutubeLoader.from_youtube_url("https://youtu.be/VXfJwZORMCc")
data = text.load()
print(data[0])

text_splitter = NLTKTextSplitter()
sentences = text_splitter.split_text(str(data[0]))
for sentence in sentences:
  chunk_with_punctuation = sentence+ "."
  print(sentence)
# page_content = data[0]
# document = [Document(page_content=str(page_content))]
# qa_translator = DoctranTextTranslator(language="spanish")
# translated_docs = qa_translator.transform_documents(document)
# print(translated_docs[0].page_content)
