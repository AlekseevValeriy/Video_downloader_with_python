import threading

import pyperclip
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from moviepy.editor import *
from pytube import YouTube, Playlist

import Core_work_tools_menu
import design_new_test


class MainWindow(QtWidgets.QMainWindow, design_new_test.Ui_YoViDo):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # self.meaning_for_rename = ''
        self.p_progress = 0
        self.bar_of_progress_downloading.setMaximum(100)
        self.bar_of_progress_downloading.setValue(0)

        self.special_directory_button.clicked.connect(self.getDirectory)
        self.push_button_download.clicked.connect(self.thr)
        self.push_button_paste_in_line_link.clicked.connect(self.paste_link)
        self.push_button_paste_in_line_directory.clicked.connect(self.paste_path)

        self.action_functional_list.triggered.connect(Core_work_tools_menu.ClssFunctionalList(self).functional_list)
        self.action_how_do_it.triggered.connect(Core_work_tools_menu.ClssHowDoIt(self).how_do_it)
        self.action_open_temporary_error_log.triggered.connect(
            Core_work_tools_menu.ClssListErrorTemporary(self).open_error_list_temporary)
        self.action_open_permanent_error_log.triggered.connect(
            Core_work_tools_menu.ClssListErrorPermanent(self).open_error_list_permanent)
        self.action_copy_temporary_error_log.triggered.connect(
            Core_work_tools_menu.ClssListErrorTemporary(self).copy_error_list_temporary)
        self.action_copy_permanent_error_log.triggered.connect(
            Core_work_tools_menu.ClssListErrorPermanent(self).copy_error_list_permanent)
        self.action_clear_permanent_error_log.triggered.connect(
            Core_work_tools_menu.ClssListErrorPermanent(self).clear_permanent_error_log)
        self.action_clear_temporary_error_log.triggered.connect(
            Core_work_tools_menu.ClssListErrorTemporary(self).clear_temporary_error_log)
        self.action_replace_permanent_error_log.triggered.connect(
            Core_work_tools_menu.ClssListErrorPermanent(self).replace_permanent_error_log)
        self.action_replace_temporary_error_log.triggered.connect(
            Core_work_tools_menu.ClssListErrorTemporary(self).replace_temporary_error_log)
        self.action_clear_all_error_logs.triggered.connect(Core_work_tools_menu.clear_all_error_logs)
        self.action_replace_all_error_logs.triggered.connect(Core_work_tools_menu.replace_all_error_logs)

        self.change_status_bar_status('1')

    def on_progress(self, stream, chunk, bytes_remaining):
        total_size = stream.filesize
        bytes_downloaded = total_size - bytes_remaining

        l_progress = int(bytes_downloaded / total_size * 100)
        if l_progress > self.p_progress:
            self.p_progress = l_progress
            self.bar_of_progress_downloading.setValue(l_progress)

    def custom_hook(self, error):
        with open('numbers', 'r') as file:
            all_out_numbers = [int(i.rstrip().lstrip()) for i in file.readlines()]
        with open('error_list_temporary', 'a') as file:
            file.write(f"{all_out_numbers[0]}) {error.exc_value}\n{str(error)}\n")
        with open('error_list_permanent', 'a') as file:
            file.write(f"{all_out_numbers[1]}) {error.exc_value}\n{str(error)}\n")
        with open('numbers', 'w') as file:
            [file.write(f'{str(i + 1)}\n') for i in all_out_numbers]
        self.push_button_download.setEnabled(True)
        self.change_status_bar_status('5')

    def change_status_bar_status(self, status):
        statuses = {'1': 'Waiting for work to start', '2': 'Processing', '3': 'Downloading', '4': 'Completed',
                    '5': 'Error'}
        self.statusBar.showMessage(statuses[status], 0)

    def paste_path(self):
        self.line_edit_directory.setText(pyperclip.paste())

    def paste_link(self):
        self.line_edit_link.setText(pyperclip.paste())

    # def mp3_download(self):
    #         self.rename(self.global_name, self.line_edit_directory.text())

    def download_link(self):
        self.browser_counte_of_videos.setText('0/1')
        self.bar_of_progress_downloading.setValue(0)
        yt = YouTube(self.line_edit_link.text())
        yt.register_on_progress_callback(self.on_progress)
        self.choseQuality(yt).download(self.line_edit_directory.text())
        self.p_progress = 0
        self.browser_counte_of_videos.setText('1/1')
        self.push_button_download.setEnabled(True)
        self.change_status_bar_status('4')

    def download_links_for_playlist(self):
        playlist_counter = Playlist(self.line_edit_link.text()).video_urls
        self.browser_counte_of_videos.setText(f'{0}/{len(playlist_counter)}')
        for i in enumerate(playlist_counter):
            self.choseQuality(i[1]).download(self.line_edit_directory.text())
            # if self.special_box_quality.currentText() == '.mp3':
            #     self.rename(self.choseQuality(i), self.line_edit_link.text())
            self.browser_counte_of_videos.setText(f'{i[0]}/{len(playlist_counter)}')
        self.push_button_download.setEnabled(True)
        self.change_status_bar_status('4')

    def thr(self):
        threading.excepthook = self.custom_hook
        if self.special_box_type.currentText() == 'video':
            thread = threading.Thread(target=self.download_link)
            thread.start()
            self.browser_counte_of_videos.setText('0/0')
        elif self.special_box_type.currentText() == 'playlist':
            thread = threading.Thread(target=self.download_links_for_playlist)
            thread.start()
            self.browser_counte_of_videos.setText('0/0')
        self.change_status_bar_status('3')
        self.push_button_download.setEnabled(False)

    # @staticmethod
    # def conventor(mp4, mp3):
    #     print(mp4)
    #     print(mp3)
    #     command = f"ffmpeg -i {mp4} {mp3}.mp3"
    #     subprocess.call(command, shell=True)
    #
    # def rename(self, old_name, directory):
    #     print(old_name)
    #     if not directory:
    #         self.conventor(old_name.title + self.meaning_for_rename, old_name.title)
    #         # os.remove(old_name.default_filename)
    #     else:
    #         self.conventor(directory + '/' + old_name.title + self.meaning_for_rename,
    #                        directory + '/' + old_name.title)
    #         # os.remove(directory + '/' + old_name.default_filename)

    def getDirectory(self):
        dirlist = QFileDialog.getExistingDirectory(self)
        self.line_edit_directory.setText("{}".format(dirlist))

    def choseQuality(self, link):
        # if self.special_box_quality.currentText() == '.mp3':
        #     self.meaning_for_rename = '.webm'
        #     return link.streams.get_by_itag(251)
        # elif self.special_box_quality.currentText() == '.mp4 L':
        if self.special_box_quality.currentText() == '.mp4 L':
            # self.meaning_for_rename = '.3gpp'
            return link.streams.get_lowest_resolution()
        elif self.special_box_quality.currentText() == '.mp4 H':
            # self.meaning_for_rename = '.mp4'
            return link.streams.get_highest_resolution()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    root = MainWindow()
    root.show()
    with open('numbers', 'r') as f:
        number = [i.rstrip().lstrip() for i in f.readlines()]
    with open('numbers', 'w') as f:
        f.write(f"1\n")
        f.write(f"{number[1]}")
    open('error_list_temporary', 'w').close()
    sys.exit(app.exec_())
