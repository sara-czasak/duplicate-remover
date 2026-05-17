from pathlib import Path


class BtnFunc:
    def __init__(self):
        # self.scan_btn = scan_btn
        self.system_root = Path(Path.home().anchor)
        self.files = []


    def scan_device(self):
        all_elements = self.system_root.rglob('*')
        for i in all_elements:
            try:
                if i.is_file():
                    self.files.append(i)
            except PermissionError:
                pass






if __name__ == '__main__':
    btns = BtnFunc()
    btns.scan_device()
    print(btns.files)