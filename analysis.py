import pandas as pd
from datetime import timedelta
import openpyxl

def daily_discount_rank(df) -> None:
    # expand all price
    data = pd.concat([df.drop(['所有價格'], axis=1), df['所有價格'].apply(pd.Series)], axis=1)
    data['DateTime'] = data['資料更新時間'].str[:10]
    data['Discount'] = (data['市售價'] - data['折扣後價格'])
    data = data[['產品編號', '產品名', 'DateTime', 'Discount']]
    data["Rank"] = data.groupby("DateTime")["Discount"].rank("dense", ascending=False)
    data.sort_values(by=['DateTime', 'Rank',  '產品編號'], inplace=True, ascending=[True, True, True])
    data.dropna(inplace=True)
    data.drop_duplicates(['產品編號', '產品名', 'DateTime', 'Discount'], keep='last', inplace=True, ignore_index=True)
    data.to_excel('daily_discount_rank.xlsx', index=False)


def weekly_price_change(df) -> None:
    data = pd.concat([df.drop(['所有價格'], axis=1), df['所有價格'].apply(pd.Series)], axis=1)
    data['DateTime'] = pd.to_datetime(data['資料更新時間'].str[:10], format='%Y-%m-%d')
    data = data[['產品編號', '產品名', 'DateTime', '折扣後價格']].dropna()
    data.sort_values(by=['產品編號', 'DateTime', '折扣後價格'], inplace=True)
    # drop data come from the same day, and only keep the cheapest price left
    data.to_excel('before_drop.xlsx', index=False)
    data.drop_duplicates(['產品編號', '產品名', 'DateTime', '折扣後價格'], keep='first', inplace=True, ignore_index=True)
    data = data.merge(data, how='inner', on=['產品編號', '產品名'])
    # data.keys() = Index(['產品編號', '產品名', 'DateTime_x', '折扣後價格_x', 'DateTime_y', '折扣後價格_y'], dtype='object')
    data = data[(data['DateTime_x']+timedelta(days=1) == data['DateTime_y'])]
    data['Price_diff'] = data['折扣後價格_y'] - data['折扣後價格_x']
    # print(data[['DateTime_x', 'DateTime_y']].head())  # check time diff = 1 day
    data.to_excel('weekly_price_change.xlsx', index=False)



def Analysis() -> None:
    df = pd.read_json('data.json')
    daily_discount_rank(df)
    #weekly_price_change(df)

Analysis()