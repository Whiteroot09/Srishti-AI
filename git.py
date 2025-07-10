from github import Github
my_git = Github("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")
for repo in my_git.get_user().get_repos():
    print(repo.name)