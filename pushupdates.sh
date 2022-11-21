git config core.sshCommand 'ssh -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no -i /config/.ssh/id_rsa -F /dev/null'
git config --global user.email "newlon@outlook.com"
git add .
git commit -m "`date +'%m%d%y.%H:%M:%S'`"
git push -u origin master