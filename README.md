# huffman-encoding

### This is a nameko microservice with the following rpc functions:
- squareOddNumbers([numbers])
- createEncodedDictionary([strings])
- decodeEncodedString(string)

### How to run

### In the root directory of the project run the following in your terminal:

```sh
$ docker-compose up
```
> This will start a rabbitmq service alongside the nameko miroservice

### How to call the functions

### Enter the nameko shell:
```sh
$ nameko shell
```
> The shell will send messages via the rabbitmq instance you started before

### Example Calls:

```sh
>>> n.rpc.engineering_assessment.squareOddNumbers(listOfNumbers=[343,2342,123,23,12])
```

```sh
>>> n.rpc.engineering_assessment.createEncodedDictionary(listOfStrings=["Potato","Luke","Skywalker"])
```

```sh
>>> n.rpc.engineering_assessment.decode(encodedString="1000111110000011011110110")
```