# MySQL
The goal for this project is to set up a Primary-Replica infrastructure using MySQL and create a MySQL backup

### Requirements
- Allowed editors: vi, vim, emacs
- All your files will be interpreted on Ubuntu 14.04 LTS
- Your Bash script must pass Shellcheck (version 0.3.3-1~ubuntu14.04.1 via apt-get) without any error

### Concepts
- What is the main role of a database
- What is a database replica
- What is the purpose of a database replica
- Why database backups need to be stored in different physical locations
- What operation should you regularly perform to make sure that your database backup strategy actually works

### File Descriptions
| File | Description |
| ------------- |:-------------:|
| 0-mysql_configuration_primary | Configures Primary MySQL database |
| 0-mysql_configuration_replica | Configures Replica MySQL database |
| 1-mysql_backup | Script to generate MySQL dump and create compressed archive out of it |

#### Author
Lisa Olson
