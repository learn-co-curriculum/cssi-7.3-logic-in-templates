## Lesson Notes
###Syntax
To add logic to a template, variables go between mustaches `{{variables}}` and code is embedded between curly brackets and percent signs {% code %}
```python
<h1>{{name}}'s cart </h1>
<table>
  {% for item in items:%}
    <tr>
      <td>{{ item }}</td>
    </tr>
    {% endfor %}
</table>
```

### Looping through Dictionaries
```python
# template variale in main.py
template_vars = {"pets" : {'willie':'horse', 'wilbur':'pig'}}
#in pets.html
<table>
      {% for key, value in pets.items() %}
            <tr>
              <td>{{key}}</td>
              <td>{{value}}</td>
            </tr>
      {% endfor %}
</table>

```
### Looping through Nested Dictionaries
```python
# a template variable, pets in main.py

template_vars = {"pets" : {'willie': {'kind': 'dog', 'owner': 'eric'},
        'walter': {'kind': 'cockroach', 'owner': 'eric'},
        'peso': {'kind': 'dog', 'owner': 'chloe'},}}

# in  pets.html
<h1> Our pets</h1>
{% for pet_name, pet_information in pets.items() %}
    <p>
     {{pet_name.title()}} is a {{pet_information['kind']}} who is owned by {{pet_information['owner']}}.
    </p>
{% endfor %}
```

###Logic in Templates Challenge
###Challenge
Change our `<h2>` to wish our user a great day. First, write a list containing the “good day” messages. Then read a new template variable called `msg_times` from a query parameter. This number will be passed to our template so it knows  how many “good day” messages to show.

* Add good_day_list to the HelloWorld handler
good_day_list = ["Have a Great Day", "Have en god dag!", "Bonne journee !", "Que pase un buen dia!"]

* Change the HelloWorld handler so that the new template variable, `msg_times` can be read from a query parameter and passed to the template.

* Add loop logic to your template so that
`http://localhost:8080/helloworld?msg_num=2`
  Should show the first two messages:
  * Have a Great Day!
  * Have en god dag!

* Add a conditional statement so that
`http://localhost:8080/helloworld`
and
`http://localhost:8080/helloworld?msg_id=5`
get handled appropriately.


### Stretch Lab:
Create a brand new template and handler called GoodbyeWorld that renders an entirely new template, goodbyeworld.html.
* Include at least one conditional statement
* Pass data from the GoodbyeWorld handler via a query parameter in the url
* Include a loop that prints outs 'Goodbye' in many different languages. goodbye_list = ["Goodbye","Adios", "Ciao", "Arrivederci"]
* Make sure to edit the routes so that
`http://localhost:8080/helloworld`
and
`http://localhost:8080/goodbyeworld`
go to two different places

<a href='https://learn.co/lessons/cssi-7.3-logic-in-templates' data-visibility='hidden'>View this lesson on Learn.co</a>
