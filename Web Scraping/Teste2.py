import pdfplumber
import pandas as pd
import zipfile
import os

abreviacoes = {
    "OD": "Odontolôgia",
    "AMB": "Ambulatórial"
}

def extrair_dados(pdf_path):
    dados = []
    with pdfplumber.open(pdf_path) as pdf:
        for pagina in pdf.pages:
            tabela = pagina.extract_table()
            if tabela:
                for linha in tabela[1:]:
                    if len(linha) == 13:
                        dados.append(linha)
                    else:
                        print(f"Linha ignorada: {linha}")
    return dados

def salvar_csv(dados, procedimentos):
    df = pd.DataFrame(dados, columns=["PROCEDIMENTO", "RN", "VIGENCIA", "OD", "AMB", "HCO", "HSO", "REF", "PAC", "DUT", "SUBGRUPO", "GRUPO", "CAPITULO"])
    df['CAPITULO'] = df['CAPITULO'].replace(abreviacoes)
    df.fillna("N/A", inplace=True)
    df.to_csv(procedimentos, index=False)
    print(f"Arquivo CSV salvo: {procedimentos}")

def compactar_zip(caminho_csv, nome_zip):
    with zipfile.ZipFile(nome_zip, 'w', zipfile.ZIP_DEFLATED) as zipf:
        zipf.write(caminho_csv, os.path.basename(caminho_csv))
    print(f"Arquivo ZIP criado: {nome_zip}")

pdf_path = "Downloads/Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf"
dados = extrair_dados(pdf_path)

csv_nome = "procedimentos.csv"
salvar_csv(dados, csv_nome)

zip_nome = "procedimentos.zip"
compactar_zip(csv_nome, zip_nome)

os.remove(csv_nome)
print(f"Arquivo CSV removido: {csv_nome}")
