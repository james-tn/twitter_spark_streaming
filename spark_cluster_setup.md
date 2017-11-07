# Apache Spark Streaming Setup Guide


## Provision machines

Provision three Centos 7 VSes in SoftLayer with 2 CPUs, 4GB RAM and a 100GB local hard drive. Name them spark1, spark2, and spark3.

## Configure connectivity between machines

Configure spark1 such that it can SSH to spark1, spark2, and spark3 without passwords using SSH keys, and by name).

## Install Java, SBT, and Spark on all nodes

Install packages:

```
curl https://bintray.com/sbt/rpm/rpm | sudo tee /etc/yum.repos.d/bintray-sbt-rpm.repo
yum install -y java-1.8.0-openjdk-devel sbt git
```
Set the proper location of JAVA_HOME and test it:

```
echo export JAVA_HOME=\"$(readlink -f $(which java) | grep -oP '.*(?=/bin)')\" >> /root/.bash_profile
source /root/.bash_profile
$JAVA_HOME/bin/java -version
```
Download and extract a recent, prebuilt version of Spark (link obtained from ):

```
curl https://d3kbcqa49mib13.cloudfront.net/spark-2.1.1-bin-hadoop2.7.tgz | tar -zx -C /usr/local --show-transformed --transform='s,/*[^/]*,spark,'
```
For convenience, set $SPARK_HOME:

```
echo export SPARK_HOME=\"/usr/local/spark\" >> /root/.bash_profile
source /root/.bash_profile
```


## Configure Spark

On __spark1__, create the new file `$SPARK_HOME/conf/slaves` and content:

    spark1
    spark2
    spark3

From here on out, all commands you execute should be done on __spark1__ only. You may log in to the other boxes to investigate job failures, but you can control the entire cluster from the master. If you plan to use the Spark UI, it's convenient to modify your workstation's `hosts` file so that Spark-generated URLs for investigating nodes resolve properly.  Also, review /etc/hosts on spark1 and see if you have the 127.0.0.1 spark1 line as the first one mentioning your node name.  If that is the case, comment it out and replace it with <ip_address spark1> where the ip address is either the internal or external ip address of your node.  If you leave it as is, your slave nodes may not be able to connect to the master node when the cluster comes up.

## Start Spark from master

Configure Spark

On spark1, create the new file $SPARK_HOME/conf/slaves and content:

```
spark1
spark2
spark3
```
From here on out, all commands you execute should be done on spark1 only. You may log in to the other boxes to investigate job failures, but you can control the entire cluster from the master. If you plan to use the Spark UI, it's convenient to modify your workstation's hosts file so that Spark-generated URLs for investigating nodes resolve properly.

## Copy files to master

From spark1, clone the homework repo into /root.  Locate and note the directory containing the file moby10b.txt and the directory src; they should be in the directory /root/coursework/week6/hw/apache_spark_introduction.


## Start Spark from master

Once you’ve set up the conf/slaves file, you can launch or stop your cluster with the following shell scripts, based on Hadoop’s deploy scripts, and available in $SPARK_HOME/:

```
sbin/start-master.sh - Starts a master instance on the machine the script is executed on
sbin/start-slaves.sh - Starts a slave instance on each machine specified in the conf/slaves file
sbin/start-all.sh - Starts both a master and a number of slaves as described above
sbin/stop-master.sh - Stops the master that was started via the bin/start-master.sh script
sbin/stop-slaves.sh - Stops all slave instances on the machines specified in the conf/slaves file
sbin/stop-all.sh - Stops both the master and the slaves as described above
```
Start the master first, then open browser and see http://<master_ip>:8080/:

```
$SPARK_HOME/sbin/start-master.sh

starting org.apache.spark.deploy.master.Master, logging to /root/spark/sbin/../logs/spark-root-org.apache.spark.deploy.master.Master-1-spark1.out
```
Then, run the start-slaves script, refresh the window and see the new workers (note that you can execute this from the master).
```
$SPARK_HOME/sbin/start-slaves.sh

spark1: starting org.apache.spark.deploy.worker.Worker, logging to /usr/local/spark/sbin/../logs/spark-root-org.apache.spark.deploy.worker.Worker-1-spark1.out
spark3: starting org.apache.spark.deploy.worker.Worker, logging to /usr/local/spark/sbin/../logs/spark-root-org.apache.spark.deploy.worker.Worker-1-spark3.out
spark2: starting org.apache.spark.deploy.worker.Worker, logging to /usr/local/spark/sbin/../logs/spark-root-org.apache.spark.deploy.worker.Worker-1-spark2.out
```
