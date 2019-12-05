import pandas as pd
src = pd.read_excel('СК_05-12-19.xlsx')
deps = {}
for snils in src['СНИЛС'].dropna().unique():
    tmpdf = src[src['СНИЛС'] == snils].loc[:, ['Организация', 'Комплекс', 'ГРБС','Является ОИВ']].drop_duplicates()
    size = len(tmpdf.index)
    step = 0
    for index, row in tmpdf.iterrows():       
        if size != 1:
            if step == 0:
                org = row[0]
                com = row[1]
                grbs = row[2]
                oiv = row[3]
                if row[2] not in deps: deps.update({row[2]:[0,0,0,0,0]})
                step += 1
            else:
                if row[3] == 'Да':
                    if row[1] != com:
                        deps[grbs][3] += 1
                    else:
                        deps[grbs][2] += 1
                else:
                    if row[1] != com:
                        deps[grbs][1] += 1
                    else:
                        deps[grbs][0] += 1
                break
        else:
            if row[2] not in deps: deps.update({row[2]:[0,0,0,0,0]})
            grbs = row[2]
            deps[grbs][4] += 1
print(deps)
