import requests
from pydantic import BaseModel



class activity(BaseModel):
    id: str
    event: str
    repo: str 


def get_github_activity(url: str) -> list[activity]:
    repo = requests.get(url)
    data = repo.json()

    list = []
    for r in data:
    
        acti = activity(
             id=r["id"],
             event=r["type"],
             repo=r["repo"]["name"]
            )
        list.append(acti)

    return list[:3]
    
      
print(get_github_activity("https://api.github.com/users/hkirat/events"))






"""
[{"id":"10850493764","type":"WatchEvent","actor":{"id":49764726,"login":"farazghani","display_login":"farazghani","gravatar_id":"","url":"https://api.github.com/users/farazghani","avatar_url":"https://avatars.githubusercontent.com/u/49764726?"},"repo":{"id":754221844,"name":"hkirat/open-source-contribution","url":"https://api.github.com/repos/hkirat/open-source-contribution"},"payload":{"action":"started"},"public":true,"created_at":"2026-06-18T19:01:10Z"},
{"id":"12582610974","type":"PushEvent","actor":{"id":49764726,"login":"farazghani","display_login":"farazghani","gravatar_id":"","url":"https://api.github.com/users/farazghani","avatar_url":"https://avatars.githubusercontent.com/u/49764726?"},"repo":{"id":1233130963,"name":"farazghani/multiprovider_chatbot","url":"https://api.github.com/repos/farazghani/multiprovider_chatbot"},"payload":{"repository_id":1233130963,"push_id":34872209580,"ref":"refs/heads/main","head":"650ebea1644a1b8655b857ab1b23e7998401ba43","before":"2a8e0954beda96cf8eace756ae69a0e21aa085df"},"public":true,"created_at":"2026-05-30T12:56:14Z"},
{"id":"10080838086","type":"WatchEvent","actor":{"id":49764726,"login":"farazghani","display_login":"farazghani","gravatar_id":"","url":"https://api.github.com/users/farazghani","avatar_url":"https://avatars.githubusercontent.com/u/49764726?"},"repo":{"id":274360069,"name":"BusKill/buskill-app","url":"https://api.github.com/repos/BusKill/buskill-app"},"payload":{"action":"started"},"public":true,"created_at":"2026-05-30T10:44:20Z","org":{"id":60920960,"login":"BusKill","gravatar_id":"","url":"https://api.github.com/orgs/BusKill","avatar_url":"https://avatars.githubusercontent.com/u/60920960?"}}]
"""
