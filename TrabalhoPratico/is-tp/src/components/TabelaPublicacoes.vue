<template>
  <v-card>
    <v-card-title>
      Publicações
      <v-spacer></v-spacer>
      <v-text-field
        v-model="search"
        append-icon="mdi-magnify"
        label="Pesquisar"
        single-line
        hide-details
      ></v-text-field>
    </v-card-title>
    <v-data-table
      :headers="headers"
      :items="this.publicacoes"
      :search="search"
      @click:row="viewPublicacao"
    ></v-data-table>
  </v-card>
</template>

<script>

  export default {
    props:['publicacoes'],
    data () {
      return {
        search: '', 
        headers: [
          { text: 'Título', value: 'titulo' },
          { text: 'Ano de Publicacão', value: 'ano'}
        ],
        } 
    },  
    methods: {
      viewPublicacao: function(item){
        this.$router.push({ name: 'Publicacao', params: {id : item.id}})
      }
    }
}
</script>