## **PROJECT DESCRIPTION**
___

This project makes use of RabbitMQ, which is a message broker where applications, services and systems can send and receive messages. The primary focus of this project is to produce DRY code for the tutorials. Each tutorial runs on the host, localhost, as such if a different host will be used then environment variables will need to be created.


## **RUNNING PROJECT**


1.  Set up virtual environment    
2.  Install dependencies


## **RABBITMQ INSTALLATION**


Follow this [link](https://www.rabbitmq.com/download.html) to install the RabbitMQ server on your local machine.

OR

Read through the instructions below to use a RABBITMQ container. 

Start up container.

*Windows*
```shell
$ docker-compose up
```

*Linux/MacOS*
```shell
$ docker compose up
```

## **RUNNING TUTORIALS**


### **ONE**

*shell 1*
```sh
$ python one/receive.py
```
*Output*:
```
[*] Waiting for messages. To exit press CTRL+C
```
*Output after running send.py*:
```
[x] Received 'Hello World!'
```
*shell 2*
```sh
$ python one/send.py
```
*Output*:
```
[x] Sent 'Hello World!'
```
#### **TWO**

*shell 1*
```sh
$ python two/worker.py
```
*Output*:
```
[*] Waiting for messages. To exit press CTRL+C
```
*Output after running shell 3*:
```
[x] Received 'First message.'
[x] Done
```
*shell 2*
```sh
$ python two/worker.py
```
*Output*:
```
[*] Waiting for messages. To exit press CTRL+C
```
*Output after running shell 3*:
```
[x] Received 'Second message..'
[x] Done
```
*shell 3*
```sh
$ python two/new_task.py First message.
$ python two/new_task.py Second message..
```
#### **THREE**

*shell 1*
```sh
$ python three/receive_logs.py
```
*Output*:
```
[*] Waiting for logs. To exit press CTRL+C
```
*Output after running emit_log*:
```
[x] 'info: Hello World!'
```
*shell 2*
```sh
$ python three/emit_log.py
```
*Output*:
```
[x] Sent 'info: Hello World!'
```
#### **FOUR**

*shell 1*
```sh
$ python four/receive_logs_direct.py info warning error
```
*Output*:
```
[*] Waiting for logs. To exit press CTRL+C
```
*Output after running emit_log_direct*:
```
[x] 'error':'Run. Run. Or it will explode.'
```
*shell 2*
```sh
$ python four/emit_log_direct.py error "Run. Run. Or it will explode."
```
*Output*:
```
[x] Sent 'error':'Run. Run. Or it will explode.'
```
#### **FIVE**

*shell 1*
```sh
$ python five/receive_logs_topic.py "kern.*" "*.critical"
```
*Output*:
```
[*] Waiting for logs, To exit press CTRL+C
```
*Output after running emit_log_topic*:
```
[x] 'kern.critical':'A critical kernel error'
```
*shell 2*
```sh
$ python five/emit_log_topic.py "kern.critical" "A critical kernel error"
```
*Output*:
```
[x] Sent 'kern.critical':'A critical kernel error'
```
#### **SIX**

*shell 1*
```sh
$ python six/rpc_server.py
```
*Output*:
```
[x] Awaiting RPC requests
```
*Output after rpc_client*:
```
[.] fib(30)
```
*shell 2*
```sh
$ python six/rpc_client.py
```
*Output*:
```
[x] Requesting fib(30)
[.] Got 832040
```

## **LICENCE**


RabbitMQ (190)
For raw project instructions see: http://syllabus.africacode.net/projects/rabbitmq/
