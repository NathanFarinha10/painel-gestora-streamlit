# pages/2_Leitor_de_PDF.py

import streamlit as st
import fitz  # PyMuPDF
import io

st.set_page_config(layout="wide")
st.title(" ferramenta de Leitura e Extração de PDF")
st.write("Faça o upload de um PDF de análise de mercado para extrair e visualizar seu texto.")

# Componente de upload de arquivo
uploaded_file = st.file_uploader("Escolha um arquivo PDF", type="pdf")

if uploaded_file is not None:
    # Para ler o arquivo em memória, usamos o io.BytesIO
    file_bytes = io.BytesIO(uploaded_file.read())

    try:
        # Abrir o PDF com PyMuPDF a partir dos bytes em memória
        with fitz.open(stream=file_bytes, filetype="pdf") as doc:
            st.success(f"PDF '{uploaded_file.name}' carregado com sucesso!")
            st.write(f"O documento tem {doc.page_count} páginas.")

            # Extrair e mostrar o texto de todo o documento
            text_content = ""
            for page_num in range(doc.page_count):
                page = doc.load_page(page_num)
                text_content += f"--- TEXTO DA PÁGINA {page_num + 1} ---\n"
                text_content += page.get_text("text") # Extrai o texto puro
                text_content += "\n\n"

            st.subheader("Conteúdo Extraído do Documento Completo:")
            st.text_area("Texto", text_content, height=500)

    except Exception as e:
        st.error(f"Ocorreu um erro ao processar o PDF: {e}")

else:
    st.info("Aguardando o upload de um arquivo PDF.")
