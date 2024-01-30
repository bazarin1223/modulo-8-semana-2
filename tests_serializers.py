import datetime 
import pytest 
from model_bakery import baker 
from reserva.models import petshop
from rest_api.serializers import agendamentomodelserializer1

@pytest.fixture
def dados_agendamento_invalidos():
    ontem = datetime.date.today() - datetime.timedelta(days=1)
    petshop2 = baker.make(petshop)
    return {
        'nome':'kaique',
        'email':'kaique@gmail.com',
        'nome_pet':'pet_nome',
        'data':ontem,
        'turno':'manha',
        'tamanho': 1,
        'observaçoes':'',
        'petshop': petshop2.pk

    }
@pytest.mark.django_db
def test_data_agendamento_invalido(dados_agendamento_invalidos):

    serializers = agendamentomodelserializer1(data=dados_agendamento_invalidos) 

    assert not serializers.is_valid()

