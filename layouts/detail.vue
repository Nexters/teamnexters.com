<template>
  <div class="background">
    <toolbar />
    <nuxt />
  </div>
</template>

<script>
import { defineComponent } from "@nuxtjs/composition-api";
export default defineComponent({
  name: "DetailLayout",
});
</script>

<style class="scss" scoped>
.background {
  height: 100vh;
}
</style>
