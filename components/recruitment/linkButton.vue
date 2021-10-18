<template>
  <div class="linkButton" @click="onClick">{{ buttonName }}</div>
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
    href: {
      type: String,
      require: false,
    },
  },
  methods: {
    onClick: function () {
      location.href = this.href;
    },
  },
});
</script>

<style lang="scss" scoped>
@import "~/assets/css/_device.scss";
@import "~/assets/css/setting.scss";

* {
  font-family: Spoqa Han Sans Neo;
}

.linkButton {
  display: inline-block;
  text-align: center;
  box-sizing: border-box;
  border-radius: 8px;
  background-color: $primary;
  color: white;
  text-decoration: none;
  &:hover {
    cursor: pointer;
  }
}

@include desktop {
  .linkButton {
    padding: 24px;
    font-size: 24px;
    line-height: 36px;
  }
}

@include tablet {
  .linkButton {
    padding: 24px;
    font-size: 24px;
    line-height: 36px;
  }
}

@include mobile {
  .linkButton {
    padding: 16px;
    font-size: 16px;
    line-height: 24px;
  }
}
</style>
