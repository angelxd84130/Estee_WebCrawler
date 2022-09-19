import plotly
import pandas as pd
import openpyxl

def daily_discount_rank(df) -> None:
    #data = df['所有價格'].apply(pd.Series)
    data = pd.concat([df.drop(['所有價格'], axis=1), df['所有價格'].apply(pd.Series)], axis=1)
    #data = data[['產品編號', '產品名', '資料更新時間', '市售價', '折扣後價格']]
    data['DateTime'] = data['資料更新時間'].str[:10]
    data['Discount'] = (data['市售價'] - data['折扣後價格'])
    data = data[['產品編號', '產品名', 'DateTime', 'Discount']]
    data.sort_values(by=['DateTime', '產品編號', 'Discount'], inplace=True)
    data.dropna(inplace=True)
    data.drop_duplicates(['產品編號', '產品名', 'DateTime', 'Discount'], keep='last', inplace=True, ignore_index=True)
    data.to_excel('daily_discount_rank.xlsx', index=False)


def weekly_price_change(df) -> None:
    data = pd.concat([df.drop(['所有價格'], axis=1), df['所有價格'].apply(pd.Series)], axis=1)



def Analysis() -> None:
    df = pd.read_json('data.json')
    daily_discount_rank(df)
    weekly_price_change()

Analysis()