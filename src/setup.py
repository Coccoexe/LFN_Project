import urllib.request
import zipfile
import os

DATA_PATH = os.getcwd() + "/data/"

def downloadDataset(url, filename):
    print("START  |  Downloading " + filename + "datasets...")
    urllib.request.urlretrieve(url, DATA_PATH + filename + ".zip")
    print("DONE   |  Downloaded datasets\n")

    print("START  |  Extracting zip...")
    with zipfile.ZipFile(DATA_PATH + filename + ".zip", 'r') as zip:
        zip.extractall(DATA_PATH)
    print("DONE   |  Extracted datasets\n")

    print("START  |  Removing useless file...")
    for file in os.listdir(DATA_PATH):
        if not file.endswith(".edges"):
            os.remove(DATA_PATH + file)
    print("DONE   |  Removed useless file\n")

    print("START  |  Renamoving headers...")
    with open(DATA_PATH + filename + ".edges", 'r') as f:
        data = f.read().splitlines(True)
    with open(DATA_PATH + filename + ".edges", 'w') as f:
        f.writelines(data[3:])
    print("DONE   |  Renamoved headers\n")

def main():

    filenames = ["bio-mouse-gene", "bio-human-gene1"]
    urls = ["https://nrvis.com/download/data/bio/bio-mouse-gene.zip", 
            "https://nrvis.com/download/data/bio/bio-human-gene1.zip"]

    # check if data folder exists
    if not os.path.exists(DATA_PATH): os.makedirs(DATA_PATH)

    for i in range(len(urls)):
        if not os.path.exists(DATA_PATH + filenames[i] + ".edges"):
            downloadDataset(urls[i], filenames[i])

if __name__ == "__main__":
    main()