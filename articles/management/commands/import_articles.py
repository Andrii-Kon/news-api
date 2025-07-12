import os
import sqlite3
from django.core.management.base import BaseCommand, CommandError
from articles.models import Article

class Command(BaseCommand):
    """
    A Django management command to import articles from a legacy SQLite database
    into the current Django project's database.

    This command is designed for a one-time data migration from the previous
    'news-analyzer' project. It prevents duplicate entries by checking the URL.

    Usage: python manage.py import_articles
    """
    help = 'Imports articles from the old news.db into the new Django project'

    def handle(self, *args, **options):
        """The main logic for the command."""
        # Define the path to the legacy database file.
        # This assumes the old project is located on the user's Desktop.
        # Note: This path may need adjustment depending on the user's setup.
        try:
            old_db_path = os.path.join(os.path.expanduser("~"), "Desktop", "news-analyzer", "news.db")

            if not os.path.exists(old_db_path):
                raise CommandError(f"Legacy database not found at the expected path: {old_db_path}")

            self.stdout.write(f"Connecting to legacy database at: {old_db_path}")
            conn_old = sqlite3.connect(old_db_path)
            cursor_old = conn_old.cursor()

            # Fetch all necessary data from the old 'articles' table.
            cursor_old.execute("SELECT title, url, summary FROM articles")
            legacy_articles = cursor_old.fetchall()
            conn_old.close()

            if not legacy_articles:
                self.stdout.write(self.style.WARNING("No articles found in the legacy database. Nothing to import."))
                return

            self.stdout.write(f"Found {len(legacy_articles)} articles in the legacy database. Starting import...")

            imported_count = 0
            skipped_count = 0

            # Iterate through legacy articles and import them if they don't already exist.
            for title, url, summary in legacy_articles:
                # Use get_or_create to efficiently prevent duplicate entries based on the 'url' field.
                # 'defaults' are only used if a new object is created.
                _, created = Article.objects.get_or_create(
                    url=url,
                    defaults={'title': title, 'summary': summary}
                )

                if created:
                    imported_count += 1
                else:
                    skipped_count += 1

            self.stdout.write(self.style.SUCCESS(
                f"Import complete. Successfully imported {imported_count} new articles. "
                f"Skipped {skipped_count} existing articles."
            ))

        except sqlite3.Error as e:
            raise CommandError(f"An error occurred while accessing the legacy SQLite database: {e}")
        except Exception as e:
            raise CommandError(f"An unexpected error occurred: {e}")