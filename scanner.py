from pathlib import Path
from collections import defaultdict
import hashlib
import itertools


class BtnFunc:
    def __init__(self):
        # self.scan_btn = scan_btn
        self.system_root = Path(Path.home().anchor)
        self.files = []
        self.file_size_dict = defaultdict(list)
        self.duplicate_dict = {}
        self.hash_match = defaultdict(list)
        self.duplicate_match = defaultdict(list)
        self.first_chunk = defaultdict(list)


    def scan_device(self):
        all_elements = itertools.chain(self.system_root.rglob('*.pdf'), self.system_root.rglob('*.docx'))
        for i in all_elements:
            try:
                if i.is_file():
                    self.files.append(i)
            except (PermissionError, FileNotFoundError):
                pass


    def get_size_dict(self):
        for i in self.files:
            try:
                self.file_size_dict[i.stat().st_size].append(i)
            except (PermissionError, FileNotFoundError):
                pass


    def get_duplicate_sizes(self):
        self.duplicate_dict = {k:v for (k, v) in self.file_size_dict.items() if len(v) > 1}


    def find_duplicates(self):
        for i in self.duplicate_dict.values():
            for j in i:
                hasher = hashlib.sha256()
                try:
                    with open(j, 'rb') as f:
                        chunk = f.read(8192)
                        hasher.update(chunk)
                        self.hash_match[hasher.hexdigest()].append(j)
                except (PermissionError, FileNotFoundError, OSError):
                    pass
        self.first_chunk = {k:v for (k, v) in self.hash_match.items() if len(v) > 1}
        for i in self.first_chunk.values():
            for j in i:
                hasher = hashlib.sha256()
                try:
                    with open(j, 'rb') as f:
                        chunk = f.read(8192)
                        while chunk:
                            hasher.update(chunk)
                            chunk = f.read(8192)
                    self.duplicate_match[hasher.hexdigest()].append(j)
                except (PermissionError, FileNotFoundError, OSError):
                    pass




if __name__ == '__main__':
    btns = BtnFunc()
    btns.scan_device()
    # btns.get_size_dict()
    # btns.get_duplicate_sizes()
    # btns.find_duplicates()
    print(len(btns.files))