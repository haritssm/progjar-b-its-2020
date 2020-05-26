import logging
import requests
import os
import threading


def download_gambar(url=None):
    if (url is None):
        return False
    ff = requests.get(url)
    tipe = dict()
    tipe['image/png'] = 'png'
    tipe['image/jpg'] = 'jpg'
    tipe['image/jpeg'] = 'jpg'

    content_type = ff.headers['Content-Type']
    logging.warning(content_type)
    if (content_type in list(tipe.keys())):
        namafile = os.path.basename(url)
        ekstensi = tipe[content_type]
        logging.warning(f"writing {namafile}.{ekstensi}")
        fp = open(f"{namafile}.{ekstensi}", "wb")
        fp.write(ff.content)
        fp.close()
    else:
        return False


threads = []
link = [
    'https://blog.tiket.com/wp-content/uploads/Gambar-Pemandangan-Alam-Terindah-Danau-Toba.jpg',
    'https://static.limakaki.com/2018/09/shutterstock_793946137-1.jpg',
    'https://backpackerjakarta.com/wp-content/uploads/2017/12/Anything-Bali.jpg'
]
for i in range(3):
    t = threading.Thread(target=download_gambar, args=(link[i],))
    threads.append(t)

for thr in threads:
    thr.start()