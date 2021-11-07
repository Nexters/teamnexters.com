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
    <img
      :style="{ color: `${color}`, width: `${size}px`, height: `${size}px` }"
      src="~/assets/img/ic_forward.svg"
    />
  </nuxt-link>
</template>

<script>
import { defineComponent } from "@nuxtjs/composition-api";
export default defineComponent({
  name: "ArrowButton",
  props: {
    color: {
      type: String,
      required: false,
      default: "white",
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
