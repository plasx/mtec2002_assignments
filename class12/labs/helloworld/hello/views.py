# Create your views here.
from django.template import Context, loader
from django.http import HttpResponse
def index(request):
		t = loader.get_template('hello/index.html')
		my_list =[' hi', 'hey', 'yo']
		
		d = {'greeting':'hola','my_list':my_list}
		c = Context(d)
		return HttpResponse(t.render(c))
def howdy(request):
		t = loader.get_template('hello/howdy.html')
		d = {}
		c = Context(d)
		return HttpResponse(t.render(c))