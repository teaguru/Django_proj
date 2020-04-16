from django.shortcuts import render
from django.views.decorators.http import require_GET

def index_page(request):
    response = render(request, 'homepage/index.html')
    response['MyCustomHeader'] = 'spam-and-eggs 42'
    return response


@require_GET
def articles(request):
    my_obj = MyClass()
    args = {'articles': list(range(1,5)), 'users':list([]), 'obj': my_obj}
    return render(request, 'homepage/articles.html', args)


class MyClass:
    foo = 42
    bar = 50


    def __repr__(self):
        return f'<MyClass {self.foo} {self.bar}>'
