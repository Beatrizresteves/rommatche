from ..models import Quarto


def add_quarto(new_quarto):
    quarto = Quarto(
        nome=new_quarto,
        cidade=new_quarto,
        valorr=new_quarto,
        description=new_quarto,
        imagem=new_quarto,
    )
    quarto.save()
    return quarto.to_dict_json()


def list_quartos():
    quartos = Quarto.objects.all()

    return [quarto.to_dict_json() for quarto in quartos]
