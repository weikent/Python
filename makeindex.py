#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import time
import re

import platform



fileType = ["html", "htm"]

    
defaultFolder = "Org_Publish"

ubuntuDefaultPath = "/media/psf/Home/Kuaipan/Org_Git"
macDefaultPath = "/Users/weishijian/Kuaipan/Org_Git"

defaultPath = ""


if platform.system() == "Darwin":
    defaultPath = macDefaultPath
elif platform.system() == "Linux":
    defaultPath = ubuntuDefaultPath

defaultPathLen = len(defaultPath) + len(defaultFolder) + 1  # 1是一个 "/" 的长度



def delFile(path):
    """
    
    Arguments:
    - `path`:
    """
#    print path

    if path[-3 :] == "mp3" or path[-3 :] == "pdf" or path[-3 :] == "txt" or path[-3 :] == "rar":
        pass
    else:
        os.remove(path)

def changeInfo1(rootDir, folder):

    print "--------------------------------------------------------------------------------"
    rootDir = rootDir + "/"
    rootPath = os.path.join(rootDir, folder)
    # print "1===" + rootPath
    # print "2====" + folder
    folderName = folder

    # if folder == "refs":  
    #     return

    for dirName in os.listdir(rootPath): 
        # print "dirname " + dirName
        # print "5===" + rootPath
        # print "6====" + dirName

        path = os.path.join(rootPath, dirName) 

        if os.path.isdir(path):
            needInsertDirName = False


            for dirName1 in os.listdir(path):
                # print "88====" + dirName1
                if dirName1.endswith("html"):
                    needInsertDirName = True
                    break

            if needInsertDirName:
                f.write("<h2>" + dirName + "</h2>\r\n")  #把标题放在这里的话，如果文件夹里面没有html文件的话，也会添加一个空目录标题
                # print "3===" + rootPath
                # print "4====" + dirName
                
                changeInfo1(rootPath, dirName)



            # f.write("<h2>" + dirName + "</h2>\r\n")  #把标题放在这里的话，如果文件夹里面没有html文件的话，也会添加一个空目录标题
            # changeInfo1(rootPath, dirName)

        else:
            if path[-4 :] in fileType:
                print "path = ", path
                i = path.rfind("/") # 路径中 / 最后出现的位置     rfind 反向查找
                

                f.write("<a href = " + path[defaultPathLen:] + ">" + path[i+1:-5] + "</a>")
                f.write("<br>")




import getopt, sys
def usage():
    print '''
NAME
    this file is used to make a index file of my org project.
Usage
    python makeindex.py
    should use it in the same dir with the root of the [org_publish]
'''[1:-1]

if __name__ == '__main__':




    try:
        opts, args = getopt.getopt(sys.argv[1:], "hf:", ["help", "file="])
        getopt.getopt
    except getopt.GetoptError as err:
        # print help information and exit:
        print str(err) # will print something like "option -a not recognized"
        usage()
        sys.exit(2)

    file=""

    print "opts is "
    print opts
    print args
    if opts:
        print "a"
    else:
        print "nb"

    if args:
        if args.len == 2:
            defaultFolder = args[1]
            defaultPath = args[0]
        else:
            print "wrong args"
            usage()
            sys.exit()
    else:
        print "use default args"


    for o, a in opts:
        print "o is" + o
        print "a is" + a
        if o in ("-h", "--help"):
            usage()
            sys.exit()
        elif o in ("-f", "--file"):
            file= a
        else:
            assert False, "unhandled option"
    

    print "hello world";


    if os.path.isfile("./index.html"):
        os.remove("./index.html")
    
    f = open("./index.html", 'a')
    f.write('''<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
"http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" lang="en" xml:lang="en">
<head>
<title>Index</title>
<!-- 2015-03-26 Thu 10:20 -->
<meta  http-equiv="Content-Type" content="text/html;charset=utf-8" />
<meta  name="generator" content="Org-mode" />
<meta  name="author" content="weikent" />
<style type="text/css">
 <!--/*--><![CDATA[/*><!--*/
  .title  { text-align: center; }
  .todo   { font-family: monospace; color: red; }
  .done   { color: green; }
  .tag    { background-color: #eee; font-family: monospace;
            padding: 2px; font-size: 80%; font-weight: normal; }
  .timestamp { color: #bebebe; }
  .timestamp-kwd { color: #5f9ea0; }
  .right  { margin-left: auto; margin-right: 0px;  text-align: right; }
  .left   { margin-left: 0px;  margin-right: auto; text-align: left; }
  .center { margin-left: auto; margin-right: auto; text-align: center; }
  .underline { text-decoration: underline; }
  #postamble p, #preamble p { font-size: 90%; margin: .2em; }
  p.verse { margin-left: 3%; }
  pre {
    border: 1px solid #ccc;
    box-shadow: 3px 3px 3px #eee;
    padding: 8pt;
    font-family: monospace;
    overflow: auto;
    margin: 1.2em;
  }
  pre.src {
    position: relative;
    overflow: visible;
    padding-top: 1.2em;
  }
  pre.src:before {
    display: none;
    position: absolute;
    background-color: white;
    top: -10px;
    right: 10px;
    padding: 3px;
    border: 1px solid black;
  }
  pre.src:hover:before { display: inline;}
  pre.src-sh:before    { content: 'sh'; }
  pre.src-bash:before  { content: 'sh'; }
  pre.src-emacs-lisp:before { content: 'Emacs Lisp'; }
  pre.src-R:before     { content: 'R'; }
  pre.src-perl:before  { content: 'Perl'; }
  pre.src-java:before  { content: 'Java'; }
  pre.src-sql:before   { content: 'SQL'; }

  table { border-collapse:collapse; }
  caption.t-above { caption-side: top; }
  caption.t-bottom { caption-side: bottom; }
  td, th { vertical-align:top;  }
  th.right  { text-align: center;  }
  th.left   { text-align: center;   }
  th.center { text-align: center; }
  td.right  { text-align: right;  }
  td.left   { text-align: left;   }
  td.center { text-align: center; }
  dt { font-weight: bold; }
  .footpara:nth-child(2) { display: inline; }
  .footpara { display: block; }
  .footdef  { margin-bottom: 1em; }
  .figure { padding: 1em; }
  .figure p { text-align: center; }
  .inlinetask {
    padding: 10px;
    border: 2px solid gray;
    margin: 10px;
    background: #ffffcc;
  }
  #org-div-home-and-up
   { text-align: right; font-size: 70%; white-space: nowrap; }
  textarea { overflow-x: auto; }
  .linenr { font-size: smaller }
  .code-highlighted { background-color: #ffff00; }
  .org-info-js_info-navigation { border-style: none; }
  #org-info-js_console-label
    { font-size: 10px; font-weight: bold; white-space: nowrap; }
  .org-info-js_search-highlight
    { background-color: #ffff00; color: #000000; font-weight: bold; }
  /*]]>*/-->
</style>
<link rel="stylesheet" href="../emacs.css" type="text/css"/>
<script type="text/javascript">
/*
@licstart  The following is the entire license notice for the
JavaScript code in this tag.

Copyright (C) 2012-2013 Free Software Foundation, Inc.

The JavaScript code in this tag is free software: you can
redistribute it and/or modify it under the terms of the GNU
General Public License (GNU GPL) as published by the Free Software
Foundation, either version 3 of the License, or (at your option)
any later version.  The code is distributed WITHOUT ANY WARRANTY;
without even the implied warranty of MERCHANTABILITY or FITNESS
FOR A PARTICULAR PURPOSE.  See the GNU GPL for more details.

As additional permission under GNU GPL version 3 section 7, you
may distribute non-source (e.g., minimized or compacted) forms of
that code without the copy of the GNU GPL normally required by
section 4, provided you include this license notice and a URL
through which recipients can access the Corresponding Source.


@licend  The above is the entire license notice
for the JavaScript code in this tag.
*/
<!--/*--><![CDATA[/*><!--*/
 function CodeHighlightOn(elem, id)
 {
   var target = document.getElementById(id);
   if(null != target) {
     elem.cacheClassElem = elem.className;
     elem.cacheClassTarget = target.className;
     target.className = "code-highlighted";
     elem.className   = "code-highlighted";
   }
 }
 function CodeHighlightOff(elem, id)
 {
   var target = document.getElementById(id);
   if(elem.cacheClassElem)
     elem.className = elem.cacheClassElem;
   if(elem.cacheClassTarget)
     target.className = elem.cacheClassTarget;
 }
/*]]>*///-->
</script>
</head>
<body>
<div id="content">
<h1 class="title">Index</h1>

    ''')
    

# 实际写入内容的代码

    changeInfo1(defaultPath, defaultFolder)



    f.write('''</div>
<div id="postamble" class="status">
<hr><p class="author">Author: weikent (<a href="mailto:weishijian@weikents-MacBook-Air.local">weishijian@weikents-MacBook-Air.local</a>)</p>
<p class="date">Date: ''')
    timeStr = time.strftime('%Y-%m-%d : %H : %M : %S',time.localtime(time.time()))
    f.write(timeStr)
    f.write('''</p>
<p class="creator"><a href="http://www.gnu.org/software/emacs/">Emacs</a> 24.4.1 (<a href="http://orgmode.org">Org</a> mode 8.2.10)</p>
<p class="validation"><a href="http://validator.w3.org/check?uri=referer">Validate</a></p>
</div>
</body>
</html>
''')

    f.close()


    print(platform.system())