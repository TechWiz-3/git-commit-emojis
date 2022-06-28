# Git Commit Emojis

![Image](https://img.shields.io/github/license/TechWiz-3/git-commit-emojis?color=blue&label=license&logo=gnu&style=flat-square)
![Image](https://img.shields.io/badge/python-3.9-informational?style=flat-square&logo=python&logoColor=yellow)
![Image](https://img.shields.io/github/commit-activity/m/TechWiz-3/git-commit-emojis?color=yellowgreen&logo=git&style=flat-square)  
![Image](https://img.shields.io/github/stars/TechWiz-3/git-commit-emojis?color=green&label=STARS&style=flat-square)
![Image](https://img.shields.io/github/issues/TechWiz-3/git-commit-emojis?color=red&label=ISSUES&style=flat-square)
![Image](https://img.shields.io/github/issues-pr/TechWiz-3/git-commit-emojis?color=blueviolet&label=PULL%20REQUESTS&style=flat-square)

A simple cross platform python script that automates easy labelling of git commits with descriptive emojis and text. Issues, PRs and suggestions more than welcome.

## About
We all like a bit of extra color and spice to our boring old commit messages, this not only adds that but also adds information about the commit.

## Installation
Planning on putting the project on pypi and scoop soon  

**Simple**
```sh
# <commit> = name you wish to give the command (I recommend gc or commit)
git clone https://github.com/TechWiz-3/git-commit-emojis.git
cp commit /usr/local/bin/<commit>
chmod +x /usr/local/bin/<commit>
```

**Path**
```sh
git clone https://github.com/TechWiz-3/git-commit-emojis.git
chmod +x commit gc
```
Then go into your `~/.bash_profile` and add the line
`export PATH=${PATH}:/driveorhome/ur_username/Desktop/filepath/git-commit-emojis`


## Usage

## The Story
So I noticed that [this](https://github.com/msaaddev) programmer's commits always had really neat looking labels with emojis. I searched it up and found a number of repositories or gists talking about emojis for various sorts of commits.  
My favourite was [emoji log](https://github.com/ahmadawais/Emoji-Log) (which this programmer used). Not only did it add emojis but it included simple labels that go with the emojis. However, emoji log only allows 5 labels, no more, no less, and for each label a custom command is made.  
While this is an elegant solution, what if you want more than just 5 labels?

This project combines the stablity of emojified commit labels (emoji-log), with an increased diversity of emojis and labels (gitmoji) while requiring no memorisation and keeping the CLI interface compact and neat.

Here are the emoji guides mentioned above, they are all great and this project wouldn't be possible without them so be sure to check them out:  
* [Git command emoji gist](https://gist.github.com/parmentf/035de27d6ed1dce0b36a)  
* [Emoji-log](https://github.com/ahmadawais/Emoji-Log)  
* [Gitmoji](https://github.com/topics/gitmoji)
* [Git commit emoji](https://github.com/liuchengxu/git-commit-emoji-cn)  


## Label Guide
### Select Menu Options
Usage:  
```
commit -m "your commit message (with or without quotes)"
```

![Image](./screenshots/commit_select_menu.png)  
👌 Improvement = `👌 IMPROVE: <commit message>`  
📦 Addition = `📦 NEW: <commit message>`  
📖 Documentation = `📖 DOC: <commit message>`  
🐛 Bug-fix = `🐛 FIX: <commit message>`  
🔖 Version-tag = `🔖 <commit message>`  

### Shorcut Options:
Usage:  
```
commit -sh <shortcut>
```
Shortcuts:  

`ty`     commit message defaults to: `✏️ FIX TYPO`  

`cl`     commit message defaults to: `🧹 CLEAN UP`  

`in`     commit message defaults to: `🎉 INITIAL COMMIT`  

`ln`     commit message defaults to `🚨 FIX LINT WARNINGS`  

### Other menus
## Emoji-log menu
`commit -s "msg"` or `commit --strict "msg"`
## Extra menu
Coming soon...

## Support the project
You can support the project  by adding the following text to the end of your `README.md` 
```
---
### 🎉 Commit labels
If you're interested in the commit labels used in this repo, check out the [git commit emoji](https://github.com/TechWiz-3/git-commit-emojis) project
```
