const mongoose = require('mongoose')
var Schema = mongoose.Schema


var publicacaoSchema = new Schema({
  _id : {type: String, required: true},
  titulo : {type: String, required: true},
  eid : {type: String},
  doi : {type: String},
  wos : {type: String},
  local_de_publicacao : {type: String},
  ano : {type: Number},
  autores :  [String],
  numero_citacoes : {type: Number},
  issn : {type: String},
  souce_id_issn : {type: String},
  numero_citacoes : {type : Number},
  SJR : {type: String}
})

module.exports = mongoose.model('publicacoes', publicacaoSchema)