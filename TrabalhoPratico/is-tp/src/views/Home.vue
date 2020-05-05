<template>
  <div class="home">
    
    <v-content>
      <v-container fluid>
        <v-row align="start" justify="center">
          <v-col cols="6" sm="18" md="12">
            <div>
              <v-img :src="require('../assets/LogoRealv3.png')" contain aspect-ratio="20"></v-img>
            </div> 
          </v-col>
        </v-row>
      </v-container>
    </v-content>

    <v-content>
      <v-container fluid>
        <v-row align="center" justify="center">
          <v-col cols="12" sm="12" md="8">
            <div>
              <TabelaUsers />
            </div>
          </v-col>
        </v-row>
      </v-container>
    </v-content>
  </div>
</template>

<script>
// @ is an alias to /src
import TabelaUsers from '../components/TabelaUsers.vue';

export default {
  name: 'Home',
  components: {
    TabelaUsers
  },

}
</script>

