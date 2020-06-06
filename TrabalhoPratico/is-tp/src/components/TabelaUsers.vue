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
import axios from "axios"

  export default {
    data () {
      return {
        search: '', 
        utilizadores: [],
        headers: [
          {
            text: 'Nome do investigador',
            sortable: false,
            value: 'nome',
          },
          { text: 'ORCID', value: '_id' },
          { text: 'Publicações', value: "publicacoes.length"}
        ],
        } 
    }, 
    
    created: async function() {
        // depois ir á api ou BD
        let response = await axios.get('http://localhost:3050/api/users')
        this.utilizadores = response.data 
    }, 
    methods: {
      viewUser: function(item){
        this.$router.push({ name: 'User', params: {id: item._id }})
      }
    }
}
</script>