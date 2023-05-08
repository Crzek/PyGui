from PyQt6.QtWidgets import QFileDialog
from config.configs import data_dir, files_save


class Action:

    def __init__(self):
        pass

    def open_file(self, parent, label):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file_name, _ = QFileDialog.getOpenFileName(
            parent,
            "Open file",
            "",
            "All Files (*);;Text Files (*.txt)",
            options=options)
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

    def merge_Pdf(self):
        pass
