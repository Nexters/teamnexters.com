<template>
  <nuxt-link :to="href" class="arrow-button">
    <p
      :style="{
        color: `${color}`,
        'font-size': `${size}px`,
        'line-height': `${size + 12}px`,
      }"
    >
      {{ text }}
    </p>
    <img :style="{ width: `${size}px`, height: `${size}px` }" :src="arrow" />
  </nuxt-link>
</template>

<script>
import { defineComponent } from "@nuxtjs/composition-api";
export default defineComponent({
  name: "ArrowButton",
  props: {
    isWhite: {
      type: Boolean,
      required: false,
      default: true,
    },
    href: {
      type: String,
      required: true,
    },
    text: {
      type: String,
      required: true,
    },
    size: {
      type: Number,
      required: false,
      default: 16,
    },
  },
  computed: {
    color() {
      return this.isWhite ? "white" : "black";
    },
    arrow() {
      return this.isWhite
        ? require("~/assets/img/ic_forward.svg")
        : require("~/assets/img/ic_forward_black.svg");
    },
  },
});
</script>

<style lang="scss" scopced>
@import "~/assets/css/_device.scss";
@import "~/assets/css/setting.scss";

* {
  font-family: Spoqa Han Sans Neo;
}
.arrow-button {
  display: flex;
  flex-direction: row;
  align-items: center;
  align-content: center;
  text-decoration: none;

  p {
    display: flex;
    font-style: normal;
    font-weight: bold;
    letter-spacing: -0.02em;
  }

  img {
    margin: auto 0 auto 8px;
  }
  &:hover {
    transition: 0.3s;
    opacity: 0.6;
  }
  &:active {
    transition: 0.3s;
    opacity: 0.4;
  }
  &:active {
    transition: 0.3s;
    opacity: 0.2;
  }
}
</style>
