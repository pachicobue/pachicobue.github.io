import subprocess
import datetime
import argparse
import json
from pathlib import Path
from typing import *

_this_script_dir: Path = Path(__file__).parent

_data_dir: Path = _this_script_dir.parent / "data"
_json_path: Path = _data_dir / "library/src_stats.json"

_content_dir: Path = _this_script_dir.parent / "content"
_library_dir: Path = _content_dir / "library"
_blog_dir: Path = _content_dir / "blog"
_article_dir: Path = _content_dir / "article"


def new_article(name: str):
    command: List[str] = ["hugo", "new", "--kind", "article", "article/{}".format(name)]
    subprocess.check_call(command)


def new_blog():
    date_str: str = datetime.date.today().strftime("%Y-%m-%d")
    command: List[str] = ["hugo", "new", "--kind", "blog", "blog/{}".format(date_str)]
    subprocess.check_call(command)


def _install_index_md(dir: Path):
    d: Path = dir.parent
    while d.is_relative_to(_library_dir) and d != _library_dir:
        if not (d / "index.md").exists():
            md_path = d / "_index.md"
            with open(md_path, "w") as f:
                f.writelines(
                    [
                        "+++\n",
                        'title = "{}"\n'.format(d.relative_to(_library_dir)),
                        "+++\n",
                    ]
                )
        d = d.parent


def _create_lib(name: str) -> None:
    dir = _library_dir / name
    _install_index_md(dir)
    if not dir.exists():
        command: List[str] = [
            "hugo",
            "new",
            "--kind",
            "library",
            "library/{}".format(name),
        ]
        subprocess.check_call(command)


def new_lib(all: bool, name: Optional[str]) -> None:
    if all:
        with open(_json_path) as f:
            dict: Dict[str, Any] = json.load(f)
            for key in dict.keys():
                path: Path = Path(key)
                _create_lib(str(path.parent / path.stem))
    else:
        assert name
        _create_lib(name)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Hugo new???wrapper")
    subparser = parser.add_subparsers(dest="subcommand")

    parser_article = subparser.add_parser("article", help="article???????????????")
    parser_article.add_argument("name", help="?????????")

    parser_blog = subparser.add_parser("blog", help="blog???????????????")

    parser_library = subparser.add_parser("lib", help="library???????????????")
    parser_library.add_argument("--all", action="store_true", help="???????????????????????????????????????")
    parser_library.add_argument(
        "--name", help="????????????????????? src/?????????????????????(ex. `algorithm/mo`)"
    )

    args = parser.parse_args()
    if args.subcommand == "article":
        print(args.name)
        new_article(args.name)
    elif args.subcommand == "blog":
        new_blog()
    elif args.subcommand == "lib":
        new_lib(args.all, args.name)
    else:
        parser.print_help()
