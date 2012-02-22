zip -r PonormeSeDoPythonu3 PonormeSeDoPythonu3 
pushd buildPDF
zip -r PonormeSeDoPythonu3pdf PonormeSeDoPythonu3.pdf
move PonormeSeDoPythonu3pdf.zip ..
popd
call ziphtml.bat