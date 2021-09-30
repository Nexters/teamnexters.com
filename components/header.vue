<template>
  <nav>
    <ul>
      <nuxt-link to="/" class="logo"><img alt="NEXTERS_LOGO" /></nuxt-link>
      <nuxt-link
        v-for="header in headers"
        :key="header"
        :to="header.name"
        class="header-item"
      >
        {{ header.name }}
      </nuxt-link>
    </ul>
  </nav>
</template>

<script lang="ts">
import { defineComponent } from "@vue/composition-api";

export default defineComponent({
  name: "Header",
  props: {
    headers: {
      type: Array,
      required: true,
    },
  },
  setup() {
    return {};
  },
});
</script>

<style lang="scss" scoped>
nav {
  height: 73px;
  display: flex;
  align-items: center;
  .logo {
    padding: 0 48.5px 0 24px;
  }
  .header-item {
    padding: 0 48.5px 0 0;
  }
}
</style>
