FROM    py_fsk
# RUN     /bin/echo -e "LANG=\"en_US.UTF-8\"" >/etc/default/local
# EXPOSE  22
# EXPOSE  80
COPY    ./nsdashboard ~/code/nsdashboard/ 
EXPOSE  5000
# CMD     /bin/bash yum update
# CMD     /bin/bash yum install python36
# CMD     /bin/bash pip3 install flask

# CMD     /bin/bash python3 ~/code/nsdashboard/web.py
ENTRYPOINT ["python","~/code/nsdashboard/web.py"]