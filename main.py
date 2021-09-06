#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
import os, requests

file = os.listdir("test")
url = "192.168.50.190"
cookies = ""

for i in range(0, len(file)):
    post_header = {
        "Host": url,
        "Content-Length": "1126",
        "Cache-Control": "max-age=0",
        "Origin": "http://" + url,
        "Upgrade-Insecure-Requests": "1",
        "DNT": "1",
        "Content-Type": "multipart/form-data; boundary=----WebKitFormBoundary8MstAugNdsBBigBm",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Referer": "http://url/wp-admin/admin.php?page=daimma-import",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
        "Cookie": cookies,
        "Connection": "close"
    }
    post_data = "------WebKitFormBoundary8MstAugNdsBBigBm\nContent-Disposition: form-data; name=\"file_to_upload\"; filename=\"" + \
                file[i] + "\"\nContent-Type: text/markdown\n" + (open(os.getcwd() + "/test/" + file[i], "r",
                                                                      encoding="utf-8").read()) + "\n------WebKitFormBoundary8MstAugNdsBBigBm--"
    post_data = post_data.encode("utf-8")
    print(file[i], requests.post("http://" + url + "/wp-admin/admin.php?page=daimma-import", headers=post_header,
                                 data=post_data).status_code,i)
