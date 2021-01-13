# thl-google-ocr

This repo is for scripts used to OCR (generally Tibetan) texts for THL and related projects.

The simplest script `quickocr.py` just does a simple call to convert one image and 
this call is repeated for a known series of numbered images.

Further developments should include REST calls to the Google Storage to convert all files in a bucket.

The scripts use the Google Vision API and other Google APIS. See:

* https://cloud.google.com/functions/docs/tutorials/ocr
* https://cloud.google.com/vision/product-search/docs/reference/rest
* https://cloud.google.com/vision/docs
* https://googleapis.dev/python/vision/latest/index.html
* https://googleapis.dev/python/vision/latest/vision_v1/types.html


Than Grove
Jan 13, 2021