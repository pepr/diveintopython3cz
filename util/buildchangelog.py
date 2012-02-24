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

<pre>
'''

foot = '</pre>'

def gitLogLines():
    gitcmd = 'git log --pretty=format:"%ad  %s" --date=short'
    with subprocess.Popen(gitcmd, stdout=subprocess.PIPE) as proc:
        for line in proc.stdout:
            try:
                yield line.decode('utf-8')
            except UnicodeDecodeError:
                yield line.decode('cp1250') # první git commit byl v cp1250


def pgmPath():
    return os.path.split(os.path.realpath(__file__))[0]


# Generovaný výstupní soubor.
chlogname = os.path.join(pgmPath(), '..', 'changelog.html')
with open(chlogname, 'w', encoding='utf-8') as f:
    f.write(head)
    f.write(''.join(gitLogLines()).replace('&', '&amp;'))
    f.write(foot)
