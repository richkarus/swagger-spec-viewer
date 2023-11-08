
# Swagger Spec Viewer

The main motiviation around having this project was I never felt comfortable uploading Swagger JSON specs to an external web service as this could divulge too much information about how my API is formed and I would rather keep that to myself.

Therefore, I went around looking for an OSS solution that would allow me to spin up a local HTTP server after rendering the HTML files. I was unable to find something that would fit the bill, so I decided to go and make this project.

The application will detect any new swagger files and will render only those new additions, rather than wasting cycles on re-rendering everything again.

Main benefits of this are:

- Local HTTP server, no more having to upload your specs to an external service
- Rendering of SwaggerUI HTML files

Caveats:
- Only tested on Swagger 2.0 specs, your mileage may vary.
- Uses HTTPServer, as this is something that should ideally be run locally out of production-grade environments. This is designed to be local-only.



## Contributing

Contributions are always welcome!



## Usage/Examples

Starting is simple, just run:

```
python3 main.py
```


## Installation

- You will need to create `specs` (app creates the folder for you on first run) folder and populate this folder with your JSON swagger files. 

