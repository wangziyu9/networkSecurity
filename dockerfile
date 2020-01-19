# 通过文件创建 docker 镜像
FROM    termmgr

COPY    ./nsdashboard ~/code/nsdashboard/ 
# MOUNT

EXPOSE  5000

ENTRYPOINT ["python","~/code/nsdashboard/web.py"]

# 连接远程服务器
# 10.56.113.68   mssdev [passowrd]
# ssh -p [port] mssdev@10.56.113.68 
# password [passowrd]

# 传输工作目录
# scp -r -P [port] networkSecurity/ mssdev@10.56.113.68:~

# 通过 DockerFile 构建 Docker 镜像
# [mssdev@localhost networkSecurity]$ docker build -t wzy-termmgr .

# 运行 Docker 镜像
# docker run -p5000:5000 wzy-termmgr