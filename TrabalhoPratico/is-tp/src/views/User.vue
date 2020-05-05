<template>
  <div class="home">
    <v-card-title class="justify-center">
        Informações do investigador {{utilizador.nome}}
    </v-card-title>
    <div style="width:70%;margin-left:auto;margin-right:auto;">
      <TabelaPublicacoes :publicacoes="publicacoes" />
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

}
</script>
