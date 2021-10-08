<template>
  <div class="container" @click="$router.go(-1)">
    <img class="leading" src="~/assets/img/ic_back.png" />
  </div>
</template>

<script>
import { defineComponent } from "@nuxtjs/composition-api";
export default defineComponent({
  name: "Toolbar",
});
</script>

<style lang="scss" scoped>
* {
  font-family: Spoqa Han Sans Neo;
}
.container {
  height: 56px;
  display: flex;
  flex-direction: row;
  align-items: center;
  .leading {
    margin: 16px;
    height: 24px;
    width: 24px;
    cursor: pointer;
  }
}
</style>
