from pandas import read_excel

df=read_excel("清理后2.xls")

# 原始有多少行
count_lines= df.shape[0]

index_list=df.index.tolist()

print(index_list)

never_list=[]
with open('neverlook.csv','r',encoding='utf-8') as neverdf:
    neverli=neverdf.read().split('\n')
    for nums in neverli:
        if nums !='':
            never_list.append(int(nums))
    print(never_list)
