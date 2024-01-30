import pytest
from model_bakery import baker 
from reserva.models import reserva,petshop
import datetime
@pytest.fixture
def Agendamento2():
    return baker.make(reserva)

@pytest.fixture
def Petshop2():
    return baker.make(petshop , nome = 'petshop de test')

@pytest.fixture
def dados_agendamento():
    hoje = datetime.date.today()
    petshop2 = baker.make(petshop)
    return{
        'nome':'kaique',
        'email':'kaique@gmail.com',
        'nome_pet':'pet_nome',
        'data':hoje,
        'turno':'manha',
        'tamanho': 1,
        'observaçoes':'',
        'petshop': petshop2.pk

    }
@pytest.fixture
def usuario():
    return baker.make('auth.User')