import requests
import json

def getRepoInformationByID(userId):
    #Check for right type: string
    if not isinstance(userId, str):
        raise TypeError("Expected a string. Incorrect Type")

    responseDictionary = {}

    #Request to retrieve repo of user.
    repoList_URL = f'https://api.github.com/users/{userId}/repos'
    repoList_Response = requests.get(repoList_URL)
    repoList_JSON = repoList_Response.json()

    for repo in repoList_JSON:
        #Do second request to retrieve number of commits for each repo.
        commits_URL = f"https://api.github.com/repos/{userId}/{repo['name']}/commits"
        commits_Response = requests.get(commits_URL)
        commits_JSON = commits_Response.json()

        #Iterate and count number of commits
        for commit in commits_JSON:
            if repo["name"] not in responseDictionary:
                responseDictionary[repo["name"]] = 1
            else:
                responseDictionary[repo["name"]] += 1


    return "\n".join(
            f"Repo: {key} Number of commits: {value}" 
            for key, value in responseDictionary.items()
            )

print(getRepoInformationByID("Johan0214"))
