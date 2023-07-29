import datetime as dt
import subprocess

from PySide6.QtGui import QIcon, QPixmap
from PySide6.QtWidgets import QMainWindow

from fjt.model import Media, MediaType, normalize_number
from fjt.ui.main_window import Ui_MainWindow


def copy_to_clipboard(message):
    process = subprocess.Popen(["wl-copy"], stdin=subprocess.PIPE)
    process.communicate(input=message.encode())


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        media_types = MediaType.select(MediaType.name).order_by(
            MediaType.last_usage.desc()
        )
        self.ui.combo_box_media_type.addItems(
            [media_type.name for media_type in media_types]
        )
        saved_media = Media.select(Media.name).order_by(Media.last_usage.desc())
        self.ui.combo_box_name.addItems([media.name for media in saved_media])
        #
        self.ui.push_button_copy.clicked.connect(self.on_push_button_copy_clicked)
        #
        self.ui.combo_box_media_type.currentIndexChanged.connect(self.on_change)
        self.ui.double_spin_box_amount.valueChanged.connect(self.on_change)
        self.ui.combo_box_name.currentTextChanged.connect(self.on_name_change)
        self.ui.combo_box_name.currentIndexChanged.connect(self.on_name_change)
        self.ui.line_edit_additional.textChanged.connect(self.on_change)
        self.on_name_change()

    def on_push_button_copy_clicked(self):
        media_type_name = self.ui.combo_box_media_type.currentText()
        amount = normalize_number(self.ui.double_spin_box_amount.value())
        name = self.ui.combo_box_name.currentText().strip()
        additional = self.ui.line_edit_additional.text().strip()
        text = f".log {media_type_name} {amount} {name} {additional}".strip()
        media_type = MediaType.get_or_none(MediaType.name == media_type_name)
        media_type.last_usage = dt.datetime.utcnow()
        media_type.usage_count += 1
        media_type.save()
        media, _ = Media.get_or_create(
            name=name,
            media_type=media_type,
        )
        media.last_amount = amount
        media.last_additional_info = additional
        media.save()
        copy_to_clipboard(text)

    def on_name_change(self):
        name = self.ui.combo_box_name.currentText()
        media = Media.get_or_none(Media.name == name)
        if media:
            self.ui.combo_box_media_type.setCurrentText(media.media_type.name)
            self.ui.double_spin_box_amount.setValue(media.last_amount)
            self.ui.line_edit_additional.setText(media.last_additional_info)
        self.on_change()

    def on_change(self):
        media_type_name = self.ui.combo_box_media_type.currentText()
        amount = normalize_number(self.ui.double_spin_box_amount.value())
        name = self.ui.combo_box_name.currentText()
        additional = self.ui.line_edit_additional.text()
        text = f".log {media_type_name} {amount} {name} {additional}".strip()
        self.ui.line_edit_log.setText(text)
        media_type = MediaType.get_or_none(MediaType.name == media_type_name)
        self.ui.label_result.setText(
            f"{media_type.amount_text} → +{normalize_number(amount*media_type.points)} points"
        )
