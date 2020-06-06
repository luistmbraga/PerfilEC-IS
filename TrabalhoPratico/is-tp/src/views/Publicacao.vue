<template>
  <div class="home">
    <v-card-title class="justify-center">
        Publicação 
        {{infoPublicacao.titulo}}
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
                    <v-flex xs6>
                    <v-text-field
                    v-model="infoPublicacao.issn"
                    label="ISSN"
                    outlined
                    disabled
                    />
                    </v-flex>
                </v-layout>
                </v-col>
            </v-row>
        <div v-if="infoPublicacao.source_id_issn != 'None'" >
            <a v-bind:href="linkhref" title="SCImago Journal &amp; Country Rank">
                <img border="0" v-bind:src="linksrc" alt="SCImago Journal &amp; Country Rank"  />
            </a>
        </div>
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
import axios from "axios"

export default {
    data () {
      return {
        infoPublicacao: {},
        linkhref: "",
        linksrc: ""
        } 
    },
  name: 'Publicacao',
  props: ['id'],
  created: async function(){
      // Ir á api depois
      var idPub = this.id.replace("/","%2F");
      let response = await axios.get('http://localhost:3050/api/publicacoes/' + idPub)
      this.infoPublicacao = response.data[0]
      this.linkhref = "https://www.scimagojr.com/journalsearch.php?q="+this.infoPublicacao.source_id_issn+"&amp;tip=sid&amp;exact=no"
      this.linksrc = "https://www.scimagojr.com/journal_img.php?id="+this.infoPublicacao.source_id_issn
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