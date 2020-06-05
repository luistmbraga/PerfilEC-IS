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
            value: 'name',
          },
          { text: 'ORCID', value: '_id' },
          { text: 'Publicações', value: 'nrPub'}
        ],
        } 
    }, 
    
    created: async function() {

        let response = await axios.get("http://localhost:3050/api/users")
        

        response.data.forEach(element => {
          console.log(element)
          var pub = element.publicacoes.length
          var obj = {name: element.nome, _id: element._id, nrPub: pub, publicacoes: element.publicacoes } 
          this.utilizadores.push(obj)
        });
    }, 
    methods: {
      viewUser: function(item){
        this.$router.push({ name: 'User', params: {id: item._id, publicacoes: item.publicacoes, utilizador: {_id: item._id, nome: item.name} }})
      }
    }
}
</script>