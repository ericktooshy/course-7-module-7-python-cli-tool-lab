import argparse
from lib.models import Task, User

users = {}

def handle_add_task(args):
    username = args.username
    title = args.title
    if username not in users:
        users[username] = User(username)
    user = users[username]
    user.add_task(title)

def main():
    parser = argparse.ArgumentParser(description="CLI Task Manager")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # Subparser for add-task
    add_parser = subparsers.add_parser("add-task", help="Add a task for a user")
    add_parser.add_argument("username", type=str)
    add_parser.add_argument("title", type=str)
    add_parser.set_defaults(func=handle_add_task)

    args = parser.parse_args()
    if hasattr(args, "func"):
        args.func(args)

if __name__ == "__main__":
    main()
