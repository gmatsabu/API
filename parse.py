import requests

headers ={
      'Authorization': 'token token', # replace <TOKEN> with your token
          }

response = requests.get('https://api.github.com/users/gmatsabu/received_events', headers=headers) # replace <username> with your user name
data = response.json()
event_actions = {'WatchEvent': 'starred', 'PushEvent': 'pushed to'}

for event in data:
  if event['type'] in event_actions:
    name = event['actor']['display_login']
    action = event_actions[event['type']] 
    repo = event['repo']['name'] 
    print('{name} {action} {repo}'.format(name=name, action=action, repo=repo))

  if event['type'] == 'ForkEvent':
    name = event['actor']['display_login']
    repo = event['repo']['name']  
    forked_repo = event['payload']['forkee']['full_name'] 
    print('{name} forked {forked_repo} from {repo}'.format(name=name, forked_repo=forked_repo,repo=repo))