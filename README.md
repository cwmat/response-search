# Response Search Helper

TODO

## Tech Stack

Client: Streamlit

Server Side: LangChain 🦜🔗

Vectorstore: Pinecone 🌲

## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`PINECONE_API_KEY`
`OPENAI_API_KEY`
`LANGCHAIN_TRACING_V2`
`LANGCHAIN_API_KEY`
`LANGCHAIN_PROJECT`
`PROJECT_PROFILE_HELPER_PASSWORD`

## Run Locally

Clone the project

```bash
  git clone git@github.com:cwmat/response-search.git
```

See `https://github.com/emarco177/documentation-helper.git` for more context, forked from this repo.

Go to the project directory

```bash
  cd documentation-helper
```

Download Docx data and place in

```bash
  ./data/
```

Install dependencies

```bash
  pipenv install
```

Push data to Pinecone (need to create the index first and update the name in `ingestion.py` and `backend/core.py`)

Run ingestion script to hydrate Pinecone index with docx embeddings

```bash
  pipenv run ingest
```

Start the streamlit server

```bash
  pipenv run start
```
