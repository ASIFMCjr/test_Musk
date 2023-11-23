<script setup>
import axios from "axios";
import { useMediaQuery } from '@vueuse/core'
const isMediumScreen = useMediaQuery('(min-width: 750px)')
const navData = await axios.get(`http://77.246.159.10/api/nav-items/`);
const navs = await navData.data.data;
console.log(navs);
</script>

<script>
import { Slide } from 'vue3-burger-menu'  // import the CSS transitions you wish to use, in this case we are using `Slide`

export default {
    components: {
        Slide // Register your component
    }
}
</script>

<template>
  <div v-if="isMediumScreen" class="nav-items">
    <a class="nav-items__a" :key="index" v-for="(nav, index) in navs" :href="'#' + nav.nav_link">
      {{ nav.nav_name }}
    </a>
  </div>
  <div v-else>
    <Slide>
      <a style="text-decoration: none;color: white;" :key="index" v-for="(nav, index) in navs" :href="'#' + nav.nav_link">
        {{ nav.nav_name }}
      </a>
    </Slide>
  </div>
</template>

<style scoped>
.nav-items {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  width: 65%;
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


@media screen and (max-width: 1050px) {
  .nav-items {
    width: 100%;
  }
}

@media screen and (max-width: 750px) {
  .nav-items {
  }
}
</style>
