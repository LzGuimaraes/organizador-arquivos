# organizador.py
import os
import shutil
import logging
from config import MAPA_DE_PASTAS

def organizar_pasta(caminho_da_pasta: str, dry_run: bool = False) -> int:
    if not os.path.isdir(caminho_da_pasta):
        logging.error(f"O caminho '{caminho_da_pasta}' não existe ou não é uma pasta.")
        return 0

    try:
        lista_de_arquivos = os.listdir(caminho_da_pasta)
    except Exception as e:
        logging.error(f"Erro ao listar arquivos: {e}")
        return 0

    arquivos_movidos = 0
    
    for nome_arquivo in lista_de_arquivos:
        caminho_origem = os.path.join(caminho_da_pasta, nome_arquivo)
        if os.path.isdir(caminho_origem):
            continue

        _, extensao = os.path.splitext(nome_arquivo)
        extensao = extensao.lower()

        if extensao in MAPA_DE_PASTAS:
            nome_pasta_destino = MAPA_DE_PASTAS[extensao]
            caminho_pasta_destino = os.path.join(caminho_da_pasta, nome_pasta_destino)

            if not os.path.exists(caminho_pasta_destino):
                logging.info(f"Criando pasta: {caminho_pasta_destino}")
                if not dry_run:
                    os.makedirs(caminho_pasta_destino)

            caminho_destino_final = os.path.join(caminho_pasta_destino, nome_arquivo)
            
            if dry_run:
                logging.info(f"[DRY-RUN] {nome_arquivo} → {nome_pasta_destino}")
            else:
                try:
                    shutil.move(caminho_origem, caminho_destino_final)
                    arquivos_movidos += 1
                    logging.info(f"Movido: {nome_arquivo} → {nome_pasta_destino}")
                except Exception as e:
                    logging.error(f"Erro ao mover '{nome_arquivo}': {e}")

    return arquivos_movidos