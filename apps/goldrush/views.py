from django.shortcuts import render, HttpResponse, redirect

import random, datetime

# Create your views here.
def index(request):
	if not 'yourGold' in request.session:
		request.session['yourGold'] = 0
		request.session['result'] = None
		request.session['log'] = ""
	return render(request, "goldrush/index.html")

def process_money(request):
	if request.method == "POST":
		print ('*'*30)
		print (request.POST)
		print ('*'*30)
		time = datetime.datetime.today()
		current_time = time.strftime("%Y/%m/%d %H:%M %p")
		if request.POST['building'] == 'farm':
			gold = random.randrange(9, 21)
			request.session['yourGold'] += gold
			request.session['result'] = 'farm_gold'
			request.session['log'] += ("Earned " + str(gold) + " gold from the Farm! " + current_time + "\n")
		elif request.POST['building'] == 'saloon':
			gold = random.randrange(4, 11)
			request.session['yourGold'] += gold
			request.session['result'] = 'saloon_gold'
			request.session['log'] += ("Earned " + str(gold) + " gold from the Saloon! " + current_time + "\n")
		elif request.POST['building'] == 'river':
			gold = random.randrange(1, 6)
			request.session['yourGold'] += gold
			request.session['result'] = 'river_gold'
			request.session['log'] += ("Earned " + str(gold) + " gold from the River! " + current_time + "\n")
		elif request.POST['building'] == 'casino':
			gold = random.randrange(-51, 51)
			request.session['yourGold'] += gold
			if gold < 0:
				request.session['result'] = 'casino_gold_neg'
				gold = abs(gold)
				request.session['log'] += ("Lost " + str(gold) + " gold from the Casino! " + current_time + "\n")
			else:
				request.session['result'] = 'casino_gold_pos'
				request.session['log'] += ("Earned " + str(gold) + " gold from the Casino! " + current_time + "\n")
		return redirect('/')
	else:
		return redirect('/')

def reset(request):
	del request.session['yourGold']
	del request.session['result']
	del request.session['log']
	return redirect('/')