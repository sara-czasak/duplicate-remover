from pathlib import Path
from collections import defaultdict


class BtnFunc:
    def __init__(self):
        # self.scan_btn = scan_btn
        self.system_root = Path(Path.home().anchor)
        self.files = []
        self.file_size_dict = defaultdict(list)
        self.duplicate_dict = {}


    def scan_device(self):
        all_elements = self.system_root.rglob('*')
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


    def get_duplicates(self):
        self.duplicate_dict = {k:v for (k, v) in self.file_size_dict.items() if len(v) > 1}





if __name__ == '__main__':
    btns = BtnFunc()
    btns.scan_device()
    btns.get_size_dict()
    btns.get_duplicates()
    print(len(btns.duplicate_dict))