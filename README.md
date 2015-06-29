##Logic in Templates Challenge

###Challenge
Change our h2 to wish our user a great day. First, write a list containing the “good day” messages. Then use the get method to read a new template variable called msg_times. This number will be passed to our template so it knows  how many “good day” messages to show.

* Add good_day_list to the HelloWorld handler
good_day_list = [“Have a Great Day”, “Have en god dag!”, “ “Bonne journée !”, “Que pase un buen día!”]

* Change the HelloWorld handler so that the new template variable msg_times can be read via the get method and passed to the template

* Add loop logic to your template so that 
`http://localhost:8080/helloworld?msg_num=2`
  Should show the first two messages:
  * Have a Great Day 
  * Have en god dag!

* Add a conditional statement so that
`http://localhost:8080/helloworld`
and
`http://localhost:8080/helloworld?msg_id=5`
get handled appropriately.


### Stretch Lab: 
Create a brand new template and handler called GoodbyeWorld that renders an entirely new template, goodbyeworld.html. 
* Include at least one conditional statement
* Pass data from the GoodbyeWorld handler via the GET method url
* Include a loop that prints outs Goodbye in many different languages. goodbye_list = [“Goodbye”,“Adios”, “Ciao”, “Arrivederci”]
* Make sure to edit the routes so that 
`http://localhost:8080/helloworld`
and
`http://localhost:8080/goodbyeworld`
go to two different places
