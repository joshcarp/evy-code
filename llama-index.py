from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, Settings
from llama_index.core.embeddings import resolve_embed_model
from llama_index.llms.ollama import Ollama
from llama_index.readers.file import CSVReader
from llama_index.readers.huggingface_fs import HuggingFaceFSReader

# load documents
loader = HuggingFaceFSReader()
documents = loader.load_data("datasets/joshcarp/evy-code")

# Load a CSV file
# csv_reader = CSVReader()
# documents = csv_reader.load_data(file=Path("evy_dataset.csv"))
# documents = SimpleDirectoryReader(".", "evy_dataset.csv").load_data()

# Load the dataset from the Hugging Face Hub

# Create the index
index = VectorStoreIndex.from_documents(documents)



# Create the index

# documents = SimpleDirectoryReader("data").load_file()

# bge embedding model
Settings.embed_model = resolve_embed_model("local:bigcode/starcoder2-3b")

# ollama
Settings.llm = Ollama(model="starcoder2", request_timeout=30.0)

index = VectorStoreIndex.from_documents(
    documents,
)
