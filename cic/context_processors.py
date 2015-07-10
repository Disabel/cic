from cic.apps.homepage.forms import boletinForm


def include_boletinForm(request):
	newsletter = True
	if request.method == 'POST':
		form = boletinForm(request.POST)
		if form.is_valid():
			form.save()
			newsletter = False
	else:
		form = boletinForm()
	return {'boletinform': form, 'newsletter': newsletter}
