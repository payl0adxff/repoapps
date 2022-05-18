s = requests.Session()

s.get('https://astrobox.hotmart.com')
r = s.get('https://astrobox.hotmart.com/cookies')

print(r.text)
# '{"cookies": {"astrobox-token": "aiasdjijwijawebJsadnasdJJhasd.eyJqdGkiOiJUR1QtMzE3Mi1JalJUVlh2V3NBellOeHN4bUdyQzdLMkl3OVpadW43VHRVZ1NFcmpkVHdHMUY1UDZEaWZhNC0tUU0tU0l2QkUt"}}'
