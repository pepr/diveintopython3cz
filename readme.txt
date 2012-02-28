The diveintopython3cz repository is related to the Czech translation
of the "Dive Into Python 3" by Mark Pilgrim -- see
https://github.com/diveintomark/diveintopython3.git

Majority of the texts here are therefore written in Czech.

Český překlad je k dispozici v podobě Git úložiště 
https://pepr@github.com/pepr/diveintopython3cz.git

Podadresář examples obsahuje příklady, které jsou součástí výsledných HTML.
V HTML souborech jsou na příslušných místech umístěny odkazy pro stažení
těchto příkladů.

Podadresář i obsahuje ostré obrázky.

Podadresář j obsahuje JavaScripty.

Soubor changelog.html není v git zachycen. Generuje se skriptem
util/buildchangelog.py

Dávka rebuildAll.bat volá níže popsané dávky a způsobí vygenerování a zabalení
všech možných forem do podoby zip souborů.

Dávka clean.bat odstraňuje vše, co může být vygenerované
(s výjimkou changelog.html).

Dávka ziphtml.bat balí nekorigovanou podobu HTML do PonormeSeDoPythonu3-html.zip.
Výsledek je poté ručně umísťován na web jak ve sbalené, tak v rozbalené podobě.

Dávka pack.bat balí vše vygenerované i nevygenerované do podoby zip souborů.

util/flatten2.py (Python 3) způsobí vygenerování podadresáře PonormeSeDoPythonu3
s korigovaným obsahem HTML. Poté je vygenerována zploštěná verze HTML do
nově vytvořeného buildPDF v podobě single.html. Ta je spolu s upraveným
css souborem použita programem Prince (free verze) pro vygenerování
PonormeSeDoPythonu3.pdf.
