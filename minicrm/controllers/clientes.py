# coding: utf8
# intente algo como
def index(): return dict(message="hello from clientes.py")

def nuevo():
	formulario= SQLFORM(db.clientes)
	return dict(form=formulario)