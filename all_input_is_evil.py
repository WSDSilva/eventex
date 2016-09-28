from django import forms


class AccountForm(forms.Form):
    what = forms.CharField(max_length=255)
    howmuch = forms.DecimalField(decimal_places=2)
    when = forms.SplitDateTimeField()


form = AccountForm()
print(form.as_p())

for field in form: print(str(field))

#Sanitização de dados válidos

VALID = dict(what= 'Meagasena', howmuch='1.99', when_0='28/09/2016', when_1='13:30')

form = AccountForm(VALID)

form.is_bound

form.is_valid()

form.cleaned_data

#Sanitização de dados inválidos

VALID = dict(what= 'Meagasena', howmuch='INVALIDO', when_0='28/09/2016', when_1='13:30')

form.errors


print(form.errors)

print(form.errors['howmuch'])

form.errors.as_data()

print(form.as_p())

for field in form: print(field)

for field in form: print(field, field.errors)

#BoundField vs Field

boundfield, field = form['howmuch'], form.fields['howmuch']

str(boundfield)

str(field)

field.clean('1.99')

boundfield = form['when']

boundfield.name

boundfield.label

boundfield.errors

#retorna os valores recebidos do dicionario de dados vindo da subimissão do form
boundfield.data

#retorna os valores que popula os widgets
boundfield.value()

boundfield.field

field = boundfield.field

widget = field.widget

widget.render('when', None)
#a expressão abaixo retorna um boundfield
#{{ form.when }}


# Renderizar uma formulário com dados iniciais
# Neste caso o formulário está undounded, pois os dados não são oriundos de submissão

INITIAL = dict(what='Megasena', howmuch='1.99')
form = AccountForm(initial=INITIAL)

