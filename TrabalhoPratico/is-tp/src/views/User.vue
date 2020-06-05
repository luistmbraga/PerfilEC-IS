<template>
  <div class="home">
    <v-card-title class="justify-center">
        Investigador {{utilizador.nome}}
    </v-card-title>
    <v-container class="justify-center">
        <v-text> <b> ORCID                :</b>     {{utilizador._id}} </v-text>
        <p><v-text> <b> Numero de publicacões:</b>     {{publicacoes.length}}</v-text></p>
    </v-container>
    <div style="width:70%;margin-left:auto;margin-right:auto;">
      <TabelaPublicacoes v-if="publicacoes.length!=0" :publicacoes="publicacoes" />
    </div>  
  </div>
</template>

<script>
// @ is an alias to /src
import axios from "axios"
import TabelaPublicacoes from '../components/TabelaPublicacoes.vue';

export default {
  name: 'User',
  props: ['publicacoes', 'utilizador'],
  components: {
    TabelaPublicacoes
  },
  created: async function(){
      // ir buscar o utilizador a as publicacões á API para não ficar com informação pendente das outras páginas
      let response = await axios.get("http://localhost:3050/api/users/0000-0001-6018-7346")
      console.log(response.data)
  }

}
</script>
