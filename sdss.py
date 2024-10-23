import tkinter as tk
from tkinter import simpledialog
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


# Function to open a URL
def open_url():
    url = simpledialog.askstring("Input", "Enter URL:")
    if url:
        driver.get(url)


# Initialize the main window
root = tk.Tk()
root.title("Simple Browser")

# Create a button to open a URL
open_button = tk.Button(root, text="Open URL", command=open_url)
open_button.pack(pady=20)

# Set up the Selenium WebDriver (make sure you have the appropriate driver installed)
driver = webdriver.EdgeOptions()  # You can use Firefox or any other browser

# Run the Tkinter event loop
root.mainloop()

# exit()
# import sys
# from PyQt5.QtCore import *
# from PyQt5.QtWidgets import *
# from PyQt5.QtWebEngineWidgets import *


# class Browser(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.browser = QWebEngineView()
#         self.browser.setUrl(
#             QUrl(
#                 "https://my.spline.design/abstractblob10-2137c29154cfe90c7806039c9a1954cc/"
#             )
#         )
#         self.setCentralWidget(self.browser)
#         self.showMaximized()

#         # Navigation Bar

#     #     navbar = QToolBar()
#     #     self.addToolBar(navbar)

#     #     back_btn = QAction("Back", self)
#     #     back_btn.triggered.connect(self.browser.back)
#     #     navbar.addAction(back_btn)

#     #     forward_btn = QAction("Forward", self)
#     #     forward_btn.triggered.connect(self.browser.forward)
#     #     navbar.addAction(forward_btn)

#     #     reload_btn = QAction("Reload", self)
#     #     reload_btn.triggered.connect(self.browser.reload)
#     #     navbar.addAction(reload_btn)

#     #     home_btn = QAction("Home", self)
#     #     home_btn.triggered.connect(self.navigate_home)
#     #     navbar.addAction(home_btn)

#     #     self.url_bar = QLineEdit()
#     #     self.url_bar.returnPressed.connect(self.navigate_to_url)
#     #     navbar.addWidget(self.url_bar)

#     #     self.browser.urlChanged.connect(self.update_url)

#     # def navigate_home(self):
#     #     self.browser.setUrl(QUrl("http://google.com"))

#     # def navigate_to_url(self):
#     #     url = self.url_bar.text()
#     #     self.browser.setUrl(QUrl(url))

#     # def update_url(self, q):
#     #     self.url_bar.setText(q.toString())


# app = QApplication(sys.argv)
# QApplication.setApplicationName("My Browser")
# window = Browser()
# app.exec_()
