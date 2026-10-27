"""Regression checks for catalog behavior and security fixes."""

import contextlib
import io
from pathlib import Path
import subprocess
import sys
import unittest

import museum_catalog as catalog


class CatalogTests(unittest.TestCase):
    """Use an empty catalog for each independent behavior check."""

    def setUp(self):
        catalog.conn.execute("DELETE FROM artifacts")
        catalog.conn.commit()

    def test_quoted_and_sql_like_titles_are_literal_data(self):
        titles = [
            "Curator's Mirror",
            "x', 'era', 0, 0); DROP TABLE artifacts; --",
        ]
        for title in titles:
            catalog.add_artifact(title, "King's Era", 50)
        rows = catalog.conn.execute(
            "SELECT title, era FROM artifacts ORDER BY id"
        ).fetchall()
        self.assertEqual(rows, [(title, "King's Era") for title in titles])

    def test_storage_to_display_transition(self):
        catalog.add_artifact("Mirror", "Chola", 120000)
        self.assertEqual(catalog.display_status(1), "in storage")
        catalog.move_to_display(1)
        self.assertEqual(catalog.display_status(1), "on display")

    def test_initial_display_flag(self):
        catalog.add_artifact("Manuscript", "Vijayanagara", 80000, 1)
        self.assertEqual(catalog.display_status(1), "on display")

    def test_totals_filter_by_era_and_handle_no_matches(self):
        catalog.add_artifact("Mirror", "Chola", 120000)
        catalog.add_artifact("Lamp", "Chola", 15000)
        catalog.add_artifact("Manuscript", "Vijayanagara", 80000, 1)
        self.assertEqual(catalog.total_value("Chola"), 135000)
        self.assertEqual(catalog.total_value("Unknown"), 0)

    def test_missing_artifact_has_clear_error(self):
        with self.assertRaisesRegex(ValueError, "Unknown artifact ID: 999"):
            catalog.display_status(999)

    def test_backup_notice(self):
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            catalog.backup_note()
        self.assertEqual(output.getvalue(), "catalog backup complete\n")

    def test_import_has_no_demo_side_effects(self):
        result = subprocess.run(
            [sys.executable, "-c", (
                "import museum_catalog as m; "
                "print(m.conn.execute("
                "'SELECT COUNT(*) FROM artifacts').fetchone()[0])"
            )],
            cwd=Path(__file__).resolve().parent,
            capture_output=True,
            text=True,
            check=True,
        )
        self.assertEqual(result.stdout, "0\n")
        self.assertEqual(result.stderr, "")


if __name__ == "__main__":
    unittest.main()
