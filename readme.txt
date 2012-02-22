Podadresář en obsahuje podobu originálu, která byla použita pro původní 
překlad pro CZNIC.

Podadresář examples obsahuje příklady, které jsou součástí výsledných HTML.

Podadresář i obsahuje ostré obrázky.

Podadresář j obsahuje JavaScripty.

Dávka rebuildAll.bat volá níže popsané dávky a způsobí vygenerování a zabalení
všech možných forem do podoby zip souborů.

Dávka clean.bat odstraňuje vše, co může být vygenerované.

Dávka ziphtml.bat balí nekorigovanou podobu HTML do PonormeSeDoPythonu3-html.zip.
Výsledek je poté ručně umísťován na web jak ve sbalené, tak v rozbalené podobě.

Spuštění util/f.bat způsobí vygenerování podadresáře PonormeSeDoPythonu3
s korigovaným obsahem HTML. (Dávka pack.py ji případně zabalí 
do PonormeSeDoPythonu3.zip.) Poté je vygenerována zploštěná verze HTML do
nově vytvořeného buildPDF v podobě single.html. Ta je spolu s upraveným
css souborem použita programem Prince (free verze) pro vygenerování 
PonormeSeDoPythonu3.pdf. Ta bývá dávkou pack.bat zabalena 
do PonormeSeDoPythonu3pdf.zip.

Dávka pack.bat balí vše vygenerované i nevygenerované do podoby zip souborů.