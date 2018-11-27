import linecache
def client_id():
    file = open('id.txt', 'r')
    second_line = linecache.getline('id.txt', 1)
    actual_line = second_line.strip()
    file.close()
    return actual_line

def secret_id():
    file = open('id.txt', 'r')
    second_line = linecache.getline('id.txt', 2)
    actual_line = second_line.strip()
    file.close()
    return actual_line

def discord_token():
    file = open('id.txt', 'r')
    second_line = linecache.getline('id.txt', 3)
    actual_line = second_line.strip()
    file.close()
    return actual_line