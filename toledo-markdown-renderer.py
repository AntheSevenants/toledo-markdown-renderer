import argparse
from pathlib import Path
import os

from cms import Cms

parser = argparse.ArgumentParser(description='Convert Markdown to HTML compatible with KU Leuven Toledo.')
parser.add_argument('input_file', type=str, help='the path to your Markdown file')

args = parser.parse_args()

extension = Path(args.input_file).suffix

if not extension in [ ".html", ".md" ]:
    raise Exception("Input file type not recognised")

if not os.path.exists(args.input_file):
    raise Exception("Input file does not exist")    

is_markdown = extension == ".md"

cms = Cms(args.input_file, is_markdown)

output_path = f"{Path(args.input_file).parent}/{Path(args.input_file).stem}_render.html"

with open(output_path, "wt") as writer:
    writer.write(cms.content)

print("Done")