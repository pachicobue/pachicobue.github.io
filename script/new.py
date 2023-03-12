import pathlib
import subprocess
import datetime
import argparse


def new_blog():
    date_str = datetime.date.today().strftime("%Y-%m-%d")
    command = ["hugo", "new", "--kind", "blog", "blog/{}".format(date_str)]
    subprocess.check_call(command)


def new_lib(name):
    command = ["hugo", "new", "--kind", "library", "library/{}".format(name)]
    subprocess.check_call(command)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Hugo newのwrapper")
    subparser = parser.add_subparsers(dest="subcommand")

    parser_blog = subparser.add_parser("blog", help="blog記事の追加")
    parser_blog.set_defaults(handler=new_blog)

    parser_library = subparser.add_parser("lib", help="library記事の追加")
    parser_library.add_argument("name", help="src/からの相対パス(ex. `algorithm/mo`)")
    parser_library.set_defaults(handler=new_lib)

    args = parser.parse_args()
    if args.subcommand == "blog":
        new_blog()
    elif args.subcommand == "lib":
        new_lib(args.name)
    else:
        parser.print_help()
