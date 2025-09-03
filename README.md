# Small RAG

## Instructions

Please use python 3.12+

### Create virtual env
```bash
python -m venv .venv
source .venv/bin/activate
```
### Install dependecies
```bash
pip install -r requirements.txt
```

### Setup your OpenAI API key
```bash
export  OPENAI_API_KEY="your key"
```

### Copy in the data folder
Copy the folder `data` into the repository, on the same level as `src`

### Ingest documents to database
```bash
cd src
python ingest_documents.py
```

### Start the application
```bash
python main.py
```


## The "Architecture"

This application is based on FastAPI which is a standard python library for APIs nowadays. The FAST API is run on uvicorn which enables higher load on the API.
It also uses langchain which is a tools for chaining mostly LLM calls (perfectly suitable for RAG since it also support document retrieval)
Finally, I use Dependency injector. In order to be able to scale the application, there may be some changes in the way the main components for RAG are implemented.
- Ingestion
- Vector/Document Store
- LLM


## Improvements needed for "Production ready RAG":
- There may be a ton of improvements on the retrieval/answer quality side:
  - With longer texts chunking will become a must (the embedding models have a limited contextual window) 
  - Doing more sophisticated retrieval (Vector + BM25, Knowledge Graphs)
  - The prompt/llm hyperparameters can be tuned for better performance (this will require some qualitative benchmark to be created)
- Production ready
  - CI/CD pipeline needs to be constructed. The code should be containerized
  - Tests (Unit, Integration)
  - Logging and monitoring should also be setup
  - Some production type vector store needs to be deployed. Probably ElasticSearch based DB that can handle higher loads.

## Application workflow
- `ingest_documents.py`
  - Document ingestion script
    - I selected the OpenAI embedding with one of the LangChain local persistent vector stores.
- `main.py`
  - The main components are ingested via the dependency injector in `services.py`:
    - Embedding - to embed the documents and user query ()
    - Document Store - store the embedded documents and retrieves the relevant documents based on embedded user query
    - llm - Takes the relevant documents and user query to generate an answer (gpt-4.1)
  - `api`
    - There are two API endpoints:
      - `/` for the UI part of  the application (the whole UI is ChatGPT generated, since I am not a frontend expert)
      - `ask` the main "backend functionality" which takes in the user question and returns a streamed LLM answer.
        - The whole endpoint is completely async to allow for multiple requests without any blocking
        - For better UX the endpoint is streaming the answer, which makes user to wait shorter for something to start happening
          - I measured around (1.5 - 2s) till the first tick was returned
