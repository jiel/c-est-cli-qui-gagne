from fire import Fire

from enum import Enum

class Priority(Enum):
    Low = 'Low'
    Medium = 'Medium'
    High = 'High'


class Gliss:
    """Command Line Interface to interact with GitLab Issues."""

    def list(self):
        """List all issues."""
        print("Listing all issues.")

    def create(self, title, description=None, priority='Low'):
        valid_priority = Priority(priority) # use an enum to validate the value
        """Create a new issue."""
        print(f"Creating issue: {title}")
        if description:
            print(f"Description: {description}")
        if priority:
            print(f"Priority: {valid_priority.value}")

    def show(self, issue_id):
        """Show details of an issue."""
        print(f"Showing details of issue: {issue_id}")

    def close(self, issue_id):
        """Close an issue."""
        print(f"Closing issue: {issue_id}")

    def comment(self, issue_id, comment):
        """Comment on an issue."""
        print(f"Adding comment to issue {issue_id}: {comment}")

    def assign(self, issue_id, assignee_name):
        """Assign an issue to an assignee."""
        print(f"Assigning issue {issue_id} to {assignee_name}")

if __name__ == '__main__':
    Fire(Gliss)
