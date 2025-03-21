from django.views.generic import ListView
from .models import EmployeeModel

class IndexView(ListView):
    model = EmployeeModel
    queryset = EmployeeModel.objects.all().order_by('-id')
    template_name = 'pages/index.html'
    context_object_name = 'employees'
    
    # PAGINAÇÃO
    paginate_by = 5