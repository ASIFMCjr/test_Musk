<script setup>
import { createWebHistory, createRouter } from "vue-router";
import MainPage from "./components/MainPage.vue";
import Header from "./components/Header.vue";
</script>

<template>
  <div class="screen">
    <div class="screen-inner">
      <Header />
      <MainPage msg="Main" />
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
</style>
