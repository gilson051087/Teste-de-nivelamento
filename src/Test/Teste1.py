import os
import requests
from bs4 import BeautifulSoup
import zipfile


pasta_de_download = "pasta_de_download"
if not os.path.exists(pasta_de_download):
    os.mkdir(pasta_de_download)

site = 'https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos'
resposta = requests.get(site)


html = BeautifulSoup(resposta.text, 'html.parser')

lista_pdfs = []
for elemento in html.find_all('a', href=True):
    url_pdf = elemento['href']
    if '.pdf' in url_pdf:
        if 'anexo' in url_pdf or 'anexo-il' in url_pdf:
            if 'http' not in url_pdf:
                url_pdf = 'https://www.gov.br' + url_pdf
            lista_pdfs.append(url_pdf)

arquivos_baixados = []
for pdf in lista_pdfs:
    nome_arquivo = pdf.split("/")[-1]
    caminho_arquivo = pasta_de_download + "/" + nome_arquivo
    resposta_pdf = requests.get(pdf)
    with open(caminho_arquivo, 'wb') as arquivo:
        arquivo.write(resposta_pdf.content)
    arquivos_baixados.append(caminho_arquivo)
    print("Arquivo baixado:", nome_arquivo)

zip_arquivo = "arquivos_estagiario.zip"
with zipfile.ZipFile(zip_arquivo, 'w') as zip_estagiario:
    for arquivo in arquivos_baixados:
        zip_estagiario.write(arquivo, os.path.basename(arquivo))
    print("Todos os arquivos foram zipados no arquivo:", zip_arquivo)
