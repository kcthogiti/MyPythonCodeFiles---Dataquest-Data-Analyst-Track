## 2. Authenticating with the API ##

headers = {"Authorization": "bearer 13426216-4U1ckno9J5AiK72VRbpEeBaMSKk", "User-Agent": "Dataquest/1.0"}

params = {"t": "day"}
response = requests.get("https://oauth.reddit.com/r/python/top", headers = headers, params = params)

python_top = response.json()


## 3. Getting the Most Upvoted Post ##


python_top_articles = python_top["data"]["children"]

print(python_top_articles)
counter = 0
for elem in python_top_articles:
    a = elem["data"]["ups"]
    if a > counter:
        most_upvoted = elem["data"]["id"]
        counter = a

## 4. Getting Post Comments ##

params = {"subreddit":"python", "article":"4b7w9u"}
headers = {"Authorization": "bearer 13426216-4U1ckno9J5AiK72VRbpEeBaMSKk", "User-Agent": "Dataquest/1.0"}
response = requests.get("https://oauth.reddit.com/r/python/comments/4b7w9u", headers = headers)

comments = response.json()


## 5. Getting the Most Upvoted Comment ##

comments_list = comments[1:len(comments)]
counter = 0

for elem in comments_list:
    ls = elem["data"]["children"]
    for row in ls:
        a = row["data"]["ups"]
        if a > counter:
            counter = a
            most_upvoted_comment = row["data"]["id"]


## 6. Upvoting a Comment ##

payload = {"dir":1, "id":"d16y4ry"}
headers = {"Authorization": "bearer 13426216-4U1ckno9J5AiK72VRbpEeBaMSKk", "User-Agent": "Dataquest/1.0"}
response = requests.post("https://oauth.reddit.com/api/vote", json = payload, headers = headers)

status = response.status_code