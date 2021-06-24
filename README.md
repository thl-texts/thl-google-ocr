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

## Instructions
### Convert Original Images to JPEGs
If original scans are .tiff they need to be converted to .jpgs. This can be done on a Mac with the script in this 
repo called `convimgs.sh`. The Mac will need to have ImageMagick installed using homebrew, e.g. `brew install imagemagick`.
The script assumes that the .tiffs are in a sister folder called "tiffs" and there is an output folder called "jpgs", but
these directory names can be changed in the script itself. To run the script type `./convimgs.sh` and it will convert 
all images in the /tiffs folder.

### Upload JPEGs to Google Cloud
In the CSC Google Cloud Console (https://console.cloud.google.com/storage/browser/), there is a 
"Google OCR Project (woven-invention-254116)". Choose this project and go to the storage section. There are buckets 
there to hold the images. Use an existing one or create your own and upload all images into a folder on that 
bucket. The example here is the /ngb-peltsek-scans bucket.

### Set up Authentication
Go to the Service Accounts section for the project and create a key and down load the JSON file for the key.
Then in a terminal do:
    `export GOOGLE_APPLICATION_CREDENTIALS="/home/user/Downloads/service-account-file.json"`
Pointing to the JSON file. This will allow you to access the storage bucket with your script.

### Run the OCR Script
Edit the script `quickocr.py` and modify the variables at the top of the script to match your situation:

```python
bucket = 'ngb-peltsek-scans'
folder = 'ngb_vol58jpg'
startpg = 0
endpg = 100
outdir = 'docs'
outfilenm = 'pt-vol058-ocr-1-100.txt'
```

These are self-explanatory. The out directory is relative to the script itself.

Then run the script with `python quickocr.py` in a terminal or through your IDE.

Than Grove
Jan 13, 2021 (modified June 24, 2021)