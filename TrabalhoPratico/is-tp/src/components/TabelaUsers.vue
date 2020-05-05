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
      :justify="center"
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
          { text: 'Publicações', value: 'publicacoes'}
        ],
        } 
    }, 
    
    created: async function() {
        var json = require('./utilizadores.json');
        this.utilizadores = json 
        var i=0; 
        for(;i<json.length;i++){ 
          if(json[i].nome != null){   
            var pub = json[i].publicacoes.length
            var obj = {name: json[i].nome, _id: json[i]._id, publicacoes: pub } 
            this.utilizadores.push(obj)
          }
        }
        console.log(this.utilizadores)
    }
}
</script>