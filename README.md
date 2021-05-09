

- python -m pip install Django==3.2
- py -3 manage.py startapp catalog or py manage.py startapp catalog

### MDN Local Library Project
Project synopsis: A website that manages the catalog of library books

(Reference: MDN Django)[https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django]

### Part 2: The skeleton
```
locallibrary__ 
             |
            __init__.py
            asgi.py
            settings.py
            urls.py
            wsgi.py
manage.py

```

### Part 3: Models
When designing `Models`, it makes sense to have separate models for every `object`(a group of related information). In this case the obvious objects are books, book instance, and authors.

We might also want to use models to present selection-list options(eg. like a drop down list of options) if we aren't sure of all the available options we need so that we don't hard code options. Options could be `book genre (eg. poetry, scifi, adventure, etc)` or `language (English, Arabic, Spanish)`

### Brief Intro to Models
Models usually have these 3 things: `fields`, `methods`, and `metadata`. 

### Fields:
- `Field types`: Example are, `CharField, TextField, Interfield, DateField`

- `Field arguments`: Examples are, `help_text, verbose_name, null, blank, choices, etc`.

### Methods:
Methods are functions in a class. It is a standard practice to always declare the `__stri__()` in every model to return a human-readable string for each object. 

This string is used to represent individual records in the administration site (and anywhere else you need to refer to a model instance). Often this will return a title or 
name fielf from the model. 
- Syntax:

``
def __str__(self):
    return self.field_name
``

- Another common method is `get_absolute_url()`. This method returns a URL for displaying individual model records on the website. 
Syntax:

```
def get_absolute_url(self):
    '''returns the url to a particular instance of the model'''

    return reverse('detail-view', args=[str(self.id)])

```

- The `reverse()` function is able to reverse your url mapper, i.e converting a `view` to a `url`. The usual way is converting `url ==> view`. Now this case is the opposite, thus the use of the function `reverse()`



### Metadata
You can declare model-level metadata for your Model by declaring `class Meta`. Example
```
class Meta:
    ordering = ['-date_purchased']
```
The `ordering` attribute is used in sorting your records when the model is queried. Ordering depends on the type of field. `Character fields` are sorted alphabetically while `Date fields` are sorted in chronological order

- Prefixing the field name with a minus symbol `(-)` reverses the sorting order.
- Example:

```
ordering = ['title', '-pub_date']

```
- The above means, `title` is sorted in alphabetical order for A-Z and `pub_date` by descending order, from latest to oldest

### Filtering Models
- The fields to match and the type of match are defined in the filter parameter name, using the format `field_name__match_type`. Take note of double underscore

- Example: `good_books = Book.objects.filter(title__contains='api')`.

- `field_name ==> title` AND `match_type ==> contains`

- Examples of matches types are: `contains (case-insentive)` and `icontains(case-insentitive)`


Take the following code for example. 

```

```