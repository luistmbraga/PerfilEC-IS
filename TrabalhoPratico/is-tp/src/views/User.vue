<template>
  <div class="home">
    <v-card>
      <v-card-title class="justify-center">
          Investigador
      </v-card-title>
      <center>
        <v-text style="font-size:30px">
           {{utilizador.nome}}
        </v-text>
      </center>
      <v-container class="justify-center">
          <v-text> <b> ORCID                :</b>     {{utilizador._id}} </v-text>
          <p><v-text> <b> Numero de publicacões:</b>     {{utilizador.publicacoes.length}}</v-text></p>
      </v-container>
      <div style="width:70%;margin-left:auto;margin-right:auto;">
        <TabelaPublicacoes v-if="utilizador.publicacoes.length!=0" :publicacoes="utilizador.publicacoes" />
      </div> 
    </v-card> 
  </div>
</template>

<script>
// @ is an alias to /src
import TabelaPublicacoes from '../components/TabelaPublicacoes.vue';
import axios from "axios"

export default {
  data () {
      return {
        utilizador: {}
        } 
    }, 
  name: 'User',
  props: ['id'],
  components: {
    TabelaPublicacoes
  },
  created: async function(){
      // ir buscar o utilizador a as publicacões á API para não ficar com informação pendente das outras páginas
      var id = this.$route.params.id
      let response = await axios.get('http://localhost:3050/api/users/' + id)
      this.utilizador = response.data[0]

  }

}
</script>
