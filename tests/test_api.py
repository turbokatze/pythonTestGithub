import os
import unittest
from dotenv import load_dotenv
from github import Github
from github import Auth


class PythonTest(unittest.TestCase):
    def test_create_repo(self):
        load_dotenv()
        auth = Auth.Token(os.getenv('GITHUB_TOKEN'))
        g = Github(auth=auth)
        user_login = g.get_user().login
        user = g.get_user()
        user.create_repo('repo_name_demo') #create repo
        print(user)
        assert True

    def test_print_repos(self):
        load_dotenv()
        auth = Auth.Token(os.getenv('GITHUB_TOKEN'))
        g = Github(auth=auth)
        user_login = g.get_user().login
        g.get_user()
        for repo in g.get_user().get_repos(): #show current repos
            print(repo.name)

            if repo.name == 'repo_name_demo': #delete repo
                repo.delete()
                assert True

if __name__ == "__main__":
    unittest.main()