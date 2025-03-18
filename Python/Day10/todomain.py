import sys
from PyQt5 import QtWidgets
from todolist import Ui_MainWindow 


class TodoListApp(QtWidgets.QMainWindow): #TodoListApp Sınıfının nelerden türedigini yazdik
    def __init__(self):
        super().__init__()

        # Ui_MainWindow sınıfından bir örnek oluşturuyoruz.
        # Bu örnek, tasarımın arayüz öğelerini ve işlevselliğini içerir.
        self.ui = Ui_MainWindow()
        # Oluşturduğumuz Ui_MainWindow örneğini, bu QMainWindow altında kuruyoruz.
        self.ui.setupUi(self)

        self.ui.pushButton_8.clicked.connect(self.add_task) # task olusturma butonu aktifleştirme
        self.ui.pushButton_6.clicked.connect(self.delete_task) # taski silme butonu aktifleştirme
        self.ui.pushButton_9.clicked.connect(self.delete_all_tasks) # bütün tasklari silen butonu aktifleştirme
        self.ui.pushButton_5.clicked.connect(self.exit_app) # uygulamadan cikis yapan butona aktifleştirme

    def add_task(self):
        task_text = self.ui.lineEdit.text() # Metin giriş kutusundaki girilen metni alma

        # Girilen metin boş değilse (yani bir görev girilmişse) devam etme
        if task_text:
            self.ui.listWidget.addItem(task_text) # ListWidget'e yeni bir öğe (görev) ekleme
            self.ui.lineEdit.clear() # Metin giriş kutusunu temizleme



    def delete_task(self):
        selected_item = self.ui.listWidget.currentItem() # Şu an seçili olan öğeyi alma (kullanıcı bu öğeyi seçmişse)

        if selected_item: # Eğer bir öğe seçilmişse devam et
            self.ui.listWidget.takeItem(self.ui.listWidget.row(selected_item)) # Seçilen öğeyi ListWidget'tan kaldır


    def delete_all_tasks(self):
        self.ui.listWidget.clear() # Listwidget'taki bütün görevleri silme


    def exit_app(self):
        sys.exit() # direk çıkış yapar 

# Ana program akışını kontrol ediyoruz
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv) # PyQt5 uygulama nesnesini başlatıyoruz ve komut satırı argümanlarını alıyoruz.
    todo_app = TodoListApp()    # TodoListApp sınıfından bir örnek oluşturuyoruz.
    todo_app.show()   # Oluşturduğumuz pencereyi görünür hale getiriyoruz.
    sys.exit(app.exec_())  # Uygulamayı çalıştırıyoruz ve etkileşim bekliyoruz.
