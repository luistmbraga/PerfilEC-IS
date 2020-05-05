<template>
  <v-app>
    <Navbar />
    <v-content class="ma-0">
      <router-view></router-view>
    </v-content>
    <Footer />
  </v-app>
</template>


<script>
import Navbar from "./components/Navbar";
import Footer from "./components/Footer";

export default {
  components: { Navbar, Footer },
  name: "App",
  data() {
    return {};
  }
};
</script>