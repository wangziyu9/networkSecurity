# 通过文件创建 docker 镜像
FROM    jcdemo/flaskapp

COPY    ./nsdashboard ~/code/nsdashboard/ 
EXPOSE  5000

ENTRYPOINT ["python","~/code/nsdashboard/web.py"]
# docker build -t termmgr .
# 10.56.113.68   mssdev Hnltxxhb@2020