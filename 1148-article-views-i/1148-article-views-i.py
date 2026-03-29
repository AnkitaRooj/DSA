import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    df = views[views['author_id'] == views['viewer_id']][['author_id']].sort_values(by='author_id',ascending=True).drop_duplicates().rename(columns={'author_id':'id'})

    return df