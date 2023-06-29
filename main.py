import os
import time
import random
import string
from tqdm import tqdm

def convert_bits(bits):
    bytes = bits / 8
    kilobytes = bytes / 1024
    megabytes = kilobytes / 1024
    gigabytes = megabytes / 1024

    if gigabytes >= 1:
        return f"{gigabytes:.2f} GB"
    elif megabytes >= 1:
        return f"{megabytes:.2f} MB"
    elif kilobytes >= 1:
        return f"{kilobytes:.2f} KB"
    else:
        return f"{bytes:.2f} B"


def make_fake_dir(dir_path, dir_name):
    if not os.path.exists(dir_path+dir_name):
        os.mkdir(dir_path+dir_name)
    return dir_path+dir_name


def make_fake_file(file_path, file_name, file_extension='', content=''):
    with open(f'{file_path}/{file_name}.{file_extension}', 'w') as f:
        f.write(content)  
    #return os.stat(f'{file_path}/{file_name}.{file_extension}')

def delete_dir(dir_path, dir_name):
    try:
        os.rmdir(dir_path+dir_name) 
    except NotADirectoryError:
        os.remove(dir_path+dir_name)  
    except OSError:
        for path in os.listdir(dir_path+dir_name):
            delete_dir(dir_path+dir_name+'/', path) 
        os.rmdir(dir_path+dir_name) 

def main():
    path = os.getcwd()+'/'

    if True:
        for dir_name in tqdm(range(1,1+1000)):  
            dir_path = make_fake_dir(path, f'dir_{dir_name}')    

            file_name = 'fake_file' 
            file_path = dir_path
            content = ''.join([random.choice(string.ascii_letters) for _ in range(2**12)])
            make_fake_file(file_path, file_name, 'pdf',content)
        
        print('Creating fake files is ended')
    print(convert_bits(os.stat(path)[6]*8))
    time.sleep(60)

    if True:
        for dir in tqdm(os.listdir()):
            if dir == 'main.py': continue
            delete_dir(path, dir)

if __name__ == "__main__":
    main()