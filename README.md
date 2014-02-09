twentytab-highlighter
=====================

A django app permits to highlight the searched words (self.query) in a long text and truncates it, counts number of chars == max_length


## Installation

Use the following command: <b><i>pip install twentytab-highlighter</i></b>


## Configuration

```py
INSTALLED_APPS = {
    ...,
    'highlighter',
    ...
}

```

## Usage

In your html template

```html
{% load highlight_tags %}

<!DOCTYPE html>
<html>
<head>
    <title></title>
</head>
<body>


{{a_very_long_text|highlight:"word"}}


</body>
</html>
```