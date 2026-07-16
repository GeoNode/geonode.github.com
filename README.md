# geonode.org

Source for the [GeoNode](https://geonode.org) project website, a static site built with [Jekyll](https://jekyllrb.com/) and served at [geonode.org](https://geonode.org).

## How it's published

The site is built and deployed automatically by GitHub Actions (`.github/workflows/jekyll.yml`): every push to the `master` branch runs `jekyll build` and deploys the result to GitHub Pages. There is no manual publish step — merging to `master` is what ships the site.

The build uses the gems pinned in this repo's `Gemfile`. The site tracks the [`github-pages`](https://github.com/github/pages-gem) gem, which keeps Jekyll and its plugins aligned with what GitHub Pages supports (currently Jekyll 3.x).

## Local development

You can run the site either with Docker (no Ruby toolchain needed on your machine) or with a native Ruby setup.

### Option A — Docker (recommended)

Build the image once:

```bash
docker build -t geonode-site .
```

Serve the site at <http://localhost:4000>:

```bash
docker run --rm -p 4000:4000 geonode-site
```

Serve with live-reload while editing, by mounting the working tree:

```bash
docker run --rm -p 4000:4000 -v "$PWD":/site geonode-site
```

Build only and extract the generated static site to `./_site` (no server):

```bash
docker run --rm -v "$PWD":/site geonode-site bundle exec jekyll build
```

> On Linux/WSL the generated files are owned by `root`. To have them owned by
> your user, add `--user "$(id -u):$(id -g)"` to the `docker run` command.

### Option B — Native Ruby

Install the prerequisites (Debian/Ubuntu example):

```bash
sudo apt-get install ruby-full build-essential zlib1g-dev
```

If gems fail to install globally, install them under your home directory:

```bash
echo '# Install Ruby gems to ~/gems' >> ~/.bashrc
echo 'export GEM_HOME="$HOME/gems"' >> ~/.bashrc
echo 'export PATH="$HOME/gems/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc
```

Install the project gems and serve the site:

```bash
gem install bundler
bundle install
bundle exec jekyll serve   # default port 4000; override with -P <port>
```

View at <http://localhost:4000>.

## Writing a blog post

Drafts live in `_drafts/` and are excluded from production builds.

1. Create the draft and set its YAML front matter:

   ```bash
   cd _drafts
   vi newpost.md
   ```

   ```yaml
   ---
   layout: base
   ---
   ```

2. Preview drafts (they show up as the latest post):

   ```bash
   bundle exec jekyll serve --drafts
   # or, with Docker:
   docker run --rm -p 4000:4000 -v "$PWD":/site geonode-site \
     bundle exec jekyll serve --host 0.0.0.0 --drafts
   ```

3. When ready to publish, move the draft into `_posts/` with a dated filename:

   ```bash
   git mv _drafts/newpost.md _posts/YYYY-MM-DD-newpost.md
   vi _posts/YYYY-MM-DD-newpost.md
   ```

4. Commit and push to `master` — the GitHub Actions workflow builds and
   deploys the site automatically:

   ```bash
   git commit -am 'publish article'
   git push origin master
   ```
