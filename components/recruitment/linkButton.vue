<template>
  <a class="linkButton" :href="link">{{ buttonName }}</a>
</template>

<script>
import { defineComponent } from "@vue/composition-api";

export default defineComponent({
  name: "LinkButton",
  props: {
    buttonName: {
      type: String,
      require: true,
    },
    link: {
      type: String,
      require: false,
    },
  },
});
</script>

<style lang="scss" scoped>
@import "~/assets/css/_device.scss";
* {
  font-family: Spoqa Han Sans Neo;
}

.linkButton {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 100%;
  box-sizing: border-box;
  border-radius: 8px;
  background-color: #6b68f7;
  color: white;
  text-decoration: none;
}

@include desktop {
  .linkButton {
    font-size: 24px;
    line-height: 36px;
  }
}

@include tablet {
  .linkButton {
    font-size: 24px;
    line-height: 36px;
  }
}

@include mobile {
  .linkButton {
    font-size: 16px;
    line-height: 24px;
  }
}
</style>
