from selene import config
import allure
from allure import attachment_type
from selene import browser

from api.jira_client.clients.JiraClient import JiraClient

jira_url = 'https://jira.hillel.it'
username = 'OleksiiCherniavskyi'
password = 'OleksiiCherniavskyi'
project = 'WEBINAR'
issue_tag = 'ocher'
config.base_url = jira_url
config.reports_folder = './reports'
config.timeout = 5


def pytest_exception_interact(node, call, report):
    allure.attach(
        name='Screenshot',
        body=browser.driver().get_screenshot_as_png(),
        attachment_type=attachment_type.PNG
    )
