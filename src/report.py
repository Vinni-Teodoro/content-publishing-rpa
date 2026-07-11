"""
Geração de relatório de exemplo.
"""

import pandas as pd

from config import OUTPUT_FILE

from logger import logger


def generate_report():

    report = pd.DataFrame(

        [

            {
                "Conteúdo": "Apresentação da Disciplina",
                "Status": "Publicado"
            },

            {
                "Conteúdo": "Aula Inaugural",
                "Status": "Já Existia"
            },

            {
                "Conteúdo": "Biblioteca Virtual",
                "Status": "Publicado"
            }

        ]

    )

    report.to_excel(

        OUTPUT_FILE,

        index=False

    )

    logger.info("Relatório salvo em output/report.xlsx")