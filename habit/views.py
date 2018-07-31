from django.views.generic import TemplateView


class HabitView(TemplateView):
    template_name = 'habit/list_habit.html'


class AddHabitView(TemplateView):
    template_name = 'habit/add_habit.html'

    def get_context_data(self, **kwargs):
        """Add STATIC_MEDIA_SERVER, current and USER_LOGGED_IN in context."""
        # form = AddClassificationForm(self.request)
        print('view caslled')
        context = super(AddHabitView, self).get_context_data(**kwargs)
        context.update({
            'form_header': 'Add New Habit',
            # 'form': form
        })

        return context

