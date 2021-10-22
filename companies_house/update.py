import pandas as pd
from typing import List

from constants import DEFAULT_DEFINITIONS_FILE

def update(
        url: str = 'https://developer-specs.company-information.service.gov.uk/companies-house-public-data-api/reference',
        path: str = DEFAULT_DEFINITIONS_FILE
) -> None:
    dfs: List[pd.DataFrame] = pd.read_html(url, encoding='utf-8')
    df: pd.DataFrame = pd.concat(dfs)
    df.reset_index(inplace=True)
    df.to_csv(path, index=False, encoding='utf-8')


if __name__ == '__main__':
    update()
