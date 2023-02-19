import cv2
import numpy as np
import os
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import Qt, QTimer

class CameraApp(QWidget):

    def __init__(self):
        super().__init__()

        # Create a layout for the window
        layout = QVBoxLayout()

        # Create a label to show the camera view
        self.camera_view = QLabel()
        self.camera_view.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.camera_view)

        # Add a button to take photos
        self.button = QPushButton('Take photo')
        self.button.clicked.connect(self.take_photo)
        layout.addWidget(self.button)

        # Set the layout for the window
        self.setLayout(layout)

        # Set up the camera
        self.cap = cv2.VideoCapture(0)

        # Set up a timer to update the camera view
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_camera_view)
        self.timer.start(30)

    def update_camera_view(self):
        # Read a frame from the camera
        ret, frame = self.cap.read()

        # Convert the frame to RGB
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Convert the frame to a QImage
        h, w, c = frame.shape
        qimg = QImage(frame.data, w, h, w*c, QImage.Format_RGB888)

        # Set the QImage as the pixmap for the camera view label
        self.camera_view.setPixmap(QPixmap.fromImage(qimg))

    def take_photo(self):
        # Read a frame from the camera
        ret, frame = self.cap.read()

        # Save the photo to the device's storage
        filename = 'photo.jpg'
        cv2.imwrite(filename, frame)

if __name__ == '__main__':
    # Create the application
    app = QApplication(sys.argv)

    # Create the main window
    window = CameraApp()
    window.show()

    # Run the application
    sys.exit(app.exec())