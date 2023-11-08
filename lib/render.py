import os
from os.path import isdir, isfile, abspath, curdir
from pathlib import Path, PosixPath
from typing import List, Dict


class HTMLRenderer:
    """
    Render swagger JSON to HTML files for HTTP serving
    """

    def __init__(self, specs: List) -> None:
        self.parent_path = Path(abspath(curdir))
        self.html_path = Path(self.parent_path / "html")
        self.specs = specs
        self.os = os

        if not isdir(self.html_path):
            self.os.mkdir(self.html_path)

    def _html_exists(self, html_file: PosixPath) -> bool:
        return isfile(html_file)

    def generate(self) -> None:
        """
        Generates HTML file(s) from loaded swagger specs
        """
        for spec in self.specs:
            try:
                for k, v in spec.items():
                    name = k
                    path = Path(self.html_path / f"{name}.html")
                    if not self._html_exists(html_file=path):
                        with open(path, "a") as f:
                            f.write(self.to_html(v))
                            print(f"[*] Wrote new HTML file for: {path.stem}.json")
            except AttributeError as e:
                # Ignore the errors as we don't want to do anything
                pass

    def to_html(self, spec: str(dict)) -> str:
        """
        Convert Swagger JSON to HTML
        """
        return (
            """
            <!DOCTYPE html>
            <html lang="en">
                <head>
                    <meta charset="UTF-8">
                    <title>Swagger UI</title>
                    <link href="https://fonts.googleapis.com/css?family=Open+Sans:400,700|Source+Code+Pro:300,600|Titillium+Web:400,600,700" rel="stylesheet">
                    <link rel="stylesheet" type="text/css" href="https://cdnjs.cloudflare.com/ajax/libs/swagger-ui/3.43.0/swagger-ui.css" >
                    <style>
                        html
                        {
                        box-sizing: border-box;
                        overflow: -moz-scrollbars-vertical;
                        overflow-y: scroll;
                        }
                        *,
                        *:before,
                        *:after
                        {
                        box-sizing: inherit;
                        }
                        body {
                        margin:0;
                        background: #fafafa;
                        }
                    </style>
                </head>
                <body>
                    <div id="swagger-ui"></div>
                    <script src="https://cdnjs.cloudflare.com/ajax/libs/swagger-ui/3.43.0/swagger-ui-bundle.js"> </script>
                    <script src="https://cdnjs.cloudflare.com/ajax/libs/swagger-ui/3.43.0/swagger-ui-standalone-preset.js"> </script>
                    <script>
                    window.onload = function() {
                    var spec = %s;
                    // Build a system
                    const ui = SwaggerUIBundle({
                        spec: spec,
                        dom_id: '#swagger-ui',
                        deepLinking: true,
                        presets: [
                        SwaggerUIBundle.presets.apis,
                        SwaggerUIStandalonePreset
                        ],
                        plugins: [
                        SwaggerUIBundle.plugins.DownloadUrl
                        ],
                        layout: "StandaloneLayout"
                    })
                    window.ui = ui
                    }
                    </script>
                </body>
            </html>
        """
            % spec
        )
