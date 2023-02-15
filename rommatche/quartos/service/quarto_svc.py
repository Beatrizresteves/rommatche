from ..models import Quarto


def add_quarto(new_quarto):
    quarto = Quarto(
        nome=new_quarto["nome"],
        cidade=new_quarto["cidade"],
        valorr=new_quarto["valorr"],
        description=new_quarto["description"],
        imagem=new_quarto["imagem"],
    )
    quarto.save()
    return quarto.Obsto_dict_json()


def list_quartos():
    quartos = Quarto.objects.all()

    return [quarto.to_dict_json() for quarto in quartos]
