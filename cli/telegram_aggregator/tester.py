string_val = "Я ПОМНЮ ЧУДНОЕ МГНОВЕНЬЕ<br><br>Я помню чудное мгновенье:<br>Передо мной явилась ты,<br>Как мимолетное виденье,"

string_val = "\n".join(string_val.split("<br>"))
print(string_val)