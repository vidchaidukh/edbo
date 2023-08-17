import numpy as np

offers = (
    ('121 ІПЗ КІС ОНП', 'https://vstup.edbo.gov.ua/offer/1139029/', 14),
    ('121 ІПЗ ІС', 'https://vstup.edbo.gov.ua/offer/1139597/', 30),
    ('121 ІПЗ КС', 'https://vstup.edbo.gov.ua/offer/1139596/', 30),
    ('123 КСМ ОНП', 'https://vstup.edbo.gov.ua/offer/1137896/', 12),
    ('123 КСМ', 'https://vstup.edbo.gov.ua/offer/1204677/', 40),
    ('126 ІУСТ ОНП', 'https://vstup.edbo.gov.ua/offer/1197065/', 11),
    ('126 ІУСТ', 'https://vstup.edbo.gov.ua/offer/1140142/', 34),
    ('126 ІІС', 'https://vstup.edbo.gov.ua/offer/1140178/', 35),
    ('126 ІЗРС', 'https://vstup.edbo.gov.ua/offer/1140177/', 34),
    ('121 ФПМ', 'https://vstup.edbo.gov.ua/offer/1139598/', 17),
    ('121 ФПМ ОНП', 'https://vstup.edbo.gov.ua/offer/1139561/', 10),
    ('123 ФПМ', 'https://vstup.edbo.gov.ua/offer/1213455/', 29),
    ('123 ФПМ ОНП', 'https://vstup.edbo.gov.ua/offer/1137897/', 10),
    ('125 ФТІ', 'https://vstup.edbo.gov.ua/offer/1207629/', 17))

def distribute(offers):
    print(offers)
    counts = [offer[1] for offer in offers]
    req_matrix = get_req_matrix((x[0] for x in offers))
    cond = True
    while cond:
        for offer_ind, offer in list(enumerate(req_matrix)):
            cond_all_checked = True
            for req in offer:
                if req[2] in ['допущено', 'зареєстровано']:
                    if counts[offer_ind] > 0:
                        req_matrix, counts = deactivate_req(req_matrix, req[1], req[3], counts)
                        req[2] = 'Рекомендовано на бюджет'
                        counts[offer_ind] -= 1
                    else:
                        req[2] = 'Рекомендовано'
                    cond_all_checked = False
                    break

        print(counts)
        write_req_matrix(req_matrix)
        cond = check_distrubution(req_matrix, counts)
        _ = input("stoped")

                        

def get_req_matrix(files):
    matrix = []
    for file in files:
        requests = filtrate(np.load('npy/'+ file +'.npy'))
        print(requests)
        f = open(file + '.csv', "w", encoding="utf-8")
        f.write(str(requests))
        f.close()
        matrix.append(requests)
    return matrix

def filtrate(requests):
    index_bad_reqs = []
    for ind in range(len(requests)):
        if requests[ind][2] == 'відмова':
            index_bad_reqs.append(ind)
        elif requests[ind][3] == 'К':
            index_bad_reqs.append(ind)
        elif float(requests[ind][4]) < 130:
            index_bad_reqs.append(ind)
        elif 'скасовано' in requests[ind][2]:
            index_bad_reqs.append(ind)
            
    return list(np.delete(requests, index_bad_reqs, axis=0))
    

def deactivate_req(req_matrix, pib, prior, counts):
    for offer_ind, offer in list(enumerate(req_matrix)):
        print("OOOOOFFER" + str(offer[1]))
        for ind, req in reversed(list(enumerate(offer))):
            if req[1] == pib and int(req[3]) > int(prior):
                if req[2] == 'Рекомендовано на бюджет':
                    cond_new_approved = False
                    for inner_req in offer[ind:]:
                        if inner_req[2] not in ['Рекомендовано на бюджет', 'Зараховано за вищим пріоритетом']:
                            inner_req[2] = 'Рекомендовано на бюджет'
                            cond_new_approved = True
                            break
                    if not cond_new_approved:
                            counts[offer_ind] += 1
                req[2] = 'Зараховано за вищим пріоритетом'
                offer.append(offer.pop(ind))
    return req_matrix, counts

def check_distrubution(req_matrix, avaliable_counts):
    cond = False
    for ind, offer in reversed(list(enumerate(req_matrix))):
        for req in offer:
            if req[2] == 'допущено' or req[2] == 'зареєстровано':
                cond = True
                print("ДОП", req[1])
            elif req[2] == 'Рекомендовано' and avaliable_counts[ind] > 0:
                cond = True
                print("РЕК", req[1])

    return cond

def write_req_matrix(req_matrix):
    with open('final_matrix.csv', 'w', encoding='utf-8') as f:
        for offer in req_matrix:
            f.write(str(offer) + '\n\n')

distribute([(x[0], x[2]) for x in offers])