FROM    jcdemo/flaskapp

COPY    ./nsdashboard ~/code/nsdashboard/ 
EXPOSE  5000

ENTRYPOINT ["python","~/code/nsdashboard/web.py"]
