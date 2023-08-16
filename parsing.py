from bs4 import BeautifulSoup
import numpy as np

class_list = ("offer-request-n", "offer-request-fio", "offer-request-status", "offer-request-priority")
def parse(file):
    page = open("html/"+file + ".html", encoding="utf-8").read()
    soup = BeautifulSoup(page, "html.parser")
    raw_requests = soup.find_all("div", {"class": "offer-request"})

    requests = []
    f = open('csv/' + file + '.csv', "w", encoding="utf-8")
    for raw_request in raw_requests[1:]:
        request = []
        for class_name in class_list:
            request.append(raw_request.find("div", {"class": class_name}).find("div").text)
        kv = float(raw_request.find("div", {"class": "offer-request-kv"}).find("div").text.replace(',', '.'))
        request.append(kv if kv else 0)
        grades = [float(x.text.split(" ")[2].replace(',', '.')) for x in raw_request.find_all("div", {"class": "f"})]
        grades.extend([0 for _ in range(3-len(grades))])
        request.extend(grades)
        requests.append(request)
    f.write(str(requests))
    f.close()
    np.save("npy/"+file+'.npy', np.array(requests))
