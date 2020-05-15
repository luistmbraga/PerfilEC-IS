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
  isbn: {type: String},
  numero_citacoes : {type : Number},
  numero_citacoes_ultimos_3_anos : {type : Number},
  SJR : {type: Number}
})

module.exports = mongoose.model('publicacoes', publicacaoSchema)