from tqdm import tqdm
import os
import glob
from pathlib import Path
import os.path
import re

if __name__ == '__main__':
    directory = r'C:\Users\nikhi\OneDrive\Documents\gitUploads\Capstone_Dataset\Python'
    for root, subdirectories, files in tqdm(list(os.walk(directory))):
        for file in tqdm(list(files)):
            path = os.path.join(root, file)
            with open(path, 'r') as f:
                lines = f.readlines()
            with open(path, 'w') as f:
                text = ''
                for i in lines:
                    text += i
                text = re.sub('"""[\w\W]*?"""', '', text, flags=re.S)
                out = re.sub("'''[\w\W]*?'''", '', text, flags=re.S)
                f.writelines(out)