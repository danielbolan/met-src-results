import jinja2
import json

with open("data/samples/calzada2015.json") as json_file:
    json_data = json.load(json_file)
    calzada2015 = list(json_data.keys())

with open("data/samples/validation.json") as json_file:
    json_data = json.load(json_file)
    validation = list(json_data.keys())

env = jinja2.Environment(loader=jinja2.FileSystemLoader("."))
template = env.get_template("index.jinja")
output = template.render(calzada2015=calzada2015, validation=validation)

with open("index.html", "w") as output_file:
    output_file.write(output)
