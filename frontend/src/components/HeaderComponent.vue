<script setup>
import NavBar from "./NavBar.vue";

import logo from "../assets/logo.png";
import { useMediaQuery } from '@vueuse/core'

const isLargeScreen = useMediaQuery('(min-width: 1050px)')
</script>

<template>
  <div class="navbar">
    <div class="navbar-inner">
      <div v-if="isLargeScreen" class="navbar-logo">
          <img :src="logo" alt="logo" class="logo"/>
        
      </div>
      <Suspense>
        <NavBar msg="haha" />
  
        <template #fallback>
          <span>Help...</span>
        </template>
      </Suspense>
    </div>
    
  </div>
</template>

<style scoped>
.navbar {
  width: 100%;
  box-sizing: border-box;
  border-bottom: 1px solid #ffffff1b;
  border-top: 1px solid #ffffff1b;
}

.navbar-inner {
  max-width: 1300px;
  width: 100%;
  margin: auto;
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  height: 100px;
  align-items: center;
  
  padding: 0 50px;
  box-sizing: border-box;
}

.navbar-logo {
  border: 10px solid;
  border-image: url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 11 11' width='10' height='10'><g fill='white'><rect width='1' height='3'/><rect y='6' width='1' height='5'/><rect x='10' y='6' width='1' height='5'/><rect x='10' width='1' height='5'/><rect width='5' height='1'/><rect y='10' width='5' height='1'/><rect x='6' y='10' width='5' height='1'/><rect x='6' width='5' height='1'/></g></svg>") 5;
  border-radius: 5px;
  height: 100px;
  width: 300px;
  box-sizing: border-box;
  display: flex;
  position: relative;
}

.navbar-logo:after {
  content: "";
  position: absolute;
  z-index: 999;
  top: -10px;
  left: -10px;
  right: -10px;
  bottom: -10px;
  border: 1px solid rgba(255, 255, 255, 0.108);
}

.logo {
  width: 100%;
  margin: auto;
  justify-content: center;
  align-items: center;
}

@media screen and (max-width: 1000px) {

}
</style>
