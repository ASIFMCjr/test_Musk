<script setup>
import MainPage from "./components/MainPage.vue";
import HeaderComponent from "./components/HeaderComponent.vue";
</script>

<template>
  <div class="screen">
    <div class="screen-inner">
      <HeaderComponent />
      <MainPage/>
    </div>
  </div>
</template>

<style scoped>
.screen {
  background-image: url("./assets/bg.png");
  background-position: center;
  background-repeat: no-repeat;
  width: 100vw;
  height: 100vh;
  background-size: cover;
}
.screen-inner {
  margin: auto;
}

@media screen and (max-width: 1050px) {
  .screen {
    width: 100vw;
    min-height: 100vh;
    height: 100%;
  }
  
}
</style>
