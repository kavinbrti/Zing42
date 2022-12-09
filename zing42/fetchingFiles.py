# -*- coding: utf-8 -*-
"""
Created on Fri Dec  9 16:58:35 2022

@author: kavin
"""

import os
import requests


def download(url: str, dest_folder: str):
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)  # create folder if it does not exist

    filename = url.split('/')[-1].replace(" ", "_")  # be careful with file names
    file_path = os.path.join(dest_folder, filename)

    r = requests.get(url, stream=True)
    if r.ok:
        print("saving to", os.path.abspath(file_path))
        with open(file_path, 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024 * 8):
                if chunk:
                    f.write(chunk)
                    f.flush()
                    os.fsync(f.fileno())
    else:  # HTTP status code 4XX/5XX
        print("Download failed: status code {}\n{}".format(r.status_code, r.text))


download("https://archives.nseindia.com/content/equities/EQUITY_L.csv", dest_folder="mydir")
download("https://archives.nseindia.com/content/historical/EQUITIES/2022/DEC/cm08DEC2022bhav.csv.zip", dest_folder="mydir")