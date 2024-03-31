import os

from dotenv import load_dotenv
from notion_client import Client

from notion2md.exporter.block import MarkdownExporter

load_dotenv()
notion = Client(auth=os.environ["NOTION_TOKEN"])


def inject_multiple_pages_by_url(page_url: str):
    page_id = page_url.split('/')[-1].split("-")[-1]
    page = notion.blocks.children.list(page_id)

    for item in page.get('results'):
        if item['has_children']:
            try:
                inject_single_page_by_url(item.get('id').replace("-", ""))
            except Exception as e:  # noqa
                print(e)

    generate_summary_file(page_url)


def inject_single_page_by_url(url: str):
    page_id = url.split('/')[-1].split('-')[-1]

    page_info = notion.pages.retrieve(page_id)
    title = page_info.get('properties').get('title').get('title')[0].get('text').get('content').replace("/", "")

    MarkdownExporter(block_id=page_id, output_path='./result/markdowns', download=True,
                     output_filename=title, unzipped=True).export()


def generate_summary_file(url: str):
    page_id = url.split('/')[-1].split("-")[-1]
    with open(
            os.path.join(
                "./result/SUMMARY.md"
            ),
            "w",
            encoding="utf-8",
    ) as output:
        output.write("# Summary\n\n"
                     "* [Introduction](README.md)\n"
                     )
        child_pages = notion.blocks.children.list(page_id)
        for item in child_pages.get("results"):
            if item['has_children']:
                title = item['child_page']['title'].replace("/", "")
                title = str("* [{}](markdowns/{}.md)\n".format(title, title.replace(" ", "%20")))
                output.write(title)


inject_multiple_pages_by_url("Input your notion page url here")
inject_single_page_by_url("Input your notion page url here")
