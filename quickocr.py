from os import path
from google.cloud import vision

bucket = 'ngb-peltsek-scans'
folder = 'ngb_vol58jpg'
startpg = 201
endpg = 500
outdir = 'docs'
outfilenm = 'pt-vol058-ocr-201-500.txt'

outpath = path.join(outdir, outfilenm)
client = vision.ImageAnnotatorClient()

with open(outpath, 'a+', encoding='utf-8') as outf:
    for n in range(startpg, endpg + 1):
        pgnum = str(n).zfill(4)
        print("doing page {}".format(pgnum))
        imgname = 'out_{}.jpg'.format(pgnum)
        imgurl = 'gs://{}/{}/{}'.format(bucket, folder, imgname)
        # print(imgurl)
        response = client.document_text_detection({
            'source': {'image_uri': imgurl},
        })
        try:
            text_out = response.text_annotations[0].description
            outf.write(imgname + "\n")
            outf.write(text_out)
        except Exception as e:
            print("\tNo response!", e)

print("done")
