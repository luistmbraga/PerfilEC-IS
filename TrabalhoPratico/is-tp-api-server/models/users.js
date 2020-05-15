const mongoose = require('mongoose')
var Schema = mongoose.Schema

var pubAuxSchema = new Schema({
    _id : {type: String, required: true},
    nome : {type : String},
    ano : {type: Number} 
})

var userSchema = new Schema({
    _id : {type: String, required: true},
    nome : {type: String},
    publicacoes: [pubAuxSchema]
})

module.exports = mongoose.model('utilizadores', userSchema)
