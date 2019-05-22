# chrisfleisch.github.io

```
brew install ruby
echo 'export PATH="/usr/local/lib/ruby/gems/2.6.0/bin:/usr/local/opt/ruby/bin:$PATH"' >> ~/.bash_profile
source ~/.bash_profile
gem install jekyll bundler
bundle install
```

Start up server in code directory (pwd cannot have spaces or special characters in it)
```
bundle exec jekyll serve
```
