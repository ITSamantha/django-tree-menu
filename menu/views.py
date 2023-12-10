from django.views.generic import TemplateView

from menu.models import Menu


class IndexPageView(TemplateView):
    template_name = 'menu/index.html'

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        context['menu'] = Menu.objects.get(slug=context['menu']) if 'menu' in context else Menu.objects.first()
        context['item'] = context['item'] if 'item' in context else ""
        return context
