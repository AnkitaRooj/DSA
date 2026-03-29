import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    # df = orders.merge(customers, left_on = 'customerId', 
    #         right_on = 'id', how='right'
    #         ) 
    # df = df[df['id_x'].isna()][['name']]
    # df.rename(columns={'name':'Customers'}, inplace=True)

    df = customers.loc[~customers['id'].isin(orders['customerId']),['name']]
    df.rename(columns={'name':'Customers'}, inplace=True)
    return df