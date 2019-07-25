# chrisfleisch.github.io

```
brew install ruby
echo 'export PATH="/usr/local/lib/ruby/gems/2.6.0/bin:/usr/local/opt/ruby/bin:$PATH"' >> ~/.bash_profile
source ~/.bash_profile
gem install jekyll bundler
bundle install  # may need to remove Gemfile.lock
```

Start up server in code directory (pwd cannot have spaces or special characters in it)
```
bundle exec jekyll serve
```

To get photos from flickr setup python env
```
conda create -n chrisfleisch python=3.6 pip
conda activate chrisfleisch
pip install -r scripts/reqs.txt
```

Run get photos
```
python scripts/get_photos.py
```

Update Jekyll
```
bundle update
```
