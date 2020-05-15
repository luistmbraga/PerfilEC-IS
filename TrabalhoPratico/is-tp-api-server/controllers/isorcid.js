var Publicacoes = require('../models/publicacoes')
var Users = require('../models/users') 

const ISORCID = module.exports

var ObjectId = require('mongodb').ObjectID

ISORCID.getUsers = () => {
    return Users
            .find()
            .exec()
}

ISORCID.getUser = (id) => {
    return Users
            .find({"_id" : id})
            .exec()
}

ISORCID.getPublicacao = (id) => {
    return Publicacoes
            .find({"_id" : id})
            .exec()
}

