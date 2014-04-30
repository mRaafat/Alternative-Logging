from django.shortcuts import render, render_to_response, RequestContext

# Create your views here.
def loginPage(request):
	return render_to_response("login.html",
		locals(),
		context_instance=RequestContext(request))