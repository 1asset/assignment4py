from paragraphs import Paragraphs
scrapper = Paragraphs()
a = 1
for i in scrapper.get_paragraphs('bitcoin'):
    print(str(a) + ")     Title : " + i['title'] + ".\n    Link: "+ i['link'])
    print("Briefly: " + i['body'])
    print("############################################################################################################")
    a+=1
