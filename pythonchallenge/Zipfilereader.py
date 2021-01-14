import zipfile, re

file = zipfile.ZipFile("channel.zip")

num = '90052'
comments = []
while True:
    content = file.read(num + ".txt").decode("utf-8")
    comments.append(file.getinfo(num + ".txt").comment.decode("utf-8"))
    match = re.search("Next nothing is (\d+)", content)
    if match == None:
        break
    num = match.group(1)

print("".join(comments))