import subprocess
import sys
import tempfile
from pathlib import Path
import unittest

from check_relative_links import LinkChecker


class LinkCheckerTests(unittest.TestCase):
    def test_relative_links_in_html_and_image_maps(self):
        checker = LinkChecker()
        checker.feed('<a href="open-opportunities">Open Positions</a>\n'
                     '<a href="../page">Parent</a><area href="./page">'
                     '<a href=projects/fishsense>Project</a>')
        self.assertEqual(checker.errors, [(1, "open-opportunities"),
                         (2, "../page"), (2, "./page"), (2, "projects/fishsense")])

    def test_valid_links_and_non_hyperlinks(self):
        checker = LinkChecker()
        for href in ["/page", "//example.com/page", "https://example.com", "#section",
                     "?page=2", "mailto:e4e@ucsd.edu", "tel:+15555555555", ""]:
            checker.feed(f'<a href="{href}">Link</a>')
        checker.feed('<a id="anchor"></a><!-- <a href="bad"> -->'
                     '<img src="assets/photo.jpg"><link href="assets/style.css">')
        self.assertEqual(checker.errors, [])

    def test_command_exit_status_and_diagnostics(self):
        script = Path(__file__).with_name("check_relative_links.py")
        with tempfile.TemporaryDirectory() as directory:
            command = [sys.executable, str(script), directory]
            self.assertNotEqual(subprocess.run(command, capture_output=True).returncode, 0)
            page = Path(directory) / "nested.html"
            page.write_text('<a href="open-opportunities">Open Positions</a>')
            result = subprocess.run(command, capture_output=True, text=True)
            self.assertEqual(result.returncode, 1)
            self.assertIn("nested.html:1:", result.stderr)
            self.assertIn("open-opportunities", result.stderr)
            page.write_text('<a href="/open-opportunities">Open Positions</a>')
            self.assertEqual(subprocess.run(command, capture_output=True).returncode, 0)


if __name__ == "__main__":
    unittest.main()
