import pandas as pd
import math

# kintoneに登録されている商品一覧取得
filename_kin = pd.read_csv('../itemlist_kintone.csv', encoding='cp932',sep=',', engine='python', error_bad_lines=False)

list_kin_id = []
list_kin_procd = []

list_kin_id =  filename_kin['$id']
list_kin_procd =  filename_kin['product_cd']


# e2に登録されている商品一覧取得
filename_e2 = pd.read_csv('../商品情報一覧.csv', encoding='cp932',sep=',', engine='python', error_bad_lines=False)

list_e2_id = []
list_e2_procd = []

list_e2_id =  filename_e2['$id'].copy()
list_e2_procd =  filename_e2['product_cd']

idex=0
leng = len(list_e2_procd)


for n in range(leng):

    match = list_kin_procd[list_kin_procd == list_e2_procd[n]]

    if not match.empty:
        #print(list_kin_id[match.index[0])
        list_e2_id[n] = str(math.floor(list_kin_id[match.index[0]]))
        #print(str(math.floor(list_kin_id[match.index[0]])))
    else:
        list_e2_id[n] = ""

   

filename_e2['$id'] = list_e2_id.copy()
filename_e2.to_csv("../itemlist_new.csv", index=False, encoding='cp932',sep=',')


