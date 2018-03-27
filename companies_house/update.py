import os
import pandas as pd
from typing import List


def update(
        url: str='https://developer.companieshouse.gov.uk/api/docs/',
        path: str=os.path.join(os.path.dirname(__file__), 'definition.csv')
) -> None:
    dfs: List[pd.DataFrame] = pd.read_html(url)
    df: pd.DataFrame = pd.concat(dfs)
    df.to_csv(path, index=False)


if __name__ == '__main__':
    update()
