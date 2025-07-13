# ZeroBone's website

Installation:

First, Ruby is to be installed. Then we need to install dependencies.

```bash
bundle install
bundle add csv
bundle add logger
bundle add base64
bundle add bigdecimal
bundle update
```

After that the website can be served on a local webserver using

```bash
set JEKYLL_ENV=development
bundle exec jekyll serve
```

and built for production using

```bash
set JEKYLL_ENV=production
bundle exec jekyll build
```