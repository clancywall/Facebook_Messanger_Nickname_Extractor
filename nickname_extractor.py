import json
import re



# Input and Output fileaddresses
input_filename = "PATH/message.json"
output_filename = "PATH/nicknames.json"

# Nickname messages to match against
nickname_regs = \
    [r'(.*) set the nickname for (.\w+) (.\w+) to (.*)',
     r'(.*) set \w{3} own nickname to (.*)',
     r'(.*) set your nickname to (.*)']

# Put your own name exactly as it appears on Facebook
myself = "John Snow"


def find_owner(con, parts, sender):
    if re.match(nickname_regs[2], content):
        return myself
    for p in parts:
        name = p['name']
        if re.match(rf"(.*) {name} (.*)", con):
            return name
    return sender


# Read file
with open(input_filename, 'r') as file:
    data = file.read()

# Parse file
messages = json.loads(data)['messages']
participants = json.loads(data)['participants']

# Add array to store nicknames to participants
for p in participants:
    p['nicknames'] = []

# Find nicknames
for message in messages:
    if 'content' in message:
        content = message['content']
        for reg in nickname_regs:
            if re.match(reg, content):
                search_group = re.search(reg, content)
                nickname = search_group.group(search_group.lastindex)
                owner = find_owner(content, participants, message['sender_name'])
                # Add nickname
                for p in participants:
                    if p['name'] == owner:
                        p['nicknames'].insert(0, nickname)
                        break
                break

with open(output_filename, 'w', encoding='utf-8') as file:
    json.dump(participants, file, ensure_ascii=False, indent=4)

