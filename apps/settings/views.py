from django.shortcuts import render

import requests
from bs4 import BeautifulSoup




def settings(request):
    BANK = "https://www.nbkr.kg/index.jsp?lang=RUS" 
    headers = {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36' }  # my user agent
    if request.method == 'POST':
        amount = float(request.POST['amount'])
        full_page = requests.get(BANK, headers=headers)

        soup = BeautifulSoup(full_page.content, 'html.parser')

        currency = request.POST['currency']
        convert = soup.find_all("td", {"class": "excurr", "class": "exrate"})   
        usd = float(convert[0].text.replace(',', '.'))
        eur = float(convert[2].text.replace(',', '.'))
        rub = float(convert[4].text.replace(',', '.'))
        kzt = float(convert[6].text.replace(',', '.'))


       
        if currency == 'USD':
            result = amount / usd
        elif currency == 'EUR':
            result = amount / eur
        elif currency == 'RUB':
            result = amount / rub
        elif currency == 'KZT':
            result = amount / kzt
        else:
            result = 0.0
        
        context = {
            'amount': amount,
            'currency': currency,
            'result': result
        }
        
        return render(request, 'index.html', context)
    
    return render(request, 'index.html')
