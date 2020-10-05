from django.views.generic import TemplateView

class PageView(TemplateView):
	template_name = 'page.html'

class PageOneView(TemplateView):
	template_name = 'page-1.html'

class PageTwoView(TemplateView):
	template_name = 'page-2.html'
	def get_context_data(self, *args, **kwargs):
		context = super(PageTwoView, self).get_context_data(*args, **kwargs)
		context['name'] = 'Gryffindor'
		context['id'] = '1'
		return context

