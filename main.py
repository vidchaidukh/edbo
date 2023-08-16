import grabbing
import parsing
import distributing

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


for offer in offers:
    grabbing.grab([offer[0], offer[1]])
    parsing.parse(offer[0])
    
distributing.distribute([(x[0], x[2]) for x in offers])