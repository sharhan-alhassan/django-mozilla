

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
### Part 4: Django Admin Site
### Admin Site

- Usually `list_display` field is used to list the fields of a model in the `Admin Site` to properly view data from those fields

- Unfortunately, a field with `ManyToManyField` relationship can not be used in the `list_display` from the Admin model in the `admin.py` because Django won't allow that. 

- Django doesn't allow that because there'll be a large database access COST. 

- To get around in displaying data from `ManyToManyField` relationship field, create a function to get the information as a string

- Let's create a function called `display_genre` int he `Book` model

python 
```

def display_genre(self):
    return ', '.join(genre.name for genre in self.genre.all()[:3])

display_genre.short_description = 'Genre'

```

- Likewise, you can apply filtering to the Model in the Admin area with the `list_filter` field. This feature adds a filter bar on the right. 

- In the admin site, fields are displayed vertically by default, but will display horizontally if you group them in a tuple. Example:
1. `Vertical display: list_display = ['fname', 'lname', 'age']`

2. `Horizontal display: list_display = ('fname', 'lname', 'age')`

### Sectioning a Detail view on the Admin site

- You can add `"sections"` to group related model information within the detail form, using the `fieldsets` attribute.

- In the `BookInstance` model we have information related to what the book is `(i.e. name, imprint, and id)` and when it will be a`vailable (status, due_back)`. We can add these in different sections by adding the text in bold to our BookInstanceAdmin class. 

```
fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back')
        }),
    )
```
- section 1 has no title, section 2 has a title called availability



### Part 5: Creating Home Page



### Part 6: General Lists and Detail Views
- Two generic views are `List` and `Detail`
- without `queryset` set, the List view will automatically generate the List for. However, you can overide this by explicitly declaring `queryset` or better still using the method `get_queryset()`. Syntax:
    ```def get_queryset(self):
        return ...
    ```
- You can add extra data to the list of objects. It returns context data for displaying the list of objects. `get_context_data(self, **kwargs)`
Syntax:

```
def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(BookListView, self).get_context_data(**kwargs)
        # Create any data and add it to the context
        context['some_data'] = 'This is just some data'
        return context
```

Steps in creating a `get_context_data()`:
1. First get the existing context from our superclass
2. Then add your new context information
3. Then return the new(updated) context 


### Regular expressions for URL mapping
- Sintax of `re` is: `r'<regular expression goes here>`

### How to get choices from `choices field`
- If you have a choices field with attribute = `status` and a model name `BookInstance`. 
- Django automatically creates a method `get_FOO_display()` for every choices field `FOO` in a model, which can be used to get the current value of the field.
- The method here is : `get_status_display()`


### Pagination:
- Use `paginate_by` attribute on the view handler (class view).
- The different pages are accessed using `GET` parameters -- to access page 2 you would use the URL `books/?page=2`
- To to add this functionality to the template, we might choose to do this in the `base_generic` template

- The `page_obj` is a Paginator object that will exist if pagination is being used on the current page. It allows you to get all the information about the `current page, previous pages, how many pages there are`, etc. 


### Sessions framework
- Objective of session: `The session framework lets you implement features at user level, allowing you to store and retrieve arbitrary data on a per-site-visitor basis. `
 
- **Django uses a cookie containing a special session id to identify each browser and its associated session with the site. The actual session data is stored in the site database by default (this is more secure than storing the data in a cookie, where they are more vulnerable to malicious users). You can configure Django to store the session data in other places (cache, files, "secure" cookies), but the default location is a good and relatively secure option.**


### Part 9: FORMS

- If a form is valid, then we can start to use the data, accessing it through the `form.cleaned_data` attribute (e.g. `data = form.cleaned_data['renewal_date'])`. Here we just save the data into the `due_back` value of the associated `BookInstance` object.
- ### Warning:
- While you can also access the form data directly through the request (for example, `request.POST['renewal_date']` or `request.GET['renewal_date']` if using a GET request), this is `NOT` recommended. The cleaned data is sanitized, validated, and converted into Python-friendly types.