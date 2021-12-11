from django.http import HttpResponse
from django.shortcuts import render
import re


class MyClass:
    string = ''

    def __init__(self, s):
        self.string = s


def index(request):
    my_num = 33
    my_str = 'some string'
    my_dict = {"some_key": "some_value"}
    my_list = ['list_first_item', 'list_second_item', 'list_third_item']
    my_set = {'set_first_item', 'set_second_item', 'set_third_item'}
    my_tuple = ('tuple_first_item', 'tuple_second_item', 'tuple_third_item')
    my_class = MyClass('class string')
    return render(request, 'index.html', {
        'my_num': my_num,
        'my_str': my_str,
        'my_dict': my_dict,
        'my_list': my_list,
        'my_set': my_set,
        'my_tuple': my_tuple,
        'my_class': my_class,
        'display_num': True
    })


def test(request):
    return HttpResponse("TEST")


def main(request):
    return HttpResponse("Hey! It's your main view!!")


def article_main(request):
    return HttpResponse(f"It`s article main")


def article_archive_main(request):
    return HttpResponse(f"It`s article/archive main")


# ------------------------


def articles(request, article_id):
    return HttpResponse(f"It`s article: №{article_id}!")


def articles_archives(request, articles_archives_id):
    return HttpResponse(f"It`s articles/archives: {articles_archives_id}!")


def articles_name(request, article_id, name=''):
    return HttpResponse(f"It`s article: №{article_id}. Name of this article: {name}")


# ------------------------


def users_main(request):
    return HttpResponse("It`s users!")


def users(request, user):
    return HttpResponse(f"It`s user: {user}!")


# ------------------------

def main_regex(request, num):
    pattern = r'(?:[a-f]|\d){4}-(?:[a-f]|\d){6}'
    match = re.match(pattern, num)
    if match is not None:
        return HttpResponse(f'{num} was found')
    return HttpResponse(f'{num} was not found')


def num_tel(request, num):
    pattern = r'0(?:39|67|68|96|97|98|50|66|95|99|63|93|91|92|94)+\d{6}'
    match = re.match(pattern, num)
    if match is not None:
        return HttpResponse(f'{num} was found')
    return HttpResponse(f'{num} was not found')
