# CPE 2.3Parser

Parser CPE 2.3 napisany jako rozwiązanie zadania rekrutacyjnego do firmy NASK. Skrypt pisany i testowany w Pythonie 3.9.6.


UWAGA: Znak specjalny backslash w Pythonie aby był widoczny musi zostać zdublowany, stąd w wynikach widzimy podwojone znaki "\".
W ostatnim wierszu po uruchomieniu skryptu wyświetlany jest string z poprawionymi podwojonymi backslashami. Ponadto w pliku tekstowym również zapisywany jest format poprawiony.

UŻYCIE: python parse.py "stringCpe"

Komendy testowe z dokumentacji CPE 2.3:

python parse.py "cpe:2.3:a:microsoft:internet_explorer:8.0.6001:beta:*:*:*:*:*:*"

python parse.py "cpe:2.3:a:microsoft:internet_explorer:8.*:sp?:*:*:*:*:*:*"

python parse.py "cpe:2.3:a:microsoft:internet_explorer:8.\*:sp?:*:*:*:*:*:*"

python parse.py "cpe:2.3:a:hp:insight_diagnostics:7.4.0.1570:-:*:*:online:win2003:x64:*"

python parse.py "cpe:2.3:a:hp:insight_diagnostics:7.4.*.1570:*:*:*:*:*:*"

python parse.py "cpe:2.3:a:foo\\bar:big\$money:2010:*:*:*:special:ipod_touch:80gb:*"


#########

Skrypt napisany przy pomocy dokumentacji: https://csrc.nist.gov/publications/detail/nistir/7695/final

Jan Adamski 2022