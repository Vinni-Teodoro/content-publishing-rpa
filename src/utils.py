"""
Funções auxiliares.
"""

import pandas as pd

from config import INPUT_FILE


def load_links():

    return pd.read_excel(
        INPUT_FILE,
        sheet_name="Links"
    )


def load_contents():

    return pd.read_excel(
        INPUT_FILE,
        sheet_name="Conteúdos"
    )