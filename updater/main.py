import logging
import sys
import traceback

from PyQt5.QtWidgets import QApplication, QMessageBox

from main_window import MainWindow

window = None


def new_except_hook(etype, evalue, tb):
    QMessageBox.information(
        None, "Error", "".join(traceback.format_exception(etype, evalue, tb)))
    logging.critical(evalue)
    print(evalue)

    global window
    window.stop_recording()
    window.close()


def main():
    result = -1

    try:
        sys.excepthook = new_except_hook
        app = QApplication([])

        global window
        window = MainWindow()
        window.show()
        result = app.exec_()
    except Exception as e:
        window.stop_recording()
        logging.critical(e)
        print(e)

    sys.exit(result)


if __name__ == '__main__':
    main()
