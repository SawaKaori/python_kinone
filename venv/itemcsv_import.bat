cd C:\kintone
REM  E:\src\Python\kintone\venv
cli-kintone.exe --export -a 141 -d hira-print -t IzzpfQdIS2YNCl5pT8bBzsmogWyheXJnTSPRwY0d -e sjis -c "$id,product_cd" > itemlist_kintone.csv 
cd C:\kintone\getrecordid
REM  cd E:\src\Python\kintone\venv\dist\getrecordid
call getrecordid.exe
cd C:\kintone
REM  cd E:\src\Python\kintone\venv
cli-kintone.exe --import -a 141 -d hira-print -t IzzpfQdIS2YNCl5pT8bBzsmogWyheXJnTSPRwY0d -e sjis -f itemlist_new.csv 

