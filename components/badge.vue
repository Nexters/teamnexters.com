<template>
  <div class="badge-container">
    <p>{{ text }}</p>
  </div>
</template>

<script>
import { defineComponent } from "@nuxtjs/composition-api";
export default defineComponent({
  name: "Badge",
  props: {
    text: {
      type: String,
      required: true,
    },
  },
});
</script>

<style lang="scss" scoped>
@import "~/assets/css/_device.scss";
@import "~/assets/css/setting.scss";

.badge-container {
  background-color: $background-accent;
  color: $background-default;
  @include desktop {
    width: 76px;
    height: 29px;
    padding: 0 3px 0 3px;
    p {
      font-size: 14px;
      line-height: 21px;
      letter-spacing: -0.02em;
    }
  }
  @include tablet {
    width: 76px;
    height: 29px;
    padding: 0 3px 0 3px;
    p {
      font-size: 14px;
      line-height: 21px;
      letter-spacing: -0.02em;
    }
  }
  @include mobile {
    width: 55px;
    height: 24px;
    padding: 0 4px 0 4px;
    p {
      font-size: 12px;
      line-height: 18px;
      letter-spacing: -0.02em;
    }
  }
  border-radius: 100px;
  display: flex;
  justify-content: center;
  align-items: center;
}
</style>
