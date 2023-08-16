arr = [ [ [1,2,3], [1,2,3]], [[2,3,4], [2,3,4]], [[3,4,5], [3,4,5]]]

for offer in arr:
    with open('final_matrix.csv', 'a+', encoding='utf-8') as f:
        f.write(str(offer))