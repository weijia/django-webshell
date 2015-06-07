import commands
import subprocess

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import permission_required


@csrf_exempt
@require_POST
@permission_required('is_superuser')
def execute_script_view(request):
    source = request.POST.get('source', '').replace('"', r'\"')
    # result = commands.getoutput('python -c "%s"' % source)
    result = subprocess.check_output('python -c "%s"' % source)
    # result = eval(source)
    return HttpResponse(result)