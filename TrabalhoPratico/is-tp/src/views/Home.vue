<template>
  <div class="home">
    <div>
      <v-img :src="require('../assets/LogoRealv3.png')" contain aspect-ratio="20"></v-img>
    </div> 
    <div style="width:70%;margin-left:auto;margin-right:auto;">
      <TabelaUsers />
    </div>  
  </div>
</template>

<script>
// @ is an alias to /src
import TabelaUsers from '../components/TabelaUsers.vue';

export default {
  name: 'Home',
  components: {
    TabelaUsers
  }
}
</script>

