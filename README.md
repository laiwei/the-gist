##### 这是一个手把手教你如何写一个类似于github的gist

|功能|
|------------------------------|
|支持markdown格式|
|自动判断代码类型并支持代码高亮|
|自动识别超链接|
|支持python, ruby, bash, js 等文件语法高亮|
|支持表格扩展, github markdown flavored|
|使用python语言|
|使用flask web框架|


#### 环境准备

- 安装python环境

    ```bash
    sudo apt-get install python
    sudo apt-get install python-virtualenv
    ```

- 使用virtualenv生成开发环境

    ```bash
    mkdir -p  ~/proj/the-gist/
    cd ~/proj/the-gist/
    virtualenv ./env
    source ./env/bin/activate

    pip install misaka
    pip install pygments
    pip install Flask
    pip install sh
    ```

- 说明

      - [sundown](https://github.com/vmg/sundown)

            是一个c语言开发的，快速，兼容，稳定的markdown解析器。
            github.com的markdown文档解析，底层就是用的sundown。

      - [misaka](https://github.com/FSX/misaka/)

            是sundown的Python binding

      - [pygments](http://pygments.org/)

            pygments，这是一个很牛逼的项目，python开发的。
            专门用来提供语法高亮的，目前支持有上百种语言的高亮
            很简单，输入一段内容，自动高亮输出，输出格式可以是html，RTF，LaTeX 以及ascii序列
            另外，pygments也提供一个shell命令行工具 pygmentize
            比如：
                pygmentize ./app.py  # 就会按照语法，高亮输出app.py的内容到屏幕

      - [flask](flask.pocoo.org) -- [quickstart](http://flask.pocoo.org/docs/quickstart/)

             一个很流行的python web框架

      -  [sh](https://github.com/amoffat/sh) - `optional`

             一个很酷的python lib，可以让你很方便的在python里面，
             操作各种shell命令，比如:

             import sh
             sh.git.clone("https://github.com/laiwei/xxx.git")


- 代码 [fork me on github](https://github.com/laiwei/the-gist)

- 安装

    ```bash
      git clone https://github.com/laiwei/the-gist ~/
      cd ~/the-gist/ && virtualenv env
      . env/bin/activate
      pip install -r ./pip_requirements.txt

      python app.py

      浏览器中访问
      http://127.0.0.1:5009/show/test.md
      http://127.0.0.1:5009/show/test.py
    ```
