from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont


class InfoPopup(QWidget):
    def __init__(self, title, description, parent=None):
        super().__init__(parent)
        self.setWindowFlags(Qt.ToolTip)  # Setting window flags for tooltip style

        layout = QVBoxLayout()  # Vertical layout for widget

        # Creating QLabel for title with similar font properties
        self.titleLabel = QLabel(title)
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.titleLabel.setFont(font)

        # Creating QLabel for description similar to QTextBrowser
        self.descriptionLabel = QLabel(description)
        font = QFont()
        font.setPointSize(11)
        self.descriptionLabel.setFont(font)
        self.descriptionLabel.setWordWrap(True)  # Ensuring text wraps within the label

        # Adjusting layout spacing
        layout.setContentsMargins(10, 10, 10, 10)  # Set margins around the layout
        layout.setSpacing(5)  # Reduce spacing between widgets

        # Adding widgets to the layout
        layout.addWidget(self.titleLabel)
        layout.addWidget(self.descriptionLabel)

        # Set layout and apply style
        self.setLayout(layout)
        self.setStyleSheet(
            """
            QWidget {
                background-color: #f0f0f0;
                border: 1px solid #b0b0b0;
                border-radius: 8px;
                padding: 10px;
            }
            QLabel {
                margin-bottom: 5px;  /* Reduce margin between title and description */
            }
            """
        )
