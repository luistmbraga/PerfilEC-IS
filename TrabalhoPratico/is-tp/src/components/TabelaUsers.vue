<template>
  <v-card>
    <v-card-title>
      Investigadores
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
      :items="this.utilizadores"
      :search="search"
      @click:row="viewUser"
    ></v-data-table>
  </v-card>
</template>

<script>

  export default {
    data () {
      return {
        search: '', 
        utilizadores: [],
        headers: [
          {
            text: 'Nome do investigador',
            sortable: false,
            value: 'name',
          },
          { text: 'ORCID', value: '_id' },
          { text: 'Publicações', value: 'nrPub'}
        ],
        } 
    }, 
    
    created: async function() {
        // depois ir á api ou BD
        var json = require('./../components/utilizadores.json');
        var length = json.length
        var i = 0
        for(;i< length;i++){ 
            var pub = json[i].publicacoes.length
            var obj = {name: json[i].nome, _id: json[i]._id, nrPub: pub, publicacoes: json[i].publicacoes } 
            this.utilizadores.push(obj)
        } 
    }, 
    methods: {
      viewUser: function(item){
        this.$router.push({ name: 'User', params: {id: item._id, publicacoes: item.publicacoes, utilizador: {_id: item._id, nome: item.name} }})
      }
    }
}
</script>