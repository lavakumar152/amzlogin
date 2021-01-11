import mechanize

br = mechanize.Browser()
br.set_handle_robots(False)
br.addheaders = [('User-agent', 'Chrome')]
br.open('https://www.facebook.com/login.php')
br.select_form(nr = 0)
br.form['email'] = 'giri.kumar.98284'
br.form['pass'] = 'girikumar10'
sub = br.submit()
print (sub.geturl())