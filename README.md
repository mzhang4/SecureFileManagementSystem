# Secure-file-management-system
1.install mysql, then install Python interface to MySQL,
for example, on MAC:
export PATH=$PATH:/usr/local/mysql/bin
sudo pip install MySQL-python 

some problem you may come across:
otool -L /Library/Python/2.7/site-packages/_mysql.so
sudo install_name_tool -change libmysqlclient.18.dylib /usr/local/mysql/lib/libmysqlclient.18.dylib /Library/Python/2.7/site-packages/_mysql.so

2.install pycrypto(The Python Cryptography Toolkit) which used in this project:
sudo pip install pycrypto

