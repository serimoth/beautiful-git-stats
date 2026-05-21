"""
Git repository analyzer
"""

from git import Repo
from datetime import datetime
from collections import defaultdict
from pathlib import Path


class GitAnalyzer:
    """Analyze Git repository statistics"""

    def __init__(self, repo_path='.'):
        """Initialize analyzer with repository path"""
        self.repo = Repo(repo_path)
        if self.repo.bare:
            raise ValueError("Cannot analyze bare repository")

    def get_summary(self, author=None, since=None, until=None):
        """Get repository summary statistics"""
        commits = list(self.repo.iter_commits(author=author, since=since, until=until))

        if not commits:
            return {
                'total_commits': 0,
                'total_authors': 0,
                'total_files': 0,
                'lines_added': 0,
                'lines_deleted': 0,
                'first_commit': 'N/A',
                'last_commit': 'N/A',
                'active_days': 0
            }

        authors = set()
        files = set()
        lines_added = 0
        lines_deleted = 0
        active_dates = set()

        for commit in commits:
            authors.add(commit.author.name)
            active_dates.add(datetime.fromtimestamp(commit.committed_date).date())

            # Get stats for this commit
            if commit.parents:
                diffs = commit.parents[0].diff(commit, create_patch=True)
                for diff in diffs:
                    if diff.a_path:
                        files.add(diff.a_path)
                    if diff.b_path:
                        files.add(diff.b_path)

                    # Count line changes
                    if diff.diff:
                        diff_text = diff.diff.decode('utf-8', errors='ignore')
                        for line in diff_text.split('\n'):
                            if line.startswith('+') and not line.startswith('+++'):
                                lines_added += 1
                            elif line.startswith('-') and not line.startswith('---'):
                                lines_deleted += 1

        first_commit = datetime.fromtimestamp(commits[-1].committed_date).strftime('%Y-%m-%d')
        last_commit = datetime.fromtimestamp(commits[0].committed_date).strftime('%Y-%m-%d')

        return {
            'total_commits': len(commits),
            'total_authors': len(authors),
            'total_files': len(files),
            'lines_added': lines_added,
            'lines_deleted': lines_deleted,
            'first_commit': first_commit,
            'last_commit': last_commit,
            'active_days': len(active_dates)
        }

    def get_contributors(self, limit=10):
        """Get top contributors by commit count"""
        contributors = defaultdict(lambda: {'commits': 0, 'additions': 0, 'deletions': 0})

        for commit in self.repo.iter_commits():
            author = commit.author.name
            contributors[author]['commits'] += 1

            if commit.parents:
                diffs = commit.parents[0].diff(commit, create_patch=True)
                for diff in diffs:
                    if diff.diff:
                        diff_text = diff.diff.decode('utf-8', errors='ignore')
                        for line in diff_text.split('\n'):
                            if line.startswith('+') and not line.startswith('+++'):
                                contributors[author]['additions'] += 1
                            elif line.startswith('-') and not line.startswith('---'):
                                contributors[author]['deletions'] += 1

        # Sort by commit count
        sorted_contributors = sorted(
            contributors.items(),
            key=lambda x: x[1]['commits'],
            reverse=True
        )[:limit]

        return [
            {
                'author': author,
                'commits': stats['commits'],
                'additions': stats['additions'],
                'deletions': stats['deletions']
            }
            for author, stats in sorted_contributors
        ]

    def get_hotspots(self, limit=10):
        """Get most frequently changed files"""
        file_changes = defaultdict(int)

        for commit in self.repo.iter_commits():
            if commit.parents:
                diffs = commit.parents[0].diff(commit)
                for diff in diffs:
                    if diff.a_path:
                        file_changes[diff.a_path] += 1
                    if diff.b_path and diff.b_path != diff.a_path:
                        file_changes[diff.b_path] += 1

        sorted_files = sorted(
            file_changes.items(),
            key=lambda x: x[1],
            reverse=True
        )[:limit]

        return [
            {'file': file, 'changes': changes}
            for file, changes in sorted_files
        ]

    def get_activity_pattern(self):
        """Get commit activity patterns by day and hour"""
        by_day = defaultdict(int)
        by_hour = defaultdict(int)

        days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

        for commit in self.repo.iter_commits():
            dt = datetime.fromtimestamp(commit.committed_date)
            day_name = days[dt.weekday()]
            by_day[day_name] += 1
            by_hour[dt.hour] += 1

        return {
            'by_day': dict(by_day),
            'by_hour': dict(by_hour)
        }
