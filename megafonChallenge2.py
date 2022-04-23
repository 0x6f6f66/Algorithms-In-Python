

s2 = '.акызя оготэ еинавзан еоньлачановреп тенатс мотевто мынреВ .атпигЕ огенверД еонтовиж еовилсоныв еомас — ,ыноараф тюузьлопси йыроток ,акызя епитогол аН'


s = 'jhds26473834sdfsddsdff3892sdjgjs36478348jdfdff38923djkms36478348jsg\
kjjkdvnk326474sdfss3247888237jsh23647383djd3345dhj6729gh23647383det\
ifhsjdhjkd62346sdf3204dshf8326jddgdj3025shb7484hfj4838sedgdj3025sew\
kksd44786264sjdhfd303sdnnsk356dgdksj1537dhdhd3673978svdfssvj1537ddg\
fuhuifd43647733dsf334dfgsdg324shdhfb2573sjv4364shd6377fdjfgb2573sdf\
fshjdshjsdf472934d3248dfgj8376sfsjab2674sv4762dhfjl6373ygdsc9536svd\
kjjkdvnk3264744dfdd2587366832sdjjcsv2547shs3644hfh7337sjhjab2674scv\
jhds26473834dsifhsdhfd4373sfdhjsbjhc9536svdh362476376dhdfwsj1537dds'

"""

lOfSymbols = {}
for symbol in s:
    if symbol not in lOfSymbols:
        lOfSymbols[symbol] = 1
    else:
        lOfSymbols[symbol] += 1

for i in lOfSymbols:
    print(f'{i}: {lOfSymbols[i]}')
"""

print(s2[::-1])