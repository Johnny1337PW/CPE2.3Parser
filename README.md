# CPE 2.3Parser

Parser CPE 2.3 napisany jako rozwiązanie zadania rekrutacyjnego do firmy NASK.

UWAGA: Znak specjalny backslash w Pythonie aby był widoczny musi zostać zdublowany, stąd w wynikach widzimy podwojone znaki "\". 

Komendy testowe z dokumentacji CPE 2.3:

python parse.py "cpe:2.3:a:microsoft:internet_explorer:8.0.6001:beta:*:*:*:*:*:*"

python parse.py "cpe:2.3:a:microsoft:internet_explorer:8.*:sp?:*:*:*:*:*:*"

python parse.py "cpe:2.3:a:microsoft:internet_explorer:8.\*:sp?:*:*:*:*:*:*"

python parse.py "cpe:2.3:a:hp:insight_diagnostics:7.4.0.1570:-:*:*:online:win2003:x64:*"

python parse.py "cpe:2.3:a:hp:insight_diagnostics:7.4.*.1570:*:*:*:*:*:*"

python parse.py "cpe:2.3:a:foo\\bar:big\$money:2010:*:*:*:special:ipod_touch:80gb:*"


Jan Adamski 2022