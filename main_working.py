from typing import Set

from backend.core import run_llm
import streamlit as st
from streamlit_chat import message


def create_sources_string(source_files: Set[str]) -> str:
    if not source_files:
        return ""
    sources_list = list(source_files)
    sources_list.sort()
    sources_string = "sources:\n"
    for i, source in enumerate(sources_list):
        sources_string += f"{i+1}. {source}\n"
    return sources_string


st.header("📚 Project Profile Search Helper Bot")
st.subheader(
    "Enter a description of the project you are working on a response for and I will try to help you find relevant project profiles"
)
if (
    "chat_answers_history" not in st.session_state
    and "user_prompt_history" not in st.session_state
    and "chat_history" not in st.session_state
):
    st.session_state["chat_answers_history"] = []
    st.session_state["user_prompt_history"] = []
    st.session_state["chat_history"] = []


prompt = st.text_input("Prompt", placeholder="Enter your message here...") or st.button(
    "Submit"
)

if prompt:
    with st.spinner("Generating response..."):
        generated_response = run_llm(
            query=prompt, chat_history=st.session_state["chat_history"]
        )

        # Assuming 'filename' is used in metadata during ingestion
        source_filenames = set(
            doc.metadata.get("filename", "Unknown source")
            for doc in generated_response["source_documents"]
        )
        formatted_response = f"{generated_response['answer']} \n\n {create_sources_string(source_filenames)}"

        st.session_state.chat_history.append((prompt, generated_response["answer"]))
        st.session_state.user_prompt_history.append(prompt)
        st.session_state.chat_answers_history.append(formatted_response)

if st.session_state["chat_answers_history"]:
    for generated_response, user_query in zip(
        st.session_state["chat_answers_history"],
        st.session_state["user_prompt_history"],
    ):
        message(
            user_query,
            is_user=True,
        )
        message(generated_response)
