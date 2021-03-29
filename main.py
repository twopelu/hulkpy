import sys

# import webview

from hulk import BitbucketManager

print("HULK The Incredible says hi!")

if len(sys.argv) < 3:  # sys.argv[0] is the command itself
    print("HULK usage is: hulk <username> <password>")
    quit(1)

username = sys.argv[1]
password = sys.argv[2]

bb_man = BitbucketManager()
bb_man.setup_client(username, password)
bb_man.list_repos()

# window = webview.create_window("BitBucket", "https://bitbucket.org/twopelu/")
# webview.start()

print("HULK The Incredible says bye!")
