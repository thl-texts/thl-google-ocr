from google.cloud import vision

client = vision.ImageAnnotatorClient()

with open('ocr-out.txt', 'a+', encoding='utf-8') as outf:
    for n in range(0, 100):
        txtnum = 540 + n
        print("doing page {}".format(txtnum))
        imgurl = 'gs://ngb-peltsek-scans/inverted/out_0{}-inv.jpg'.format(txtnum)
        # print(imgurl)
        response = client.document_text_detection({
            'source': {'image_uri': imgurl},
        })
        try:
            text_out = response.text_annotations[0].description
            outf.write(text_out)
        except Exception as e:
            print("\tNo response!", e)

print("done")
