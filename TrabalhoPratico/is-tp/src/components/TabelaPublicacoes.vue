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
      @click:row="viewUser"
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
          {
            text: 'Id',
            sortable: false,
            value: 'id',
          },
          { text: 'Título', value: 'titulo' },
          { text: 'Ano de Publicacão', value: 'ano'}
        ],
        } 
    },  
    methods: {
      viewUser: function(item){
        alert(item._id)
      }
    }
}
</script>