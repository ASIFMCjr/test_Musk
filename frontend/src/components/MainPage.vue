<script setup>
import { ref } from "vue";
import MainPageTiles from "./MainPageTiles.vue";
defineProps({
  msg: String,
});

const count = ref(0);
</script>

<template>
  <div class="main">
    <div class="main-item main-item__left">
      <h1 class="main-item__heading">
        Путешествие <br />
        <span>на красную планету</span>
      </h1>

      <button>Начать путешествие</button>
    </div>
    <Suspense>
      <MainPageTiles />

      <template #fallback>
        <span>Tiles...</span>
      </template>
    </Suspense>
  </div>
</template>

<style scoped>
.main {
  display: flex;
  flex-direction: row;
  width: 100%;
  max-width: 1300px;
  margin: auto;
  justify-content: space-between;
  height: calc(100vh - 100px);
}

.main-item {
  width: 50%;
  
}

.main-item__left {
  width: 50%;
  margin: auto;
}

.main-item__heading {
  text-align: left;
}
</style>
