import argparse
import logging
from organizador import organizar_pasta

def main():
    parser = argparse.ArgumentParser(description="Organizador de Arquivos")
    parser.add_argument(
        "--pasta",
        type=str,
        default=".",
        help="Caminho da pasta a ser organizada (default: pasta atual)"
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Simula a execução sem mover arquivos"
    )
    parser.add_argument(
        "--log",
        type=str,
        default="organizador.log",
        help="Arquivo de log (default: organizador.log)"
    )

    args = parser.parse_args()

    # Configuração do logging
    logging.basicConfig(
        filename=args.log,
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )

    logging.info("Iniciando organização da pasta")
    total = organizar_pasta(args.pasta, args.dry_run)
    logging.info(f"Organização concluída. {total} arquivos movidos.")

    if args.dry_run:
        print("[DRY-RUN] Simulação concluída. Veja os logs para detalhes.")
    else:
        print(f"Organização concluída! {total} arquivos movidos.")

if __name__ == "__main__":
    main()
