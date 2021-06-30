# nyt-xml-parser 
- Based on: [so-xml-parser](https://github.com/simonwiles/so-xml-parser)

- Installing with `pipenv install` is recommended. Or `pip install -r requirements.txt`

- Output is as follows (see [`config.yaml`](config.yaml)).

```
$ ./parse.py && sqlite3 -header output.sqlite "SELECT * FROM articles;"

id|title|date|paragraphs
100000002487615|Afghanistan’s Worsening, and Baffling, Hunger Crisis|20140104T000000|LASHKAR GAH, Afghanistan — In the Bost Hospital here, a teenage mother named Bibi Sherina sits on a bed in the severe acute malnutrition ward with her two children. Ahmed, at just 3 months old, looks bigger than his emaciated brother Mohammad, who is a year and a half and weighs 10 pounds. In another bed is Fatima, less than a year old, who is so severely malnourished that her heart is failing, and the doctors expect that she will soon die unless her father is able to find money to take her to Kabul for surgery. The girl’s face bears a perpetual look of utter terror, and she rarely stops crying. Half of the other children in the ward are crying as well, a cacophony that rarely pauses. Afghan hospitals like Bost, in the capital of war-torn Helmand Province, have been registering significant increases in severe malnutrition among children. Countrywide, such cases have increased
...

```
