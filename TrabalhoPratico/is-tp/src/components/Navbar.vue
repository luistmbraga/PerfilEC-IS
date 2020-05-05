<template>
  <nav>
    <v-toolbar dark color="grey lighten-3">
      <v-toolbar-title class="black--text">
      <div @click="goHome()"> 
        <span>Orcid</span>
        <span class="font-weight-light">Tracker</span>
      </div>
      </v-toolbar-title>
    </v-toolbar>
  </nav>
</template>

<script>
//import DropdownMenu from './DropdownMenu';

export default {
  components: {},
  data() {
    return {};
  }, 
  methods:{ 
    goHome(){ 
      this.$router.push({
            name: 'Home',  
        });
    }
  } 
};
</script>

