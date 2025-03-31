import os
import requests
import zipfile
from bs4 import BeautifulSoup

url = 'https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos'

donwload_dir = "Downloads"
os.makedirs(donwload_dir, exist_ok=True)

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

pdf_links = []
for link in soup.find_all('a', href=True):
    href = link['href']
    if href.endswith(".pdf") and ("anexo" in href.lower() or "anexo-il" in href.lower()):
        pdf_links.append(href if href.startswith('http') else "https://www.gov.br" + href)

donwload_files = []
for pdf_url in pdf_links:
    arquivos = os.path.join(donwload_dir, os.path.basename(pdf_url))
    response = requests.get(pdf_url)
    with open(arquivos, "wb") as f:
        f.write(response.content)
    donwload_files.append(arquivos)
    print(f"Baixado: {arquivos}")

zip_file = "anexos_gov.zip"
with zipfile.ZipFile(zip_file, "w") as zipf:
    for file in donwload_files:
        zipf.write(file, os.path.basename(file))
    print(f"Arquivos zipados: {zip_file}")
