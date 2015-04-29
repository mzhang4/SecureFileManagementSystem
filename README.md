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

then you need add your database info into mysql:

mysql -uroot

flush privileges;

CREATE USER 'CS8120'@'localhost' IDENTIFIED BY 'CS8120';

GRANT ALL PRIVILEGES ON *.* TO 'CS8120'@'localhost'

    -> WITH GRANT OPTION;

then you can operate with:

mysql -uCS8120 -p

CREATE DATABASE CS8120;

then follow create_tables.sql in experiment/sql instruction to create tables.

before you actually create the first admin user use:

python adminCreator.py 

you need prepare a folder to install your key like this:

/Volumes/NO\ NAME/keys

for me, I store keys in a usb driver named NO NAME, then a folder named keys.

after these, you can create your first admin user now!

python adminCreator.py

then you can login in

python main.py use the user you created.
