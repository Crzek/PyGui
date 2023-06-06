from PyQt6.QtWidgets import QFileDialog
from ..config.configs import data_dir,files_save


class Action:

    def __init__(self):
        pass
    def open_file(self, parent, label):
        file_name, _ = QFileDialog.getOpenFileName(
            parent,
            "Open file",
            "./",
            "All Files (*);;Text Files (*.txt);;PDF Document(*.pdf)")
        if file_name:
            with open(file_name, "r") as f:
                data = f.read()
                label.setText(data)
            return data

    def open_Pdf(self,
                 name: str = "PDF",
                 directory: str = data_dir,
                 typeFile: str = "PDF Document(*.pdf)"):
        pdf, _ = QFileDialog.getOpenFileName(None, name, directory, typeFile)
        return pdf
        # if pdf:
        #     with open(pdf, "r") as f:
        #         self.text = f.read()
        #     return pdf

    def saveFile(self,
                 name: str = "PDF",
                 directory: str = files_save,
                 typeFile: str = "PDF Document(*.pdf)"):
        file_path, _ = QFileDialog.getSaveFileName(self, name, directory,
                                                   typeFile)
        if file_path:
            with open(file_path, "w") as f:
                f.write(self.text)
            return file_path

    def savePath(self, label):
        file_name, typesFiles = QFileDialog.getOpenFileName(
            None, "Save Path File", "./", "All Files (*);;PDF Document(*.pdf)")
        if file_name:
            file_path = file_name.split("/")[-1]
            label.setText(f"file: {file_path}")

        return file_name

    def merge_Pdf(self):
        pass
