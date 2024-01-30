
import pytest 
from rest_framework.test import APIClient
from reserva.models import petshop
from model_bakery import baker 
from rest_api.serializers import agendamentoserializer2
from rest_api.tests.conftest import Agendamento2,Petshop2,dados_agendamento


@pytest.mark.django_db
def test_api_petshop_sem_petshop():
    client = APIClient()
    response = client.get('/api/petshop')
    assert len(response.data['results']) == 0

@pytest.mark.django_db
def test_api_petshop_com_petshop_salvo(Petshop2):
    client = APIClient()
    
    response = client.get('/api/petshop')
    assert len(response.data['results']) == 1
    assert response.data['results'][0]['nome'] == 'petshop de test'



@pytest.mark.django_db
def test_api_petshop_com_petshop_salvo_usando_serializers(Petshop2):
    client = APIClient()
  
    response = client.get('/api/petshop')
    serializer = agendamentoserializer2(petshop.objects.all(), many = True)


    assert response.data['results'] == serializer.data 


@pytest.mark.django_db
def test_api_agendamento_vazio():
    client = APIClient()
    response = client.get('/api/agendamento')
    assert len(response.data['results']) == 0

@pytest.mark.django_db
def test_api_com_agendamento_salvo(Agendamento):
    client = APIClient()
    response = client.get('/api/agendamento')
    assert len(response.data['results']) == 1
    assert response.data['results'][0]['nome'] == Agendamento.nome

@pytest.mark.django_db
def criar_agendamento(usuario,dados_agendamento):
    client = APIClient()
    response = client.post('/api/agendamento',dados_agendamento)
    client.force_authenticate(usuario)

    assert response.status_code == 201 








