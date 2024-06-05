## Description

2023년 동안 쓴 365개의 일기 내용을 4개의 PDF 파일로 생성했습니다.<br/>
해당 4개의 파일을 참조하여 인덱싱 한 뒤 RAG를 통해 텍스트 생성 앱을 구현했습니다.<br/><br/>
AWS Workshop 계정으로 접근했고, Cloud9 웹브라우저 IDE를 통해 원격으로 실습을 진행했었습니다.


## Library Installation

```bash
pip3 install requirements.txt -U
```

## Running the app

```bash
streamlit run rag_pdfs_app.py --server.port 8080
```
