from argparse import ArgumentParser

if __name__ == '__main__':
    parser = ArgumentParser(description='Command Line Interface to interact with GitLab Issues.')

    subparsers = parser.add_subparsers(title='Commands', dest='command')

    # List issues
    list_parser = subparsers.add_parser('list', help='List all issues')

    # Create new issue
    create_parser = subparsers.add_parser('create', help='Create a new issue')
    create_parser.add_argument('title', help='Title of the issue')
    create_parser.add_argument('--description', help='Description of the issue')
    create_parser.add_argument('--priority', choices=['Low', 'Medium', 'High'], default='Low', help='Priority of the issue')

    # Show issue details
    show_parser = subparsers.add_parser('show', help='Show details of an issue')
    show_parser.add_argument('issue_id', type=int, help='ID of the issue')

    # Close an issue
    close_parser = subparsers.add_parser('close', help='Close an issue')
    close_parser.add_argument('issue_id', type=int, help='ID of the issue')

    # Comment on an issue
    comment_parser = subparsers.add_parser('comment', help='Comment on an issue')
    comment_parser.add_argument('issue_id', type=int, help='ID of the issue')
    comment_parser.add_argument('comment', help='Comment to add')

    # Assign an issue
    assign_parser = subparsers.add_parser('assign', help='Assign an issue to a user')
    assign_parser.add_argument('issue_id', type=int, help='ID of the issue')
    assign_parser.add_argument('assignee_name', help='Name of the assignee')

    args = parser.parse_args()
    print(vars(args))

# # Perform the appropriate action based on the command
# if args.command == 'list':
#     # Logic to list all issues
#     print('Listing all issues...')
# elif args.command == 'create':
#     # Logic to create a new issue
#     print('Creating a new issue with title:', args.title)
#     if args.description:
#         print('Description:', args.description)
#     if args.priority:
#         print('Priority:', args.priority)
# elif args.command == 'show':
#     # Logic to show details of an issue
#     print('Showing details of issue with ID:', args.issue_id)
# elif args.command == 'close':
#     # Logic to close an issue
#     print('Closing issue with ID:', args.issue_id)
# elif args.command == 'comment':
#     # Logic to comment on an issue
#     print('Adding comment to issue with ID:', args.issue_id)
#     print('Comment:', args.comment)
# elif args.command == 'assign':
#     # Logic to assign an issue to a user
#     print('Assigning issue with ID:', args.issue_id, 'to', args.assignee_name)
