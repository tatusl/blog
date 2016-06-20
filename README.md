# My blog + Docker

Dockerized version of my blog for development purposes.

## Build

```
docker build -t name_of_image .
```

## Run

```
docker run -d -p 8888:8000 -v $(pwd)/content:/opt/blog/content name_of_image
```

After adding the content volume, changes to markdown files made in host OS will trigger Pelican to regenerate site inside the Docker container.

Point your browser to localhost:8888 to see the blog.