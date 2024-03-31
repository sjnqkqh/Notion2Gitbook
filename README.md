# Notion_to_gitbook

### 노션에서 한글로 작성한 문서를 Gitbook으로 옮기는 일은 불편합니다.

도서나 레퍼런스 문서에서 클립보드에 캡처한 내용을 노션에 옮기는 일은 매우 쉽습니다. 그냥 **붙여넣기** 하면 됩니다. 노션은 정말 잘 만든 에디터이자 데이터베이스니까요.

하지만 gitbook에서 직접 문서를 작성하거나, 노션에서 적은 문서를 Github이나 Gitbook에 옮기는 일은 매우 귀찮습니다. Markdown이나 Zip으로 import해도 인코딩 문제로 인해 추가적인 수정을 하거나, 노션에 이미 작성한 이미지를 다시 캡쳐해서 Gitbook에 옮겨야합니다. 게다가 Gitbook 에디터의 문제로 인해 한글로는 이미지 캡션을 원활하게 작성할 수도 없습니다. 

해당 레포지토리는 이런 불편을 해소하기 위해 만들어졌습니다. 단일 페이지 혹은 하나의 계층 구조로 작성된 N개의 페이지를 편리하게 추출하고, `SUMMARY.md` 파일을 생성하여 Gitbook 레파지토리 폴더에 업로드하기 간단하도록 구현했습니다.

사용을 위해선 추출하려는 Notion 문서에 연결 설정에서 Notion API가 연결되어 있어야하며, 환경변수 혹은 `dotenv`를 통해 `NOTION_TOKEN`이 정의되어 있어야 합니다.

해당 레포지토리는 **notion2md**([https://github.com/echo724/notion2md](https://github.com/echo724/notion2md))과 **notion-sdk-py(**[https://github.com/ramnes/notion-sdk-py](https://github.com/ramnes/notion-sdk-py)**)** 를 기반으로 제작되었으며, [MIT](https://choosealicense.com/licenses/mit/) 라이센스를 따릅니다.

---

### It's inconvenient to move documents written in Korean from a notion to Gitbook.

It's very easy to move clipboard captures from books or reference documents into Notion - just **paste** them in. Notion is a really good editor and database.

However, it's very cumbersome to write documentation directly in gitbook, or to move documentation from Notion to Github or Gitbook. Even if you import it as Markdown or Zip, you have to make additional edits due to encoding issues, or recapture images you've already created in notions and move them to Gitbook. On top of that, you can't write image captions in Korean smoothly due to issues with the Gitbook editor.

This repository was created to solve these inconveniences by making it easy to extract a single page or N pages in a hierarchical structure, generate a `SUMMARY.md` file, and upload it to the Gitbook repository folder.

To use it, the Notion document you want to extract must have the Notion API connected in the connection settings and have `NOTION_TOKEN` defined as an environment variable or via `dotenv`.

This repository is based on **notion2md** ([https://github.com/echo724/notion2md](https://github.com/echo724/notion2md)) and **notion-sdk-py (**[https://github.com/ramnes/notion-sdk-py**](https://github.com/ramnes/notion-sdk-py**)), and is licensed under the [MIT](https://choosealicense.com/licenses/mit/) license.