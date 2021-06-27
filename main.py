"""
Basic example of a Mkdocs-macros module
"""

import math
import os

def read_file(filename):
    file = open(filename)
    line = file.read().replace("\n", " ")
    file.close()
    return line

def get_directories(path):
    f = []
    for (dirpath, dirnames, filenames) in os.walk(path):
        f.extend(dirnames)
        break
    return f

def get_files(path):
    f = []
    for (dirpath, dirnames, filenames) in os.walk(path):
        f.extend(filenames)
        break
    return f


def define_env(env):
    """
    This is the hook for defining variables, macros and filters

    - variables: the dictionary that contains the environment variables
    - macro: a decorator function, to declare a macro.
    - filter: a function with one of more arguments,
        used to perform a transformation
    """

    # add to the dictionary of variables available to markdown pages:
    env.variables['baz'] = "John Doe"

    # NOTE: you may also treat env.variables as a namespace,
    #       with the dot notation:
    env.variables.baz = "John Doe"

    @env.macro
    def bild(bilder, index):
        try:
            bilder
        except NameError:
            print ("keine bilder definiert")
            return ""
        bild = bilder[index]
        markup = []
        for key, value in bild.items():
            unterzeile = bild[key]["unterzeile"]
            format = bild[key]["format"]
            markup.extend(f'<span data-toggle="modal" data-target="#imageModal"><img class="bild {format}" src="bilder/{key}" alt="{unterzeile}"  data-target="#imageCarousel"  data-slide-to="{index}"/></span>')
        return "".join(markup)

    @env.macro
    def bar(x):
        return (2.3 * x) + 7

    # If you wish, you can  declare a macro with a different name:
    def f(x):
        return x * x
    env.macro(f, 'barbaz')

    # or to export some predefined function
    env.macro(math.floor) # will be exported as 'floor'


    # create a jinja2 filter
    @env.filter
    def reverse(x):
        "Reverse a string (and uppercase)"
        return x.upper()[::-1]


    @env.macro
    def person_links(file):
        dir_path = os.path.dirname(os.path.realpath(file.abs_src_path))
        directory_files = get_files(dir_path)
        markup = []
        markup.extend("<ul>")
        for directory_file in directory_files:
            if directory_file.find(".jpg") != -1:
                markup.extend("<li>")
                markup.extend("<img src=\"" + directory_file + "\"/>")
                markup.extend("</li>")
        markup.extend("</ul>")
        return "".join(markup);

    @env.macro
    def image_gallery(file, dirname, directories):
        dir_path = os.path.dirname(os.path.realpath(file.abs_src_path))
        markup = []
        markup.extend("<div class=\"m-0 p-0\">")
        markup.extend("<div class=\"row\">")
        for directory in directories:
            markup.extend("<a class=\"col-xl-4 col-md-6 person-link\" href=\"" + dirname + "/" + directory + "/kurz.html\">")
            markup.extend("<div class=\"container pl-0\">")
            markup.extend("<div class=\"row\">")
            markup.extend("<div class=\"col-6\">")
            person_path = dir_path + "/" + dirname + "/" + directory
            markup.extend("<img class=\"m-0\" src=\"" + dirname + "/" + directory + "/bilder/Abb 1.jpg\"" + "/>")
            markup.extend("</div>")
            markup.extend("<div class=\"p-0 col-6\">")
            name = read_file(dir_path + "/" + dirname + "/" + directory + "/name.txt")
            markup.extend("<h2>" + name + "</h2>")
            geburtsdaten = read_file(dir_path + "/" + dirname + "/" + directory + "/geburtsdaten.txt")
            markup.extend("<p>" + geburtsdaten + "</p>")
            beschreibung = read_file(dir_path + "/" + dirname + "/" + directory + "/beschreibung.txt")
            markup.extend("<p>" + beschreibung + "</p>")
            markup.extend("</div>")
            markup.extend("</div>")
            markup.extend("</div>")
            markup.extend("</a>")
        markup.extend("</div>")
        markup.extend("</div>")
        return "".join(markup);
