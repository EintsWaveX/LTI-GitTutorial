import sys
import os
import time
import random
from PyQt6 import QtWidgets, QtCore
from PyQt6.QtCore import QThread, pyqtSignal
from PyQt6.QtWidgets import QApplication, QWidget
from main_ui import Ui_Form  # File UI untuk MainApp
from motivasi_ui import Ui_Form as MotivasiForm  # File UI untuk MotivasiApp

class ProgressThread(QThread):
    progress_updated = pyqtSignal(int)

    def run(self):
        for i in range(101):
            time.sleep(0.05)  # Delay to simulate progress
            self.progress_updated.emit(i)

class MotivasiApp(QWidget):
    def __init__(self):
        super().__init__()

        # Setup UI untuk MotivasiApp
        self.ui = MotivasiForm()
        self.ui.setupUi(self)

        # Daftar kalimat motivasi
        self.motivasi_list = [
            "Semangat, nama! Setiap tugas dan ujian adalah langkah menuju mimpi besarmu di kampus ini.",
            "nama, jangan takut gagal di kampus. Kegagalan adalah guru terbaik yang akan membawamu menuju kesuksesan.",
            "Tetap semangat kuliahnya, nama! Ilmu yang kamu kumpulkan hari ini akan membuka pintu masa depan cerah.",
            "nama, ingat bahwa setiap pagi di kampus adalah kesempatan baru untuk belajar dan berkembang.",
            "Skripsi atau tugas boleh sulit, tapi nama, tekad dan kerja kerasmu akan membawamu ke garis finis!",
            "Kampus adalah tempat belajar dan bertumbuh, nama. Nikmati setiap prosesnya dan jangan menyerah.",
            "nama, walau hari ini penuh tugas dan kelas yang padat, percayalah kamu selangkah lebih dekat dengan wisuda!",
            "Tetap fokus dan semangat, nama! Masa depan cerah menantimu setelah perjuangan di kampus ini.",
            "nama, ingatlah bahwa hasil terbaik datang dari usaha terbaik. Jangan lelah belajar dan mengejar impianmu.",
            "Setiap malam begadang untuk belajar akan terbayar, nama. Tetaplah berjuang hingga kamu memakai toga dengan bangga!"
        ]

        # Menghubungkan tombol ke fungsi
        self.ui.pushButton.clicked.connect(self.display_motivasi)

    def display_motivasi(self): 
        # Mengambil nama dari textBrowser
        user_name = self.ui.textBrowser.toPlainText().strip()

        if user_name:  # Pastikan nama tidak kosong
            # Pilih kalimat acak dan ganti "nama" dengan nama pengguna
            random_sentence = random.choice(self.motivasi_list)
            personalized_sentence = random_sentence.replace("nama", user_name)

            # Menampilkan kalimat motivasi di textBrowser_2
            self.ui.textBrowser_2.setText(personalized_sentence)
        else:
            # Jika textBrowser kosong, tampilkan pesan default
            self.ui.textBrowser_2.setText("Masukkan nama terlebih dahulu!")

class MainApp(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.progressBar.setValue(0)

        # Connect buttons to their respective functions
        self.ui.pushButton.clicked.connect(self.open_applications)
        self.ui.pushButton_2.clicked.connect(self.open_applications)
        self.ui.pushButton_3.clicked.connect(self.open_applications)
        self.ui.pushButton_4.clicked.connect(self.open_applications)
        self.ui.pushButton_5.clicked.connect(self.open_motivasi_app)
        self.ui.pushButton_6.clicked.connect(self.run_progress)

    def open_applications(self):
        button_id = self.sender()
        match button_id:
            case button_id if button_id == self.ui.pushButton:
                if os.name == 'nt': os.system("start https://chatgpt.com/")
                elif os.name == 'posix': os.system("xdg-open https://chatgpt.com/")
                elif os.name == 'macos': os.system("open https://chatgpt.com/")

            case button_id if button_id == self.ui.pushButton_2:
                if os.name == 'nt': os.system("start https://claude.ai/new")
                elif os.name == 'posix': os.system("xdg-open https://claude.ai/new")
                elif os.name == 'macos': os.system("open https://claude.ai/new")

            case button_id if button_id == self.ui.pushButton_3:
                if os.name == 'nt': os.system("start https://www.blackbox.ai/")
                elif os.name == 'posix': os.system("xdg-open https://www.blackbox.ai/")
                elif os.name == 'macos': os.system("open https://www.blackbox.ai/")

            case button_id if button_id == self.ui.pushButton_4:
                if os.name == 'nt': os.system("start https://gemini.google.com/?hl=en-IN")
                elif os.name == 'posix': os.system("xdg-open https://gemini.google.com/?hl=en-IN")
                elif os.name == 'macos': os.system("open https://gemini.google.com/?hl=en-IN")


    def open_motivasi_app(self):
        # Membuka jendela aplikasi motivasi
        self.motivasi_window = MotivasiApp()
        self.motivasi_window.show()

    def run_progress(self):
        self.ui.label_2.setText("Please do not make any action, until progress reach 100%")
        self.thread = ProgressThread()
        self.thread.progress_updated.connect(self.ui.progressBar.setValue)
        self.thread.finished.connect(self.on_progress_complete)
        self.thread.start()

    def on_progress_complete(self):
        self.ui.label_2.setText("Progress completed! You can continue.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec())
