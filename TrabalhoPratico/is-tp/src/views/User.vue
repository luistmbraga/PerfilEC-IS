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
import TabelaPublicacoes from '../components/TabelaPublicacoes.vue';

export default {
  name: 'User',
  props: ['publicacoes', 'utilizador'],
  components: {
    TabelaPublicacoes
  },
  created: function(){
      // ir buscar o utilizador a as publicacões á API para não ficar com informação pendente das outras páginas
      
  }

}
</script>
