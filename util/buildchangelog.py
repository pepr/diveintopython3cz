#!/usr/bin/python3

import os
import subprocess

# Hlavička pro HTML 5
head = '''<!DOCTYPE html>
<meta charset=utf-8>
<title>Seznam oprav a úprav &ndash; Ponořme se do Pythonu 3</title>
<!--[if IE]><script src=j/html5.js></script><![endif]-->
<link rel=stylesheet href=dip3.css>
<style>
</style>
<link rel=stylesheet media='only screen and (max-device-width: 480px)' href=mobile.css>
<link rel=stylesheet media=print href=print.css>
<meta name=viewport content='initial-scale=1.0'>
<body id=appe>
<!-- <form action=http://www.google.com/cse><div><input type=hidden name=cx value=014021643941856155761:l5eihuescdw><input type=hidden name=ie value=UTF-8>&nbsp;<input type=search name=q size=25 placeholder="powered by Google&trade;">&nbsp;<input type="submit" name="sa" value="Hledej"></div></form> -->
<p>Nacházíte se zde: <a href="index.html">Domů</a> <span class="u">&#8227;</span> <a href="table-of-contents.html#troubleshooting">Ponořme se do Pythonu 3</a> <span class="u">&#8227;</span>
<h1>Seznam oprav a úprav</h1>

<p>Nejnovější záznamy jsou nahoře.


<pre>
'''

foot = '''</pre>

<p class=a>&#x2042;

<p class=v><a rel="prev" href="troubleshooting.html" title="zpět na „Odstraňování problémů“"><span class="u">&#x261C;</span></a> <a href="blank.html" rel="next"><span class="u">&#x261E;</span></a>

<p class=c>Generováno pro český překlad.
<script src=j/jquery.js></script>
<script src=j/dip3.js></script>
'''

pgmPath = os.path.split(os.path.realpath(__file__))[0]
chlogname = os.path.join(pgmPath, '..', 'changelog.html')


def gitLogLines():
    gitcmd = 'git log --pretty=format:"%ad  %s" --date=short'
    with subprocess.Popen(gitcmd, stdout=subprocess.PIPE) as proc:
        for line in proc.stdout:
            try:
                line = line.decode('utf-8')
            except UnicodeDecodeError:
                line = line.decode('cp1250') # první git commit byl v cp1250
            yield line

# Generovaný výstupní soubor.
with open(chlogname, 'w', encoding='utf-8', newline='\n') as f:
    f.write(head)
    content = ''.join(gitLogLines())
    content = content.replace('&', '&amp;')
    content = content.replace('<', '&lt;')
    f.write(content)
    f.write(foot)
