from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class ProjectCreator:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.projectName = input("Enter a project name: ")
        self.projectDescription = input('Enter a project description: ')
        self.bot = webdriver.Firefox()

    def login(self):
        bot = self.bot
        bot.get('https://github.com/login')
        time.sleep(3)  # Wait for page to load
        username = bot.find_element_by_name('login')
        password = bot.find_element_by_name('password')
        username.clear()
        password.clear()
        username.send_keys(self.username)
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
        time.sleep(5)  # Wait for login to complete

    def createProject(self):
        bot = self.bot
        bot.get('https://github.com/new')
        time.sleep(3)  # Wait for page to load
        repName = bot.find_element_by_name('repository[name]')
        repDescription = bot.find_element_by_name('repository[description]')
        repName.clear()
        repDescription.clear()
        repName.send_keys(self.projectName)
        repDescription.send_keys(self.projectDescription)
        time.sleep(2)  # Wait for repo name check
        bot.find_element_by_class_name('js-repository-readme-choice').click()
        bot.find_element_by_class_name('first-in-line').click()


PC = ProjectCreator('YOUR_EMAIL', 'YOUR_PASSWORD')
PC.login()
PC.createProject()
