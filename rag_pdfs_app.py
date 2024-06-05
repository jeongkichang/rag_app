import streamlit as st
import rag_pdfs_lib as glib

st.set_page_config(page_title="Rag and Text Generation", layout="wide")
st.title("Rag and Text Generation Application")

st.sidebar.title("Options")
page = st.sidebar.radio("Choose a task", ["Text Generation"])

if 'vector_index' not in st.session_state:
    with st.spinner("Indexing documents..."):
        st.session_state.vector_index = glib.get_index()

if page == "Text Generation":
    st.header("Text Generation")
    input_text = st.text_area("Input text", label_visibility="collapsed")

    go_button = st.button("Go", type="primary")

    if go_button:
        with st.spinner("Generating response..."):
            # Generate text response
            response_text = glib.generate_response(st.session_state.vector_index, input_text)

            st.subheader("Generated Text")
            st.write(response_text)
