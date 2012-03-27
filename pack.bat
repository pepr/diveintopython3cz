pushd buildPDF
copy PonormeSeDoPythonu3.pdf ..
copy single.html PonormeSeDoPythonu3single.html
popd
rem Přibalí i vygenerovaný changelog.html a PonormeSeDoPythonu3single.html
zip -r PonormeSeDoPythonu3-html *.html *.css examples/* i/* j/*
