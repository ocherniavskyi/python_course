from selene import config

from api.jira_client.clients.JiraClient import JiraClient

jira_url = 'https://jira.hillel.it'
username = 'OleksiiCherniavskyi'
password = 'OleksiiCherniavskyi'
project = 'WEBINAR'
issue_tag = 'ocher'
config.base_url = jira_url