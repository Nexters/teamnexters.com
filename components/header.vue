<template>
  <nav>
    <ul>
      <nuxt-link to="/" class="logo">
        <img src="~/assets/img/nexters_gnb_white.png" alt="NEXTERS_LOGO" />
      </nuxt-link>
      <nuxt-link
        v-for="header in headers"
        :key="header.name"
        :to="header.href"
        :class="{ 'header-item': true, 'white-font': isWhite }"
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
    isWhite: {
      type: Boolean,
      required: false,
      default: false,
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
    margin: 0 auto;
    padding: 0 48.5px 0 24px;
  }
  .header-item {
    padding: 0 48.5px 0 0;
    font-size: 24px;
    font-style: normal;
    font-weight: bold;
    line-height: 36px;
    letter-spacing: -0.02em;
    color: #000000;
    text-decoration: none;
  }
  .white-font {
    color: #ffffff;
  }
}
</style>
