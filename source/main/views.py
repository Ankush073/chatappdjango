from django.views.generic import TemplateView
from django.contrib.auth.models import User

class IndexPageView(TemplateView):
    template_name = "main/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Query all users and add to context
        context['all_users'] = User.objects.all()
        return context
class ChangeLanguageView(TemplateView):
    template_name = "main/change_language.html"


class CHAT(TemplateView):
    template_name = "main/chat.html"



