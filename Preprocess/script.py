import os
from pathlib import Path
import glob
from tqdm import tqdm

def C_PP( ip_path, op_path ): 
    Codeset = ip_path
    Preprocessed = op_path
    cmd = ''
    for i in ['*.c']:
        for code_path in sorted(glob.glob(os.path.join(Codeset, i))):
            ip_fname = Path(code_path).stem
            op_path = Preprocessed+ '\\' + ip_fname + '_PP.c'     # Output file name = ip_fname_PP.c
            cmd = 'gcc -E -I' + pycpath + ' ' + code_path + ' > ' + op_path
            os.system(cmd)

pycpath = r'C:\Users\nikhi\OneDrive\Documents\Engineering-3\6thSEM\Capstone\code\pycparser\utils\fake_libc_include' # Path to pycparsers fake_lib_include
directory = r'C:\Users\nikhi\OneDrive\Documents\gitUploads\Capstone_Dataset\C' # Base Directory with all C folders
for root, subdirectories, files in tqdm(list(os.walk(directory))):
    for subdirectory in tqdm(list(subdirectories)):
        ip_path = os.path.join(root, subdirectory)
        op_path = ip_path.replace('\C\\','\Preprocessed_C\\')
        if not os.path.exists(op_path):
            os.makedirs(op_path)
        C_PP(ip_path,op_path)