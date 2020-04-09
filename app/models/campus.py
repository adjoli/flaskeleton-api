from .db import db, ma
from sqlalchemy import Column, Integer, String
from marshmallow import fields


class Campus(db.Model):

    __tablename__ = "CAMPUS"

    codigo = Column(Integer, name="CODIGO", primary_key=True)
    descricao = Column(String, name="DESCRICAO")

    def __repr__(self):
        return "<Campus codigo={codigo}, descricao={descricao}>".format(
            codigo=self.codigo, descricao=self.descricao
        )


class CampusSchema(ma.ModelSchema):
    class Meta:
        strict = True
        model = Campus
        sqla_session = db.session

    codigo = fields.Integer(dump_only=True)
    descricao = fields.String(required=True, error_messages={"required": "`descricao` é um atributo necessário."})
