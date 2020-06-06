var express = require('express');
var router = express.Router();
var ISORCID = require('../controllers/isorcid')

/* GET users */
router.get('/users', function(req, res, next) {
  ISORCID.getUsers()
         .then(dados => res.jsonp(dados))
         .catch(erro => res.status(500).jsonp(erro))
});


/* GET user information */
router.get('/users/:userid', function(req, res, next) {
  ISORCID.getUser(req.params.userid)
  .then(dados => res.jsonp(dados))
  .catch(erro => res.status(500).jsonp(erro))
});

/* GET publication information */
router.get('/publicacoes/:idPublicacao', function(req, res, next) {
  ISORCID.getPublicacao(req.params.idPublicacao)
  .then(dados => res.jsonp(dados))
  .catch(erro => res.status(500).jsonp(erro))
})



module.exports = router;
