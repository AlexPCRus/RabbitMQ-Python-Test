# RabbitMQ-Python-Test

A small publish -> rabbitmq -> consume test.  

## Requirements

docker or docker desktop must be installed

## Commands

Run:  docker-compose up -d --build  
Log:  docker-compose logs -f  
Stop: docker-compose down  

## Settings

- a time delay between two published messages must be set in ./setting/publish_delay.cfg file (in seconds)  
- a time delay between two consumed messages must be set in ./setting/consume_delay.cfg file (in seconds)  
