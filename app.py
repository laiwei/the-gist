#!/usr/bin/env python
#-*- coding:utf-8 -*-
import os
import re
import misaka
import pygments
from pygments import highlight
from pygments.lexers import (get_lexer_by_name, get_lexer_for_filename, guess_lexer_for_filename)
from pygments.formatters import HtmlFormatter
import HTMLParser
from flask import Flask, request, abort, render_template
app = Flask(__name__)

@app.route("/show/<name>")
def show(name):
    name = name.replace("..", "", -1).replace(" ", "", -1)
    file_path = os.path.join("./f", name)
    if not (os.path.exists(file_path) or os.path.isfile(file_path)):
        abort(404, u"不存在这个文件哈")

    content = open(file_path).read().decode("utf8")

    if name.endswith(".md") or name.endswith(".markdown"):
        html = misaka.html(content, extensions=\
                misaka.EXT_AUTOLINK|misaka.EXT_LAX_HTML_BLOCKS|misaka.EXT_SPACE_HEADERS|\
                misaka.EXT_SUPERSCRIPT|misaka.EXT_FENCED_CODE|misaka.EXT_NO_INTRA_EMPHASIS|\
                misaka.EXT_STRIKETHROUGH|misaka.EXT_TABLES)
        def _r(m):
            try:
                lexer_name = m.group(1)
                code = m.group(2)
                lexer = get_lexer_by_name(lexer_name)
                code = HTMLParser.HTMLParser().unescape(code)
                return highlight(code, lexer, HtmlFormatter())
            except pygments.util.ClassNotFound:
                return m.group()

        p = re.compile(r'''<pre><code class="([0-9a-zA-Z._-]+)">(.+?)</code></pre>''', re.DOTALL)
        html = p.sub(lambda m: _r(m), html)

    else:
        try:
            lexer = guess_lexer_for_filename(file_path, content)
        except pygments.util.ClassNotFound:
            lexer = get_lexer_by_name("python")
        html = highlight(content, lexer,  HtmlFormatter())

    return render_template("gfm.html", **locals())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5009)

