<script setup>
import MainPageTiles from "./MainPageTiles.vue";

</script>

<template>
  <div class="main">
    <div class="main-item main-item__left">
      <h1 class="main-item__heading">
        <span style="font-size: 3.5rem;background-image: linear-gradient(90deg, rgba(255,255,255,1) 20%, rgba(250,100,0,1) 100%);-webkit-background-clip: text;-webkit-text-fill-color: transparent;background-size: 100%;background-repeat: repeat;">ПУТЕШЕСТВИЕ</span> <br />
        <span style="font-size: 1.5rem;background-image: linear-gradient(90deg, rgba(255,255,255,1) 50%, rgb(255, 176, 123) 100%);-webkit-background-clip: text;-webkit-text-fill-color: transparent;background-size: 100%;background-repeat: repeat;">на красную планету</span>
      </h1>

      <button class="main-item__button">Начать путешествие</button>
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
  padding: 0 50px;
  box-sizing: border-box;
}

.main-item {
  width: 50%;
  
}

.main-item__left {
  width: 50%;
  justify-content: start;
  display: flex;
  flex-direction: column;
}

.main-item__heading {
  text-align: left;
  margin: 100px 0;
}
.shadow {
  filter: drop-shadow( 3px 3px 2px rgba(255, 255, 255, 0.7));
}
.main-item__button {
  width: 200px;
  height: 35px;
  background-color: #ffffff00;
  color: white;
  border-width: 1px;
  border-style: solid;
  font-size: 1rem;
  position: relative;
  border-image: linear-gradient(45deg , rgba(126, 175, 244, 0.737) 5%, rgba(46, 116, 237, 0.44) 10%, rgba(89, 127, 250, 0.657) 90%,rgba(126, 175, 244, 0.737) 10%) 5;
}

.main-item__button::after {
  content: "";
  position: absolute;
  z-index: 999;
  top: 0px;
  left: 0px;
  right: 0px;
  bottom: 0px;
  border: 6px solid;
  border-image: url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 11 11' width='10' height='10'><g fill='white'><rect class='shadow' y='6' width='1' height='5'/><rect  x='10' width='1' height='5'/><rect y='10' width='5' height='1'/><rect x='6' width='5' height='1'/></g></svg>") 5;
  border-radius: 5px;
  
}



@media screen and (max-width: 1050px) {
  .main {
    flex-direction: column;
    width: 100%;
    min-height: 100vw;
    height: 100%;
    margin: auto;
    justify-content: flex-start;
    align-items: center;
  }

  .main-item__left {
    justify-content: center;
    text-align: center;
    align-items: center;
    height: 300px;
  }

  .main-item__heading {
    text-align: center;
    margin: 50px 0;
  }

  .main-item__right {
    justify-content: center;
  }
  
}
</style>
