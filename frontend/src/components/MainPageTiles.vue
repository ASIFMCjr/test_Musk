<script setup>
import { ref } from "vue";
import axios from "axios";
defineProps({
  msg: String,
});
const tileData = await axios.get(`http://127.0.0.1:8000/api/adv-items/`);
const tiles = await tileData.data.data;

const degNum = 135;
const degText = "deg";
const deg = `${degNum}${degText}`
const classDeg = `main-item_tile`
</script>

<template>
  <div class="main-item main-item__right">
    <div class="main-grid">
      <div v-for="(tile, index) in tiles" :class="classDeg + index" class="main-item_tile">
        <p style="font-size: 1.3rem;color: rgba(255, 255, 255, 0.671);">{{ tile.adv_title_up }}</p>
        <h2 style="font-size: 4rem;margin:0;color: rgba(255, 255, 255, 0.9);">{{ tile.adv_main }}</h2>
        <p style="font-size: 1.3rem;color: rgba(255, 255, 255, 0.671);">{{ tile.adv_title_down }}</p>
      </div>
    </div>
    
  </div>
</template>

<style scoped>
.main-item {
  width: 50%;
  
}

.main-item__right {
  display: flex;
  align-items: center;
}

.main-grid {
  max-width: 400px;
  display: grid;
  margin: auto;
  grid-template-columns: repeat(2, 1fr);
  box-sizing: border-box;
}

.main-item_tile {
  margin: 5px;
  text-align: center;
  width: 200px;
  height: 200px;
  box-sizing: border-box;
  transition: 0.1s linear;
  align-items: center;
  display: flex;
  flex-direction: column;
  vertical-align: middle;
  justify-content: space-between;
}

.main-item_tile:hover {
  border-width: 1px;
  border-style: solid;
}

.main-item_tile0 {
  background-image: linear-gradient(135deg , rgba(215, 24, 24, 0) 50%,  #ffffff1b);
  
}

.main-item_tile0:hover {
  border-image: linear-gradient(135deg , rgba(0, 0, 0, 0) 60%,  #ffffff6b) 1;
  border-top: none;
  border-left: none;
}

.main-item_tile1 {
  background-image: linear-gradient(225deg , rgba(215, 24, 24, 0) 50%,  #ffffff1b);
  
}

.main-item_tile1:hover {
  border-image: linear-gradient(225deg , rgba(0, 0, 0, 0) 60%,  #ffffff6b) 1;
  border-top: none;
  border-right: none;
}

.main-item_tile2 {
  background-image: linear-gradient(45deg , rgba(215, 24, 24, 0) 50%,  #ffffff1b);
  
}

.main-item_tile2:hover {
  border-image: linear-gradient(45deg , rgba(0, 0, 0, 0) 60%,  #ffffff6b) 1;
  border-bottom: none;
  border-left: none;
}

.main-item_tile3 {
  background-image: linear-gradient(-45deg , rgba(215, 24, 24, 0) 50%,  #ffffff1b);
  
}

.main-item_tile3:hover {
  border-image: linear-gradient(-45deg , rgba(0, 0, 0, 0) 60%,  #ffffff6b) 1;
  border-bottom: none;
  border-right: none;
}

</style>
