#!/usr/bin/env python3

# Import libraries
from selenium import webdriver
import tkinter as tk
import tkinter.simpledialog

# Ask Username and Password
tk.Tk().withdraw()
username = tkinter.simpledialog.askstring("Student ID", "Student ID:")
password = tkinter.simpledialog.askstring("Password", "Password:", show='*')

# Log in
YouAtB = "http://youatb.unibocconi.it/"
bboard = "http://blackboard.unibocconi.it/"
driver = webdriver.Chrome(executable_path = "/usr/local/chromedriver")

driver.get(YouAtB)

driver.find_element_by_id("username").send_keys(username)
driver.find_element_by_id("password").send_keys(password)
driver.find_element_by_class_name("Button").click()

# Open BBoard
driver.get(bboard)
