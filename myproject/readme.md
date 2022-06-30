1. Run msql
mysql -u mc -p
2. check database
show databases; //show cac databases
use .... (database muon sd);
show tables; //show cac table trong database
describe ... (table muon xem);
select * from ... (table); //noi dung chi tiet trong table
3. run web
cd project
source projectenv/bin/activate
uwsgi --socket 0.0.0.0:5000 --protocol=http -w wsgi:app
different way: run: python myproject.py