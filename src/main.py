"""
Ponto de entrada da aplicação.
"""

from automation import ContentPublishingBot

from report import generate_report

from utils import load_links

from utils import load_contents

from logger import logger


def main():

    logger.info("=" * 50)
    logger.info("Content Publishing RPA")
    logger.info("=" * 50)

    links = load_links()

    contents = load_contents()

    logger.info(f"{len(links)} links encontrados.")

    logger.info(f"{len(contents)} conteúdos encontrados.")

    bot = ContentPublishingBot()

    bot.login()

    bot.read_contents()

    bot.validate_content()

    bot.publish_content()

    bot.generate_logs()

    generate_report()

    bot.close()

    logger.info("Processo finalizado com sucesso.")


if __name__ == "__main__":

    main()