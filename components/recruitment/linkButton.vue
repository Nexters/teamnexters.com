<template>
  <div
    class="linkButton"
    :class="type === 'DEFAULT' && 'dark'"
    @click="onClick"
  >
    {{ buttonName }}
  </div>
</template>

<script>
import { defineComponent } from "@vue/composition-api";

export default defineComponent({
  name: "LinkButton",
  props: {
    type: {
      type: String,
      require: false,
    },
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
  background-color: $background-primary;
  color: white;
  text-decoration: none;

  &:hover {
    transition: 0.3s;
    cursor: pointer;
    background: linear-gradient(0deg, rgba(0, 0, 0, 0.2), rgba(0, 0, 0, 0.2)),
      $background-primary;
  }

  &:active {
    transition: 0.3s;
    cursor: pointer;
    background: linear-gradient(0deg, rgba(0, 0, 0, 0.4), rgba(0, 0, 0, 0.4)),
      $background-primary;
  }

  &.dark {
    background-color: $background-inverse;

    &:hover {
      background: linear-gradient(
          0deg,
          rgba(255, 255, 255, 0.2),
          rgba(255, 255, 255, 0.2)
        ),
        $background-inverse;
    }

    &:active {
      background: linear-gradient(
          0deg,
          rgba(255, 255, 255, 0.4),
          rgba(255, 255, 255, 0.4)
        ),
        $background-inverse;
    }
  }
}

@include desktop {
  .linkButton {
    padding: 24px 40px;
    font-size: 24px;
    line-height: 36px;
  }
}

@include tablet {
  .linkButton {
    padding: 24px 40px;
    font-size: 24px;
    line-height: 36px;
  }
}

@include mobile {
  .linkButton {
    padding: 16px 24px;
    font-size: 16px;
    line-height: 24px;
  }
}
</style>
