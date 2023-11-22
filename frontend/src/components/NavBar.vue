<script setup>
import { ref, onMounted } from "vue";
import axios from "axios";

defineProps({
  msg: String,
});
const navData = await axios.get(`http://127.0.0.1:8000/api/nav-items/`);
const navs = await navData.data.data;
console.log(navs);
</script>

<template>
  <!-- <h1>{{ msg }}</h1> -->

  <div class="nav-items">
    <a class="nav-items__a" v-for="nav in navs" :href="'#' + nav.nav_link">
      {{ nav.nav_name }}
    </a>
  </div>
</template>

<style scoped>
.nav-items {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  width: 60%;
  box-sizing: border-box;
  height: 100%;
  align-items: center;
}
.nav-items__a {
  text-decoration: none;
  color: white;
  padding: 5px;
  box-sizing: border-box;
  position: relative;
  height: 30px;
  font-size: 1.05rem;
}

.nav-items__a:hover {
  box-sizing: border-box;
  color: rgba(255, 255, 255, 0.836);
  border-bottom: 1px solid rgba(244, 244, 244, 0.602);
}

@media screen and (min-width: 1000px) {
  .nav-items {
    width: 100%;
  }
}
</style>
