# cvweaver

A simple CV tool to keep data and logic separated. 

# Quick start

1. Check that [uv](https://docs.astral.sh/uv/getting-started/installation/) is installed.
2. Edit `data/cv.yaml` and input your data.
3. Run `uv run cvweaver`, it will output a `cv.tex` file.

The initial version only supports LaTeX output. Notice that you
will need to compile the `cv.tex` file into a PDF yourself as
LaTeX compilation is outside the scope of cvweaver.

# How it works

The script reads the CV data from a YAML file and
outputs a file with the CV contents following a
given template.

The default files are in:

- data: 'data/cv.yaml'
- template: 'templates/latex.tpl'

and the data file contains dummy data as an example.

The script is supposed to be run using
[uv](https://docs.astral.sh/uv/getting-started/installation/) like:

```
uv run cvweaver
```

As there is separation of concerns between data and logic,
you can add as many data files as you need. For example, in
case you want to have the CV in different languages or for
different roles.

It's also possible to use different templates and output
in different formats.

Run

```
uv run cvweaver --help
```

and it will show the arguments needed if you want to use
anything different to the default.

# Data sections

The default template expects the sections in the default data,
namely:

- _profile_: personal data
- _summary_: short text about yourself
- _experience_: professional experience
- _skills_: skills, certificates
- _education_: academic life
- _training_: additional training for professional advancement
- _voluntary_: voluntary work

There is an extra section _setup_, to choose language. It can also
has a value `babel` set to be passed to the LaTeX package. You can
leave it out and it will default to english.


The data structure in the example file fits the template,
so I suggest you make a copy and edit it.

Of course, you can create your own template and data pairs
if you want to, but the default template is meant to be
easy to parse automatically by ATS or similar.
