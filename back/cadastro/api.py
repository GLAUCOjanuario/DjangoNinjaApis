from ninja import ModelSchema, NinjaAPI, Schema, UploadedFile

from cadastro.schemas import LivroSchema
from .models import Livro
from django.shortcuts import get_object_or_404
from django.forms.models import model_to_dict # convertendo um model para um dicionario do python
api = NinjaAPI()

@api.get('livro/')
def listar(request):
  livros = Livro.objects.all()
  response = [{'id': i.id, 'titulo': i.titulo, 'descricao': i.descricao, 'autor': i.autor} for i in livros]
  print(response)
  
  return response

@api.get('livro/{int:id}')
def listar_livro(request, id):
  livro = get_object_or_404(Livro, id=id) # get por id
  
  return model_to_dict(livro)

@api.get('livro-consulta/') 
def listar_consultar(request, id: int = 1):
  livro = get_object_or_404(Livro, id=id)

  return model_to_dict(livro)
  

'''class LivroSchema(Schema):
  titulo: str
  descricao: str
  autor: str = None '''
  
'''class LivroSchema(ModelSchema):
  class Config:
    model = Livro
    model_fields = '__all__' '''
  
@api.post('livro', response=LivroSchema)
def criar_livro(request, livro: LivroSchema):
  livro =  Livro(**livro.dict()) 
  livro.save()
  return livro

@api.post('/files')
def file_upload(request, file: UploadedFile):
  
  return
