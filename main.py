import http.server
import socketserver
import argparse


from lib.render import HTMLRenderer
from lib.spec import SpecLoader

specs = SpecLoader()
parser = argparse.ArgumentParser()
parser.add_argument(
    "--render-only",
    help="render html only, no http serving",
    action="store_true",
)
PORT = 8123


def main():
    args = parser.parse_args()
    renderer = HTMLRenderer(specs=specs.load())
    renderer.generate()

    if args.render_only:
        exit(0)

    class Handler(http.server.SimpleHTTPRequestHandler):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, directory=renderer.html_path, **kwargs)

    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print("[+] Started HTTP on Port:", PORT)
        httpd.serve_forever()


if __name__ == "__main__":
    main()
