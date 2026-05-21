#!/usr/bin/env python3
"""
Git Stats CLI - Beautiful Git repository statistics
"""

import click
from pathlib import Path
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich import box
from .analyzer import GitAnalyzer

console = Console()


@click.group()
@click.version_option(version="1.0.0")
def main():
    """🚀 Git Stats - Beautiful repository statistics in your terminal"""
    pass


@main.command()
@click.argument('path', type=click.Path(exists=True), default='.')
@click.option('--author', '-a', help='Filter by author name')
@click.option('--since', '-s', help='Start date (YYYY-MM-DD)')
@click.option('--until', '-u', help='End date (YYYY-MM-DD)')
def summary(path, author, since, until):
    """Show repository summary statistics"""
    try:
        analyzer = GitAnalyzer(path)
        stats = analyzer.get_summary(author=author, since=since, until=until)

        # Create summary table
        table = Table(title="📊 Repository Summary", box=box.ROUNDED)
        table.add_column("Metric", style="cyan", no_wrap=True)
        table.add_column("Value", style="magenta")

        table.add_row("Total Commits", str(stats['total_commits']))
        table.add_row("Total Authors", str(stats['total_authors']))
        table.add_row("Total Files", str(stats['total_files']))
        table.add_row("Lines Added", f"+{stats['lines_added']:,}", style="green")
        table.add_row("Lines Deleted", f"-{stats['lines_deleted']:,}", style="red")
        table.add_row("First Commit", stats['first_commit'])
        table.add_row("Last Commit", stats['last_commit'])
        table.add_row("Active Days", str(stats['active_days']))

        console.print(table)

    except Exception as e:
        console.print(f"[red]Error: {str(e)}[/red]")


@main.command()
@click.argument('path', type=click.Path(exists=True), default='.')
@click.option('--limit', '-l', default=10, help='Number of top contributors')
def contributors(path, limit):
    """Show top contributors"""
    try:
        analyzer = GitAnalyzer(path)
        contribs = analyzer.get_contributors(limit=limit)

        table = Table(title=f"👥 Top {limit} Contributors", box=box.ROUNDED)
        table.add_column("Rank", style="cyan", justify="right")
        table.add_column("Author", style="green")
        table.add_column("Commits", style="magenta", justify="right")
        table.add_column("Lines Added", style="green", justify="right")
        table.add_column("Lines Deleted", style="red", justify="right")

        for i, contrib in enumerate(contribs, 1):
            table.add_row(
                str(i),
                contrib['author'],
                str(contrib['commits']),
                f"+{contrib['additions']:,}",
                f"-{contrib['deletions']:,}"
            )

        console.print(table)

    except Exception as e:
        console.print(f"[red]Error: {str(e)}[/red]")


@main.command()
@click.argument('path', type=click.Path(exists=True), default='.')
@click.option('--limit', '-l', default=10, help='Number of files to show')
def hotspots(path, limit):
    """Show most frequently changed files"""
    try:
        analyzer = GitAnalyzer(path)
        files = analyzer.get_hotspots(limit=limit)

        table = Table(title=f"🔥 Top {limit} Hotspots", box=box.ROUNDED)
        table.add_column("Rank", style="cyan", justify="right")
        table.add_column("File", style="yellow")
        table.add_column("Changes", style="magenta", justify="right")

        for i, file_info in enumerate(files, 1):
            table.add_row(
                str(i),
                file_info['file'],
                str(file_info['changes'])
            )

        console.print(table)

    except Exception as e:
        console.print(f"[red]Error: {str(e)}[/red]")


@main.command()
@click.argument('path', type=click.Path(exists=True), default='.')
def activity(path):
    """Show commit activity by day of week and hour"""
    try:
        analyzer = GitAnalyzer(path)
        activity_data = analyzer.get_activity_pattern()

        # Day of week activity
        day_table = Table(title="📅 Activity by Day of Week", box=box.ROUNDED)
        day_table.add_column("Day", style="cyan")
        day_table.add_column("Commits", style="magenta", justify="right")
        day_table.add_column("Activity", style="green")

        days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        max_commits = max(activity_data['by_day'].values()) if activity_data['by_day'] else 1

        for day in days:
            commits = activity_data['by_day'].get(day, 0)
            bar_length = int((commits / max_commits) * 30) if max_commits > 0 else 0
            bar = "█" * bar_length
            day_table.add_row(day, str(commits), bar)

        console.print(day_table)

        # Hour activity
        hour_table = Table(title="⏰ Activity by Hour", box=box.ROUNDED)
        hour_table.add_column("Hour", style="cyan")
        hour_table.add_column("Commits", style="magenta", justify="right")
        hour_table.add_column("Activity", style="green")

        max_hour_commits = max(activity_data['by_hour'].values()) if activity_data['by_hour'] else 1

        for hour in range(24):
            commits = activity_data['by_hour'].get(hour, 0)
            bar_length = int((commits / max_hour_commits) * 30) if max_hour_commits > 0 else 0
            bar = "█" * bar_length
            hour_table.add_row(f"{hour:02d}:00", str(commits), bar)

        console.print(hour_table)

    except Exception as e:
        console.print(f"[red]Error: {str(e)}[/red]")


if __name__ == '__main__':
    main()
