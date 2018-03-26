import os
import pandas as pd
from typing import List


def update():
    dfs: List[pd.DataFrame] = pd.read_html('https://developer.companieshouse.gov.uk/api/docs/')
    df: pd.DataFrame = pd.concat(dfs)
    path: str = os.path.join(os.path.dirname(__file__), 'definition.csv')
    df.to_csv(path, index=False)


if __name__ == '__main__':
    update()
