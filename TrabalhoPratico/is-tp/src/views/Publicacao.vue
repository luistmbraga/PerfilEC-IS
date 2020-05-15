<template>
  <div class="home">
    <v-card-title class="justify-center">
        Publicação {{publicacao.titulo}}
    </v-card-title>
    <div v-if="infoPublicacao == undefined"/>
    <v-container v-else>
            <v-row class="justify-center">
                <v-col
                    cols="15"
                    sm="12"
                >
                <v-layout row wrap>
                    <v-flex xs6>
                    <v-text-field
                    v-model="infoPublicacao.ano"
                    label="Ano de pulbicação"
                    outlined
                    disabled
                    />
                    </v-flex>
                    <v-flex xs6>                
                    <v-text-field
                    v-model="infoPublicacao.SJR"
                    label="Classificação SJR"
                    outlined
                    disabled
                    />
                    </v-flex>
                </v-layout>
                <v-layout row wrap>
                    <v-flex xs6>
                    <v-text-field
                    v-model="infoPublicacao.eid"
                    label="EID"
                    outlined
                    disabled
                    />
                    </v-flex>
                    <v-flex xs6>
                    <v-text-field
                    v-model="infoPublicacao.doi"
                    label="DOI"
                    outlined
                    disabled
                    />
                    </v-flex>
                </v-layout>
                <v-layout row wrap>
                    <v-flex xs6>
                    <v-text-field
                    v-model="infoPublicacao.wos"
                    label="WOS"
                    outlined
                    disabled
                    />
                    </v-flex>
                    <v-flex xs6>                
                    <v-text-field
                    v-model="infoPublicacao.local_de_publicacao"
                    label="Local da Publicação"
                    outlined
                    disabled
                    />
                    </v-flex>
                </v-layout>
                    <v-layout row wrap>
                    <v-flex xs6>
                    <v-text-field
                    v-model="infoPublicacao.numero_citacoes"
                    label="Número de Citações"
                    outlined
                    disabled
                    />
                    </v-flex>
                </v-layout>
                </v-col>
            </v-row>
    </v-container>
    <v-container style="width:50%;">
            <v-card>
                <v-card-title class="justify-center white--text" style="background: #11063d;"> Autores da Publicação </v-card-title>
            <v-list>
                <v-list-item
                    v-for="autor in infoPublicacao.autores"
                    :key="autor.id"
                    @click="viewUser(autor.id)"
                >
                    <v-list-item-content style="width: 50%;">
                        <v-list-item-title v-text="autor.nome"></v-list-item-title>
                    </v-list-item-content>

                </v-list-item>
            </v-list>
            </v-card>
    </v-container>
  </div>
</template>

<script>
// @ is an alias to /src

export default {
  name: 'Publicacao',
  props: ['publicacao'],
  created: function(){
      // Ir á api depois
      var json = require('../../../publicacoes.json')
      var i = 0 
      for(; i < json.length; i++){
          if(json[i]._id == this.publicacao.id){
              this.infoPublicacao = {
                  ano: json[i].ano,
                  eid : json[i].eid,
                  doi : json[i].doi,
                  wos : json[i].wos,
                  local_de_publicacao : json[i].local_de_publicacao,
                  numero_citacoes : 0,
                  numero_citacoes_ultimos_3_anos: 0,
                  SJR : 100,
                  autores : json[i].autores
              }
              break;
          }
      }
  },
  methods :{
      viewUser: function(id){
          alert(id)
      }
  }
  

}
</script>


<style scoped>
.v-text-field{
    border-color: blue;
    margin-left: 5px;
    margin-right: 5px;
}
</style>