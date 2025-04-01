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

import pdfplumber
import pandas as pd
import zipfile
import os

abrevs = {
    "OD": "Odontolôgia",
    "AMB": "Ambulatórial"
}

def pegar_dados_do_pdf(caminho):
    info = []
    with pdfplumber.open(caminho) as pdf:
        for pagina in pdf.pages:
            tabela = pagina.extract_table()
            if tabela:  
                for linha in tabela[1:]: 
                    if len(linha) == 13:  
                        info.append(linha)
                    else:
                        print("Ignorando linha porque não tem 13 colunas:", linha)
    return info

def fazer_csv(info, nome_arquivo):
    tabela = pd.DataFrame(info, columns=["PROCEDIMENTO", "RN", "VIGENCIA", "OD", "AMB", "HCO", "HSO", "REF", "PAC", "DUT", "SUBGRUPO", "GRUPO", "CAPITULO"])
    tabela["CAPITULO"] = tabela["CAPITULO"].replace(abrevs)
    tabela.fillna("N/A", inplace=True) 
    tabela.to_csv(nome_arquivo, index=False)
    print("Salvei o CSV com o nome:", nome_arquivo)

def zipar_csv(arquivo_csv, nome_zip):
    with zipfile.ZipFile(nome_zip, "w", zipfile.ZIP_DEFLATED) as zipado:
        zipado.write(arquivo_csv, os.path.basename(arquivo_csv))
    print("Criei o ZIP com o nome:", nome_zip)


pdf = "Downloads/Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf"

info_extraida = pegar_dados_do_pdf(pdf)

nome_csv = "procedimentos_estagiario.csv"

fazer_csv(info_extraida, nome_csv)

nome_zip = "procedimentos_estagiario.zip"

zipar_csv(nome_csv, nome_zip)

os.remove(nome_csv)
print("Removido o arquivo temporário CSV:", nome_csv)
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
