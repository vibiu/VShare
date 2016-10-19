# Sublime Text
##安装sublime:

    sudo add-apt-repository ppa:webupd8team/sublime-text-3
    sudo apt-get update
    sudo apt-get install sublime-text-installer


## 配置tab为4个空格:

    Preferences-User/:
        {
            "tab_size":4,
            "translate_tabs_to_spaces": true
        }

visit [sublime text2配置tab为4个空格](http://blog.csdn.net/intel80586/article/details/8306699)


## 禁用vi模式

    Preferances-User/:
        "ignored_packages":
        [
            "Vintage"
        ],


## Package Control
    Ctrl + `

    import urllib.request,os,hashlib; h = '2915d1851351e5ee549c20394736b442' + '8bc59f460fa1548d1514676163dafc88'; pf = 'Package Control.sublime-package'; ipp = sublime.installed_packages_path(); urllib.request.install_opener( urllib.request.build_opener( urllib.request.ProxyHandler()) ); by = urllib.request.urlopen( 'http://packagecontrol.io/' + pf.replace(' ', '%20')).read(); dh = hashlib.sha256(by).hexdigest(); print('Error validating download (got %s instead of %s), please try manual install' % (dh, h)) if dh != h else open(os.path.join( ipp, pf), 'wb' ).write(by)

see [packagecontrol](https://packagecontrol.io/installation#st3)


## Preference User
```
{
    "auto_complete": true,
    "color_scheme": "Packages/Color Scheme - Default/Solarized (Dark).tmTheme",
    "ensure_newline_at_eof_on_save": true,
    "file_exclude_patterns":
    [
        ".DS_Store",
        "*.pid",
        "*.pyc"
    ],
    "folder_exclude_patterns":
    [
        ".git",
        "__pycache__"
    ],
    "font_size": 12,
    "highlight_line": true,
    "ignored_packages":
    [
        "Vintabe"
    ],
    "tab_size": 4,
    "translate_tabs_to_spaces": true,
    "trim_trailing_white_space_on_save": true
}
```
see [Develop Python Using Sublime Text](http://sw897.github.io/2014/02/13/sublime-text-3-for-python/)


## Packages
see [Build Python IDLE using Sublime Text](http://python.jobbole.com/81312/)

see [Ncuhome Backend-guide](https://github.com/ncuhome/backend-guide)

### Anaconda
[Anaconda Guide](https://rhinstaller.github.io/anaconda/)
    Preferences>Package Settings>Anaconda>Setting-User/:
        {
            "python_interpreter":"/usr/bin/python",
            "auto_python_builder_enabled": false,
            "anaconda_linting": false,
            "auto_complete_triggers": [{"selector": "source.python - string - comment - constant.numeric", "characters": "."}],
            "suppress_word_completions": true,
            "suppress_explicit_completions": true
        }

### GitGutter
[jisaacks/GitGutter](https://github.com/jisaacks/GitGutter)

### Python PEP8 Autoformat
[Python PEP8 Autoformat](https://bitbucket.org/StephaneBunel/pythonpep8autoformat)

### Flake8Lint
[Flake8Lint](https://github.com/dreadatour/Flake8Lint)

### Markdown Preview
[Markdown Preview](https://github.com/revolunet/sublimetext-markdown-preview)

    preference > user-key-binding

    { "keys": ["alt+m"], "command": "markdown_preview", "args": {"target": "browser", "parser":"markdown"} }


### Terminal
[Terminal](https://packagecontrol.io/packages/Terminal)

default key-binding:

    Ctrl+Alt+Shift+t(open terminal here)
    Ctrl+Alt+t(open system terminal)


### AdvancedNewFile
[AdvancedNewFile](https://github.com/skuroda/Sublime-AdvancedNewFile)

I don't use it now.

### Sidebar enhancements
[Sidebar enhancements](https://github.com/titoBouzout/SideBarEnhancements/tree/st3)



## front end
see [ncuhome front-end guide](https://github.com/ncuhome/frontend-guide)

### HTML-CSS-JS Prettify
see [victorporof/Sublime-HTMLPrettify](https://github.com/victorporof/Sublime-HTMLPrettify)

### AutoFileName
see [BoundInCode/AutoFileName](https://github.com/BoundInCode/AutoFileName)

### Emmet
zen-coding
see [sergeche/emmet-sublime](https://github.com/sergeche/emmet-sublime)

### Color Highlighter

### ColorPicker

### DocBlockr

### JsFormat

### LiveReload

### TrailingSpaces


# vim

## vim资料

[Vim命令合集](http://www.cnblogs.com/softwaretesting/archive/2011/07/12/2104435.html)

[Vim简明教程](http://blog.csdn.net/niushuai666/article/details/7275406)

[vim进阶](http://easwy.com/blog/archives/advanced-vim-skills-cscope/)

[vim配置](http://www.wklken.me/posts/2013/06/11/linux-my-vim.html#vim)

[vim & pathogen & git](http://lostjs.com/2012/02/04/use-pathogen-and-git-to-manage-vimfiles/)


# atom

see [atom](https://atom.io/)

see [atom开源源码](https://github.com/atom/atom)

# VSCode

see [vscode](https://code.visualstudio.com)
