from sqlalchemy import create_engine, ForeignKey, Column, String, Integer, Enum, Text, DateTime, datetime
from sqlalchemy.orm import declarative_base

engine = create_engine("sqlite:///database.db")

base = declarative_base()

class Tipo_Usuario_Sistema(base):
    __tablename__ = 'tipo_usuario_sistema'
    ID_tipo_usuario_sistema = Column(Integer, primary_key = True)
    Nome_tipo_usuario_sistema = Column(String, nullable = False)
    Descricao_tipo_usuario_sistema = Column(String, nullable = True)

class Tipo_Usuario_Cliente(base):
    __tablename__ = 'tipo_usuario_cliente'
    ID_tipo_usuario_clinte = Column(Integer, primary_key = True)
    Nome_tipo_usuario_clinte = Column(String, nullable = False)
    Descricao_tipo_usuario_clinte = Column(String, nullable = True)

class Usuario(base):
    __tablename__ = 'usuario'
    ID_usuario = Column(Integer, primary_key = True)
    Nome_usuario = Column(String, nullable = False)
    Tipo_usuario = Column(Integer, nullable = False)
    Email_usuario = Column(String, nullable = False)
    Senha_usuario = Column(String, nullable = False) 
    Afiliacao_usuario = Column(String, nullable = False)


if __name__ == '__main__':
    base.metadata.create_all(engine)