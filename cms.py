import re
import sys

from markdown2 import Markdown
markdowner = Markdown(extras=[
        "markdown-in-html",
        "strike",
        "tables"
    ])

class Cms():
    def __init__(self, html_path, markdown=False):
        self.html_path = html_path

        self.load()
        self.process(markdown)

    def load(self):
        # Read to memory
        with open(self.html_path, "r") as exercise_reader:
            self.html_raw_text = exercise_reader.read()

        # Remove metadata from HTML
        self.html_raw_text = re.sub(r"<toledo course=\".*?\" content=\".*?\" title=\".*?\">", "", self.html_raw_text)

    def process(self, markdown=False):
        print("Preprocessing")

        if markdown:
            self.html_raw_text = re.sub(r"<div ", "<div markdown='1' ", self.html_raw_text)
            self.html_raw_text = re.sub(r" -- ", " — ", self.html_raw_text)
            self.html_raw_text = markdowner.convert(self.html_raw_text).replace("em>", "i>")

        self.html_raw_text = re.sub(r"<table>", "<table style=\"margin-top: 1em; margin-bottom: 1em !important; table-layout: fixed; border-collapse: collapse; empty-cells: hide; text-align: center; width: 100%; text-align: center !important;\">", self.html_raw_text)
        self.html_raw_text = re.sub(r"<caption", "<caption style=\"padding: 0.5em; font-weight: bold;\"", self.html_raw_text)
        self.html_raw_text = re.sub(r"<th>", "<th style=\"background-color: #00407a; vertical-align: middle; padding: 0.5em; border: 1px solid #ffffff; color: #ffffff; text-align: center;\">", self.html_raw_text)
        self.html_raw_text = re.sub(r"<td", "<td style=\"text-align: center !important;  border: 1px solid #ffffff;background-color: #eeeeee; vertical-align: middle; padding: 0.5em;\"", self.html_raw_text)
        self.html_raw_text = re.sub(r"<audio", "<audio style=\"width: 100%;\"", self.html_raw_text)
        self.html_raw_text = re.sub(r"<video", "<video style=\"width: 100% !important; height: auto !important;\"", self.html_raw_text)
        self.html_raw_text = re.sub(r" \!", "!", self.html_raw_text)
        self.html_raw_text = re.sub(r" \?", "?", self.html_raw_text)
        self.html_raw_text = re.sub(r" :", ":", self.html_raw_text)
        self.html_raw_text = re.sub(r"<h3>", "<h3 style=\"color: #00407a; font-size: 2em;; margin-bottom: 0.5em !important;\">", self.html_raw_text)
        self.html_raw_text = re.sub(r"<h4>", "<h4 style=\"color: #00407a; font-size: x-large; margin-bottom: 0.5em !important;\">", self.html_raw_text)
        self.html_raw_text = re.sub(r"<h5>", "<h5 style=\"color: #00407a; margin-bottom: 0.5em !important;\">", self.html_raw_text)
        self.html_raw_text = re.sub(r"<p>", "<p style=\"margin-bottom: 1em !important; text-align: justify;\">", self.html_raw_text)
        self.html_raw_text = re.sub(r"<p>", "<p style=\"margin-bottom: 1em !important; text-align: justify;\">", self.html_raw_text)
        self.html_raw_text = re.sub(r"<hr>", "<hr style=\"margin-top: 1rem; margin-bottom: 0; border: none; box-sizing: border-box; width: 100%; height: 2px; background-color: #00407a;\">", self.html_raw_text)
        self.html_raw_text = re.sub(r"<img", "<img style=\"margin-bottom: 1em;\"", self.html_raw_text)
        self.html_raw_text = re.sub(r"<div class=\"accolade\">", "<div style=\"margin-bottom: 2em; border-left-width: 2px; border-left-style: solid; box-sizing: border-box; padding-left: 1em; border-color: #00407a;\">", self.html_raw_text)
        #self.html_raw_text = "<div style=\"line-height: 160%;\">" + self.html_raw_text + "</div>"  # AN
        self.html_raw_text = "<div style=\"padding-left: 15%; padding-right: 15%; line-height: 160%;\">" + self.html_raw_text + "</div>" # PRONUNCIATION