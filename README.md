# Toledo Markdown Renderer

A Markdown renderer for use with the KU Leuven Toledo environment

## What is Toledo Markdown Renderer?

This Python script can process a Markdown file (or an HTML file, if you want) to automatically apply proper styling to it. The script does this by adding styling elements to each eligible element separately. Unfortunately, the KU Leuven Toledo environment does not support CSS styling, so this HTML 1.0 practise. Because it is tedious, however, I decided to automate it for myself and my lovely colleagues.

## How to use Toledo Markdown Renderer?

### For normal people

Simply drag your Markdown (with extension `.md`) or HTML (with extension `.html`) file onto the Toledo Markdown Renderer binary. The program will process the file automatically.

### For nerds

1. `git clone "https://github.com/AntheSevenants/toledo-markdown-renderer.git"`
1. `pip install -r "requirements.txt"`
1. `python toledo-markdown-renderer.py "input_file.md"`