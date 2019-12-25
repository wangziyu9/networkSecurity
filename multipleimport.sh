# cd /home/yur/Documents/upload
# 列出目录下所有 .josn 文件绝对路径
echo `ls`
# tree -if /home/yur/Documents/upload | sed "s:^:`pwd`:g" | grep json$ |
tree -if /home/yur/Documents/upload | grep json$ |
while read col;
do
	echo $col;
	cp $col col.bak;
	if [ $(file -i $col | grep utf-8 | awk '{print length($0)}') ]
	then 
		echo utf-8;
	else
		iconv -f gbk -t utf-8 $col -o $col;
		echo "gbk->utf8 转换完成";
	fi
done

tree -if /home/yur/Documents/upload | grep json$ |
while read col;
do
	echo "正在导入";
	echo $col;
	mongoimport -d TERMINAL -c origin $col;
	rm $col;
done