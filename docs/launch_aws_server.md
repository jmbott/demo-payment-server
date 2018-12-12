# Launch AWS web server and Setup

1. Log into AWS Console - [Login](https://console.aws.amazon.com/console/home)
2. Navigate to the EC2 Dashboard

![alt text](assets/dashboard.png "EC2 Dashboard")

3. Launch Instance
4. Select an Ubuntu Server - *Free Tier Eligible*

![alt text](assets/ubuntu.png "EC2 Ubuntu Free Tier")

5. Select t2.micro

![alt text](assets/instance_type.png "EC2 Instance")

6. Select Review and Launch

![alt text](assets/review_launch.png "EC2 Review and Launch")

7. Select Launch

![alt text](assets/launch.png "EC2 Launch")

8. Create a new key pair and download the `*.pem` file. Store it in a safe place.

![alt text](assets/key_pair.png "EC2 Key Pair")

9. Confirm Launch. Once launched you can check the IP in the Instances tab.

![alt text](assets/instances.png "EC2 Instances")

10. Change the label on the instance

![alt text](assets/rename.png "Rename Instance")

11. Update AWS permissions in the EC2 security group,

![alt text](assets/security_rules.png "EC2 Security Rules")

12. Navigate and login to [Duck DNS](http://www.duckdns.org/),

![alt text](assets/duckdns.png "Duck DNS")

13. Add a new subdomain and assign it the IP of our new server.

![alt text](assets/domain_name.png "Duck DNS Domain Name")

14. `ssh` into the instance using the `*.pem` file

![alt text](assets/access.png "EC2 Access")

```
$ chmod 400 demo-payment-server.pem # on computer with pem
$ ssh -i "demo-payment-server.pem" ubuntu@demo-payment-server.duckdns.org
```

15. Add your ssh key for normal access if you have one.

```
$ ls -al ~/.ssh
$ cat ~/.ssh/id_rsa.pub # on computer with key
```

 * copy the key from your computer and paste it on the server in the
 authorized_keys file.

```
$ vim ~/.ssh/authorized_keys # on server
```

 * exit `ctrl-d` and test accessing the server's global ip address

```
$ ssh ubuntu@demo-payment-server.duckdns.org # test login
```

16. Move to root user and add your key there as well.

```
$ sudo su # on server
$ vim ~/.ssh/authorized_keys # add your key
$ # ctrl-d ctrl-d to exit
$ ssh root@demo-payment-server.duckdns.org # test login
```

17. Install docker

```
# apt-get update
# apt-get upgrade
# apt install docker.io
# docker --version # check it installed correctly
# systemctl enable docker # enable docker
```

18. Get the install script, (With newest version number)

```
# curl -LO https://raw.githubusercontent.com/jmbott/demo-payment-server/0.0.6/prod/install.sh
```

19. Update the permissions on the install script

```
# chmod +x install.sh
```

20. Install using the script,

```
# ./install.sh
```
