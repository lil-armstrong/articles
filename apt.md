# APT key vs GPG
Except of using `apt-key del` in maintainer scripts, the use of `apt-key` is deprecated. 
If your existing use of apt-key add looks like this:

```bash
wget -qO- https://myrepo.example/myrepo.asc | sudo apt-key add -
```
Then you can directly replace this with (though note the recommendation below):

```bash
wget -qO- https://myrepo.example/myrepo.asc | sudo tee /etc/apt/trusted.gpg.d/myrepo.asc
```
