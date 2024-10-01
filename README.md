## Python/Github API Test

Repository create/delete test.

## Requirements

* Python3: https://www.python.org/downloads/

## Description
  .env file contains GITHUB_TOKEN. File demonstrates sample github token: "demotokennumber1".
  To use this paste your token and run with "os.getenv" from "os" library(check requirements.txt).
  Don't show or upload .env file with your token. To prevent upload .env file to github add .env to .gitignore as shown here(remove #).
  
  First test:
    create repo 'repo_name_demo'.
  Second test:
    check all repo names from user and delete 'repo_name_demo' repo.

## Installation
pip install -r requirements.txt

## Running

pytest -v

## Used instruments

* pytest: https://docs.pytest.org/
* unittest: https://docs.python.org/3/library/unittest.html
* dotenv: https://pypi.org/project/python-dotenv/
* PyGitHub: https://pygithub.readthedocs.io/en/stable/
  
