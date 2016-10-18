# git入坑教程

## git简介
git是在程序猿中非常流行的分散式版本控制工具,由Linux之父Linus Torvalds创作,非常适合多人协作完成项目开发.

著名的分散式版本控制系统有Monotone，git等.


## 安装
在ubuntu安装git十分简单,只需以下命令:

    $ sudo apt-get update
    $ sudo apt-get install git

在windows下同样没有太大问题, 直接去[这里](https://git-scm.com/download/win)下载安装包, 点击安装即可.


see [How to Install Git on Ubuntu 14.04](https://www.digitalocean.com/community/tutorials/how-to-install-git-on-ubuntu-14-04)


## 用户初始配置:

    $ git config --global user.name "vibiu"
    $ git config --global user.email "vibiu_ubuntu@163.com"

## ssh密匙配置:

    $ ssh-keygen -t rsa -C "vibiu_ubuntu@163.com"

see [廖雪峰的git教程](http://www.liaoxuefeng.com/wiki/0013739516305929606dd18361248578c67b8067c8c017b000)


## 基本命令:

    git clone
    git init
    git status
    git log
    git rm
    git diff
    git add
    git commit
    git checkout
    git reset
    git rebase
    git merge
    git fetch
    git pull
    git push
    ...

这些命令你只要输入git, 按下回车, 就会发现.


## 一次完美的提交过程:
新建一个目录

    $ mkdir gitgitgit

初始化git项目

    $ cd gitgitgit
    $ git init

写你的代码

    $ echo "hello world" >> git.md

添加代码到git的缓存区

    $ git add git.md
    // 或者一次把所有代码添加
    $ git add -A

把代码从缓存区提交到版本库

    $ git commit -m "first commit"

添加远程仓库

    $ git remote add origin git@github.com:vibiu/gitgitgit.git

推送到远程仓库

    $ git push origin master


## git不止这些
* 分支管理
* 冲突解决
* 版本回退
* 子模块管理



## 我的git经验
1.fork一个管理员已经建好的的主分支到自己的git远程仓库中

2.从主分支clone一个分支到本地

    $ git clone https://git.oschina.net/master/main.git

    // 这时候有唯一分支 master
    $ git branch
    >> * master
    // 这时候有唯一远程仓库 origin
    $ git remote
    >> origin

3.添加自己的远程仓库地址,假定本地已经和远程仓库ssh连接

    $ git remote add vibiu git@oschina.net:vibiu/main.git

    // 这时候远程仓库添加了一个 vibiu
    $ git remote
    >> origin
    >> vibiu

4.新建一个自己的本地分支

    $ git branch work

    // 这时候本地分支添加了一个 work
    $ git branch
    >> * master
    >>   work

5.切换到work分支中编写代码

    $ git checkout work

    // 这时候所有的commit均会保留在work分支内
    $ git branch
    >>   master
    >> * work

6.写完记得checkout到master分支pull一下看有没有其他分支的更新

    $ git checkout master
    $ git pull origin master

7.在master分支将在work分支的代码和master合并

    $ git merge work
    //有冲突就解决冲突

8.上传到自己远程分支 vibiu

    $ git push vibiu master:master

9.在远程仓库上发起pull requests

10.远程仓库最好有两个分支,一个是主分支,用于存放原主分支的代码,一个是自己用来提交的分支,如果自己提交的分支没有被及时接受,就另开一个分支优化代码然后再用另一个分支提交pull requests


## 一些平时遇到git问题和解决方案

1.将某个文件回退到上个版本

    $ git reset HEAD^ file.md
    $ git commit -m "reset"
    $ git checkout -- file.md

2.清理提交文档树

    $ git checkout otherbranch
    $ git reabase master
    $ git checkout master
    $ git merge otherbranch

这样master的提交文档树就是一条直线了
see [rebase用法](http://gitbook.liuhui998.com/4_2.html)

3.优雅的回退版本, 就是用一次新的提交让版本库回到原来的某个版本

    $ git revert HEAD^
    // 提交一次新的提交回到上个版本


## 解决关于gitignore的问题
.gitignore是用于提示git哪些文件或目录不需要添加到版本控制中
使用.gitignore fix untracked files

    $ git rm -r --cached .
    $ git add .
    $ git commit -m "fixed untracked files"

visit [gitignore not working](http://stackoverflow.com/questions/11451535/gitignore-not-working)

.gitmodules是用来引用git上的其他包
  
    $ git submodule  init
    $ git submodule update

